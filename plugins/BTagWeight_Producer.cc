#include "BristolAnalysis/NTupleTools/plugins/BTagWeight_Producer.h"
#include "BristolAnalysis/NTupleTools/interface/BTagWeight.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Framework/interface/MakerMacros.h"

using namespace edm;
using namespace std;

BTagWeight_Producer::BTagWeight_Producer(const edm::ParameterSet& iConfig) :
		numberOfTagsInput_(consumes<unsigned int> (iConfig.getParameter < InputTag > ("numberOfTagsInput"))), //
		jetInput_(consumes< pat::JetCollection > (iConfig.getParameter < InputTag > ("jetInput"))), //
		prefix_(iConfig.getParameter < string > ("prefix")), //
		MCSampleTag_(iConfig.getParameter < std::string > ("MCSampleTag")) , //
		targetBtagMultiplicity_(iConfig.getParameter<unsigned int>("targetBtagMultiplicity")), //
		BTagSystematic_(iConfig.getParameter<int>("BTagSystematic")) {
	produces<double>();
}

void BTagWeight_Producer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {
	edm::Handle<unsigned int> numberOfBtags;
	iEvent.getByToken(numberOfTagsInput_, numberOfBtags);

	unsigned int numberOfBjets(*numberOfBtags);

	std::vector<double> bjetWeights;
	double btagWeight(1.);

	if (!iEvent.isRealData()) {
		//get jets and numberOfBtags
		edm::Handle < pat::JetCollection > jets;
		iEvent.getByToken(jetInput_, jets);
		bjetWeights = BjetWeights(*jets, numberOfBjets, BTagSystematic_, MCSampleTag_);

		btagWeight = 0;
		//calculate inclusive weights
		for (unsigned int btag = targetBtagMultiplicity_; btag <= numberOfBjets; ++btag) {
			btagWeight += bjetWeights.at(btag);
		}
	}

	std::auto_ptr<double> btagWeightProduct(new double(btagWeight));
	//-----------------------------------------------------------------
	iEvent.put(btagWeightProduct);
}

void BTagWeight_Producer::fillDescriptions(edm::ConfigurationDescriptions & descriptions) {
	edm::ParameterSetDescription desc;
	desc.add < InputTag > ("numberOfTagsInput");
	desc.add < InputTag > ("jetInput");
	desc.add < string > ("prefix", "BTagWeight_Producer");
	desc.add < string > ("MCSampleTag");
	desc.add<unsigned int>("targetBtagMultiplicity", 0);
	desc.add<int>("BTagSystematic", 0);

	descriptions.add("BTagWeight_Producer", desc);
}

DEFINE_FWK_MODULE (BTagWeight_Producer);

