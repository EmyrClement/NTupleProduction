#include "BristolAnalysis/NTupleTools/plugins/ElectronWeight_Producer.h"
#include "BristolAnalysis/NTupleTools/interface/ElectronWeight.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include <boost/filesystem.hpp>
#include <boost/scoped_ptr.hpp>
#include <TFile.h>

using namespace edm;
using namespace std;

ElectronWeight_Producer::ElectronWeight_Producer(const edm::ParameterSet& iConfig) :
		electronInput_(iConfig.getParameter < InputTag > ("electronInput")), //
		jetInput_(iConfig.getParameter < InputTag > ("jetInput")), //		
		prefix_(iConfig.getParameter < string > ("prefix")), //
		MCSampleTag_(iConfig.getParameter < std::string > ("MCSampleTag")) , //
		Systematic_(iConfig.getParameter<int>("ElectronSystematic")) {
	produces<std::vector<double> >();

	std::string electronIDScaleFactorsFile("BristolAnalysis/NTupleTools/data/ScaleFactors/scaleFactors_electron_id_iso.root");
	if (!boost::filesystem::exists(electronIDScaleFactorsFile)) {
	cerr << "ConfigFile::getElectronIdIsoScaleFactorsHistogram(" << electronIDScaleFactorsFile << "): could not find file" << endl;
	throw "Could not find electron ID & iso scale factors histogram file in " + electronIDScaleFactorsFile;
	}

	boost::scoped_ptr<TFile> idFile(TFile::Open(electronIDScaleFactorsFile.c_str()));
	electronIdIsoScaleFactorsHistogram_ = (boost::shared_ptr<TH2F>) (TH2F*) idFile->Get("scaleFactors")->Clone() ;
	idFile->Close();

	std::string electronTriggerEfficiencyFile("BristolAnalysis/NTupleTools/data/ScaleFactors/scaleFactors_electron_trigger.root");
	if (!boost::filesystem::exists(electronTriggerEfficiencyFile)) {
	cerr << "ConfigFile::getElectronIdIsoScaleFactorsHistogram(" << electronTriggerEfficiencyFile << "): could not find file" << endl;
	throw "Could not find electron ID & iso scale factors histogram file in " + electronTriggerEfficiencyFile;
	}

	boost::scoped_ptr<TFile> triggerFile(TFile::Open(electronTriggerEfficiencyFile.c_str()));
	electronTriggerEfficiencyHistogram_ = (boost::shared_ptr<TEfficiency>) (TEfficiency*) triggerFile->Get("data")->Clone() ;
	triggerFile->Close();

	std::string hadronLegEfficiencyFileName("BristolAnalysis/NTupleTools/data/ScaleFactors/hadronLegEfficiencies_electron.root");
	if (!boost::filesystem::exists(hadronLegEfficiencyFileName)) {
	cerr << "ConfigFile::getElectronIdIsoScaleFactorsHistogram(" << hadronLegEfficiencyFileName << "): could not find file" << endl;
	throw "Could not find electron ID & iso scale factors histogram file in " + hadronLegEfficiencyFileName;
	}

	boost::scoped_ptr<TFile> hadronLegEfficiencyFile(TFile::Open(hadronLegEfficiencyFileName.c_str()));
	hadronLegEfficiencyHistogram_ = (boost::shared_ptr<TH1F>) (TH1F*) ( (TEfficiency*) hadronLegEfficiencyFile->Get("data_1"))->GetPassedHistogram()->Clone() ;
	hadronLegEfficiencyHistogram_1_ = (boost::shared_ptr<TEfficiency>) (TEfficiency*) hadronLegEfficiencyFile->Get("data_1")->Clone() ;
	hadronLegEfficiencyHistogram_2_ = (boost::shared_ptr<TEfficiency>) (TEfficiency*) hadronLegEfficiencyFile->Get("data_2")->Clone() ;
	hadronLegEfficiencyHistogram_3_ = (boost::shared_ptr<TEfficiency>) (TEfficiency*) hadronLegEfficiencyFile->Get("data_3")->Clone() ;
	hadronLegEfficiencyFile->Close();

	double luminosity = 5050;
	for ( int bin = 0; bin <= hadronLegEfficiencyHistogram_->GetNbinsX(); ++bin ) {
		double period1 = hadronLegEfficiencyHistogram_1_->GetEfficiency( bin ) * luminosity * 0.076;
		double period2 = hadronLegEfficiencyHistogram_2_->GetEfficiency( bin ) * luminosity * 0.764;
		double period3 = hadronLegEfficiencyHistogram_3_->GetEfficiency( bin ) * luminosity * 0.16;
		double newBinContent = (period1 + period2 + period3)/luminosity;
		hadronLegEfficiencyHistogram_->SetBinContent( bin, newBinContent );
	}

}

void ElectronWeight_Producer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {

	std::vector<double> electronWeights;

	if (!iEvent.isRealData()) {
		//get jets and numberOfBtags
		edm::Handle < pat::ElectronCollection > electrons;
		iEvent.getByLabel(electronInput_, electrons);

		edm::Handle < pat::JetCollection > jets;
		iEvent.getByLabel(jetInput_, jets);

		if ( jets->size() > 0 ) {
			unsigned int jetIndex = 3;
			if ( jets->size() < 4 ) {
				jetIndex = jets->size()-1;
			}
			const pat::Jet& fourthJet(jets->at(jetIndex));

			electronWeights = ElectronWeights(*electrons, fourthJet, &*electronIdIsoScaleFactorsHistogram_, &*electronTriggerEfficiencyHistogram_, &*hadronLegEfficiencyHistogram_, Systematic_, MCSampleTag_);
		}
	}

	std::auto_ptr<std::vector<double> > electronWeightProduct(new std::vector<double>(electronWeights));
	//-----------------------------------------------------------------
	iEvent.put(electronWeightProduct);
}

void ElectronWeight_Producer::fillDescriptions(edm::ConfigurationDescriptions & descriptions) {
	edm::ParameterSetDescription desc;
	desc.add < InputTag > ("electronInput");
	desc.add < InputTag > ("jetInput");
	desc.add < string > ("prefix", "ElectronWeight_Producer");
	desc.add < string > ("MCSampleTag");
	desc.add<int>("ElectronSystematic", 0);

	descriptions.add("ElectronWeight_Producer", desc);
}

DEFINE_FWK_MODULE (ElectronWeight_Producer);

