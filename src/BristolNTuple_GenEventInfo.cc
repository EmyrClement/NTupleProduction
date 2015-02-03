#include "BristolAnalysis/NTupleTools/interface/BristolNTuple_GenEventInfo.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "boost/filesystem.hpp"

#include "BristolAnalysis/NTupleTools/interface/PatUtilities.h"

#include "AnalysisDataFormats/TopObjects/interface/TtGenEvent.h"


#include <iostream>

using namespace std;

BristolNTuple_GenEventInfo::BristolNTuple_GenEventInfo(const edm::ParameterSet& iConfig) : //
		genEvtInfoInputTag(iConfig.getParameter < edm::InputTag > ("GenEventInfoInputTag")), //
	    genJetsInputTag_(iConfig.getParameter<edm::InputTag>("GenJetsInputTag")),
		ttbarDecayFlags_(iConfig.getParameter < std::vector<edm::InputTag> > ("ttbarDecayFlags")), //
		puWeightsInputTag_(iConfig.getParameter < edm::InputTag > ("PUWeightsInputTag")), //
		storePDFWeights_(iConfig.getParameter<bool>("StorePDFWeights")), //
		isTTbarMC_(iConfig.getParameter<bool>("isTTbarMC")), //
		pdfWeightsInputTag_(iConfig.getParameter < edm::InputTag > ("PDFWeightsInputTag")), //
		pileupInfoSrc_(iConfig.getParameter < edm::InputTag > ("pileupInfo")), //
		tt_gen_event_input_(iConfig.getParameter < edm::InputTag > ("tt_gen_event_input")), //
	    minGenJetPt_ (iConfig.getParameter<double> ("minGenJetPt")),
	    maxGenJetAbsoluteEta_ (iConfig.getParameter<double> ("maxGenJetAbsoluteEta")),
		prefix_(iConfig.getParameter < std::string > ("Prefix")), //
		suffix_(iConfig.getParameter < std::string > ("Suffix")) {
	produces<unsigned int>(prefix_ + "ProcessID" + suffix_);
	produces<double>(prefix_ + "PtHat" + suffix_);
	produces<double>(prefix_ + "PUWeight" + suffix_);
	produces < std::vector<double> > (prefix_ + "PDFWeights" + suffix_);
	produces < std::vector<int> > (prefix_ + "PileUpInteractions" + suffix_);
	produces < std::vector<int> > (prefix_ + "NumberOfTrueInteractions" + suffix_);
	produces < std::vector<int> > (prefix_ + "PileUpOriginBX" + suffix_);
	produces<unsigned int>(prefix_ + "TtbarDecay" + suffix_);





	produces<double>(prefix_ + "leptonicTopPt" + suffix_ );

	produces<int>(prefix_ + "leptonicBGenJetIndex" + suffix_ );

	produces<double>(prefix_ + "leptonicTopPx" + suffix_ );
	produces<double>(prefix_ + "leptonicTopPy" + suffix_ );
	produces<double>(prefix_ + "leptonicTopPz" + suffix_ );
	produces<double>(prefix_ + "leptonicTopEnergy" + suffix_ );
	produces<double>(prefix_ + "hadronicTopPt" + suffix_ );
	produces<double>(prefix_ + "hadronicTopPx" + suffix_ );
	produces<double>(prefix_ + "hadronicTopPy" + suffix_ );
	produces<double>(prefix_ + "hadronicTopPz" + suffix_ );
	produces<double>(prefix_ + "hadronicTopEnergy" + suffix_ );

	produces<double>(prefix_ + "leptonicBPt" + suffix_ );
	produces<double>(prefix_ + "leptonicBPx" + suffix_ );
	produces<double>(prefix_ + "leptonicBPy" + suffix_ );
	produces<double>(prefix_ + "leptonicBPz" + suffix_ );
	produces<double>(prefix_ + "leptonicBEnergy" + suffix_ );
	produces<double>(prefix_ + "hadronicBPt" + suffix_ );
	produces<double>(prefix_ + "hadronicBPx" + suffix_ );
	produces<double>(prefix_ + "hadronicBPy" + suffix_ );
	produces<double>(prefix_ + "hadronicBPz" + suffix_ );
	produces<double>(prefix_ + "hadronicBEnergy" + suffix_ );

	produces<double>(prefix_ + "leptonicWPt" + suffix_ );
	produces<double>(prefix_ + "leptonicWPx" + suffix_ );
	produces<double>(prefix_ + "leptonicWPy" + suffix_ );
	produces<double>(prefix_ + "leptonicWPz" + suffix_ );
	produces<double>(prefix_ + "leptonicWEnergy" + suffix_ );
	produces<double>(prefix_ + "hadronicWPt" + suffix_ );
	produces<double>(prefix_ + "hadronicWPx" + suffix_ );
	produces<double>(prefix_ + "hadronicWPy" + suffix_ );
	produces<double>(prefix_ + "hadronicWPz" + suffix_ );
	produces<double>(prefix_ + "hadronicWEnergy" + suffix_ );

	produces<double>(prefix_ + "hadronicdecayquarkPt" + suffix_ );
	produces<double>(prefix_ + "hadronicdecayquarkPx" + suffix_ );
	produces<double>(prefix_ + "hadronicdecayquarkPy" + suffix_ );
	produces<double>(prefix_ + "hadronicdecayquarkPz" + suffix_ );
	produces<double>(prefix_ + "hadronicdecayquarkEnergy" + suffix_ );	
	produces<double>(prefix_ + "hadronicdecayquarkbarPt" + suffix_ );
	produces<double>(prefix_ + "hadronicdecayquarkbarPx" + suffix_ );
	produces<double>(prefix_ + "hadronicdecayquarkbarPy" + suffix_ );
	produces<double>(prefix_ + "hadronicdecayquarkbarPz" + suffix_ );
	produces<double>(prefix_ + "hadronicdecayquarkbarEnergy" + suffix_ );

	produces<double>(prefix_ + "SingleLeptonPt" + suffix_ );
	produces<double>(prefix_ + "SingleLeptonPx" + suffix_ );
	produces<double>(prefix_ + "SingleLeptonPy" + suffix_ );
	produces<double>(prefix_ + "SingleLeptonPz" + suffix_ );
	produces<double>(prefix_ + "SingleLeptonEnergy" + suffix_ );
	produces<double>(prefix_ + "SingleNeutrinoPt" + suffix_ );
	produces<double>(prefix_ + "SingleNeutrinoPx" + suffix_ );
	produces<double>(prefix_ + "SingleNeutrinoPy" + suffix_ );
	produces<double>(prefix_ + "SingleNeutrinoPz" + suffix_ );
	produces<double>(prefix_ + "SingleNeutrinoEnergy" + suffix_ );


}

void BristolNTuple_GenEventInfo::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {


	std::auto_ptr<unsigned int> processID(new unsigned int());
	std::auto_ptr<double> ptHat(new double());
	std::auto_ptr<double> PUWeight(new double());
	std::auto_ptr < std::vector<double> > pdfWeights(new std::vector<double>());
	std::auto_ptr < std::vector<int> > Number_interactions(new std::vector<int>());

	std::auto_ptr < std::vector<int> > NumberOfTrueInteractions(new std::vector<int>());
	std::auto_ptr < std::vector<int> > OriginBX(new std::vector<int>());
	std::auto_ptr<unsigned int> ttbarDecay(new unsigned int());



	std::auto_ptr<double> leptonicTopPt(new double());
	std::auto_ptr<int> leptonicBGenJetIndex(new int());
	std::auto_ptr<double> leptonicTopPx(new double());
	std::auto_ptr<double> leptonicTopPy(new double());
	std::auto_ptr<double> leptonicTopPz(new double());
	std::auto_ptr<double> leptonicTopEnergy(new double());
	std::auto_ptr<double> hadronicTopPt(new double());
	std::auto_ptr<double> hadronicTopPx(new double());
	std::auto_ptr<double> hadronicTopPy(new double());
	std::auto_ptr<double> hadronicTopPz(new double());
	std::auto_ptr<double> hadronicTopEnergy(new double());

	std::auto_ptr<double> leptonicBPt(new double());
	std::auto_ptr<double> leptonicBPx(new double());
	std::auto_ptr<double> leptonicBPy(new double());
	std::auto_ptr<double> leptonicBPz(new double());
	std::auto_ptr<double> leptonicBEnergy(new double());
	std::auto_ptr<double> hadronicBPt(new double());
	std::auto_ptr<double> hadronicBPx(new double());
	std::auto_ptr<double> hadronicBPy(new double());
	std::auto_ptr<double> hadronicBPz(new double());
	std::auto_ptr<double> hadronicBEnergy(new double());

	std::auto_ptr<double> leptonicWPt(new double());
	std::auto_ptr<double> leptonicWPx(new double());
	std::auto_ptr<double> leptonicWPy(new double());
	std::auto_ptr<double> leptonicWPz(new double());
	std::auto_ptr<double> leptonicWEnergy(new double());
	std::auto_ptr<double> hadronicWPt(new double());
	std::auto_ptr<double> hadronicWPx(new double());
	std::auto_ptr<double> hadronicWPy(new double());
	std::auto_ptr<double> hadronicWPz(new double());
	std::auto_ptr<double> hadronicWEnergy(new double());

	std::auto_ptr<double> hadronicdecayquarkPt(new double());
	std::auto_ptr<double> hadronicdecayquarkPx(new double());
	std::auto_ptr<double> hadronicdecayquarkPy(new double());
	std::auto_ptr<double> hadronicdecayquarkPz(new double());
	std::auto_ptr<double> hadronicdecayquarkEnergy(new double());
	std::auto_ptr<double> hadronicdecayquarkbarPt(new double());
	std::auto_ptr<double> hadronicdecayquarkbarPx(new double());
	std::auto_ptr<double> hadronicdecayquarkbarPy(new double());
	std::auto_ptr<double> hadronicdecayquarkbarPz(new double());
	std::auto_ptr<double> hadronicdecayquarkbarEnergy(new double());

	std::auto_ptr<double> SingleLeptonPt(new double());
	std::auto_ptr<double> SingleLeptonPx(new double());
	std::auto_ptr<double> SingleLeptonPy(new double());
	std::auto_ptr<double> SingleLeptonPz(new double());
	std::auto_ptr<double> SingleLeptonEnergy(new double());
	std::auto_ptr<double> SingleNeutrinoPt(new double());
	std::auto_ptr<double> SingleNeutrinoPx(new double());
	std::auto_ptr<double> SingleNeutrinoPy(new double());
	std::auto_ptr<double> SingleNeutrinoPz(new double());
	std::auto_ptr<double> SingleNeutrinoEnergy(new double());


	*processID.get() = 0;
	*ptHat.get() = 0.;
	*PUWeight.get() = 0.;
	*ttbarDecay.get() = 0;

	*leptonicTopPt.get() = 0;
	*leptonicTopPx.get() = 0;
	*leptonicTopPy.get() = 0;
	*leptonicTopPz.get() = 0;
	*leptonicTopEnergy.get() = 0;
	*hadronicTopPt.get() = 0;
	*hadronicTopPx.get() = 0;
	*hadronicTopPy.get() = 0;
	*hadronicTopPz.get() = 0;
	*hadronicTopEnergy.get() = 0;

	*leptonicBPt.get() = 0;
	*leptonicBPx.get() = 0;
	*leptonicBPy.get() = 0;
	*leptonicBPz.get() = 0;
	*leptonicBEnergy.get() = 0;
	*hadronicBPt.get() = 0;
	*hadronicBPx.get() = 0;
	*hadronicBPy.get() = 0;
	*hadronicBPz.get() = 0;
	*hadronicBEnergy.get() = 0;

	*leptonicWPt.get() = 0;
	*leptonicWPx.get() = 0;
	*leptonicWPy.get() = 0;
	*leptonicWPz.get() = 0;
	*leptonicWEnergy.get() = 0;
	*hadronicWPt.get() = 0;
	*hadronicWPx.get() = 0;
	*hadronicWPy.get() = 0;
	*hadronicWPz.get() = 0;
	*hadronicWEnergy.get() = 0;

	*hadronicdecayquarkPt.get() = 0;
	*hadronicdecayquarkPx.get() = 0;
	*hadronicdecayquarkPy.get() = 0;
	*hadronicdecayquarkPz.get() = 0;
	*hadronicdecayquarkEnergy.get() = 0;
	*hadronicdecayquarkbarPt.get() = 0;
	*hadronicdecayquarkbarPx.get() = 0;
	*hadronicdecayquarkbarPy.get() = 0;
	*hadronicdecayquarkbarPz.get() = 0;
	*hadronicdecayquarkbarEnergy.get() = 0;

	*SingleLeptonPt.get() = 0;
	*SingleLeptonPx.get() = 0;
	*SingleLeptonPy.get() = 0;
	*SingleLeptonPz.get() = 0;
	*SingleLeptonEnergy.get() = 0;
	*SingleNeutrinoPt.get() = 0;
	*SingleNeutrinoPx.get() = 0;
	*SingleNeutrinoPy.get() = 0;
	*SingleNeutrinoPz.get() = 0;
	*SingleNeutrinoEnergy.get() = 0;

	*leptonicBGenJetIndex.get() = -1;

	//-----------------------------------------------------------------
	if (!iEvent.isRealData()) {
		// GenEventInfo Part
		edm::Handle < GenEventInfoProduct > genEvtInfoProduct;
		iEvent.getByLabel(genEvtInfoInputTag, genEvtInfoProduct);



		if (genEvtInfoProduct.isValid()) {
			edm::LogInfo("BristolNTuple_GenEventInfoInfo") << "Successfully obtained " << genEvtInfoInputTag;

			*processID.get() = genEvtInfoProduct->signalProcessID();
			*ptHat.get() = (genEvtInfoProduct->hasBinningValues() ? genEvtInfoProduct->binningValues()[0] : 0.);

		} else {
			edm::LogError("BristolNTuple_GenEventInfoError") << "Error! Can't get the product " << genEvtInfoInputTag;
		}

		// // PU Weights Part
		// edm::Handle<double> puWeightsHandle;
		// iEvent.getByLabel(puWeightsInputTag_, puWeightsHandle);

		// if (puWeightsHandle.isValid()) {
		// 	edm::LogInfo("BristolNTuple_GenEventInfoInfo") << "Successfully obtained " << puWeightsInputTag_;

		// 	*PUWeight.get() = *puWeightsHandle;

		// } else {
		// 	edm::LogError("BristolNTuple_GenEventInfoError") << "Error! Can't get the product " << puWeightsInputTag_;
		// }

		// // PDF Weights Part
		// if (storePDFWeights_) {
		// 	edm::Handle < std::vector<double> > pdfWeightsHandle;
		// 	iEvent.getByLabel(pdfWeightsInputTag_, pdfWeightsHandle);

		// 	if (pdfWeightsHandle.isValid()) {
		// 		edm::LogInfo("BristolNTuple_GenEventInfoInfo") << "Successfully obtained " << pdfWeightsInputTag_;

		// 		*pdfWeights.get() = *pdfWeightsHandle;

		// 	} else {
		// 		edm::LogError("BristolNTuple_GenEventInfoError") << "Error! Can't get the product "
		// 				<< pdfWeightsInputTag_;
		// 	}
		// }
		// // PileupSummary Part
		// edm::Handle < std::vector<PileupSummaryInfo> > puInfo;
		// iEvent.getByLabel(pileupInfoSrc_, puInfo);

		// if (puInfo.isValid()) {

		// 	for (std::vector<PileupSummaryInfo>::const_iterator it = puInfo->begin(); it != puInfo->end(); ++it) {
		// 		Number_interactions->push_back(it->getPU_NumInteractions());
		// 		OriginBX->push_back(it->getBunchCrossing());
		// 		NumberOfTrueInteractions->push_back(it->getTrueNumInteractions());
		// 	}
		// } else {
		// 	edm::LogError("BristolNTuple_PileUpError") << "Error! Can't get the product " << pileupInfoSrc_;
		// }

		//identify ttbar decay mode
		if (isTTbarMC_) {







			if (ttbarDecayFlags_.size() != TTbarDecay::NumberOfDecayModes - 1) {
				edm::LogError("BristolNTuple_GenEventError")
						<< "Error! Not enough flags given to describe all decay modes." << "Expecting "
						<< TTbarDecay::NumberOfDecayModes - 1 << " got " << ttbarDecayFlags_.size();
			}
			unsigned short numberOfIdentifiedModes(0);
			for (unsigned short mode = 0; mode < ttbarDecayFlags_.size(); ++mode) {
				bool result = passesFilter(iEvent, ttbarDecayFlags_.at(mode));
				if (result) {
					++numberOfIdentifiedModes;
					*ttbarDecay.get() = mode + 1; //0 == not ttbar, first decay = 1, first filter = 0
					std::cout << "TTBAR DECAY = " << *ttbarDecay.get() << std::endl;

				}
			}
			if (numberOfIdentifiedModes > 1) {
				std::cout << "PANIC" << std::endl;
				edm::LogError("BristolNTuple_GenEventError") << "Error! Found more than one compatible decay mode:"
						<< numberOfIdentifiedModes;
			}

			// Only get top parton info if ttbar decay chain has been identified
			// t->Ws (~1% of top decays) are not recognised, and are ignored.
			if (numberOfIdentifiedModes==1 ) {

				// Get parton info
				edm::Handle < TtGenEvent > ttGenEvt;
				iEvent.getByLabel(tt_gen_event_input_, ttGenEvt);

				if ( ttGenEvt->isSemiLeptonic() ) {

					*leptonicTopPt.get() = ttGenEvt->leptonicDecayTop()->pt();
					*leptonicTopPx.get() = ttGenEvt->leptonicDecayTop()->px();
					*leptonicTopPy.get() = ttGenEvt->leptonicDecayTop()->py();
					*leptonicTopPz.get() = ttGenEvt->leptonicDecayTop()->pz();
					*leptonicTopEnergy.get() = ttGenEvt->leptonicDecayTop()->energy();
					*hadronicTopPt.get() = ttGenEvt->hadronicDecayTop()->pt();
					*hadronicTopPx.get() = ttGenEvt->hadronicDecayTop()->px();
					*hadronicTopPy.get() = ttGenEvt->hadronicDecayTop()->py();
					*hadronicTopPz.get() = ttGenEvt->hadronicDecayTop()->pz();
					*hadronicTopEnergy.get() = ttGenEvt->hadronicDecayTop()->energy();

	
					*leptonicBPt.get() = ttGenEvt->leptonicDecayB()->pt();
					*leptonicBPx.get() = ttGenEvt->leptonicDecayB()->px();
					*leptonicBPy.get() = ttGenEvt->leptonicDecayB()->py();
					*leptonicBPz.get() = ttGenEvt->leptonicDecayB()->pz();
					*leptonicBEnergy.get() = ttGenEvt->leptonicDecayB()->energy();
					*hadronicBPt.get() = ttGenEvt->hadronicDecayB()->pt();
					*hadronicBPx.get() = ttGenEvt->hadronicDecayB()->px();
					*hadronicBPy.get() = ttGenEvt->hadronicDecayB()->py();
					*hadronicBPz.get() = ttGenEvt->hadronicDecayB()->pz();
					*hadronicBEnergy.get() = ttGenEvt->hadronicDecayB()->energy();
	



					*leptonicWPt.get() = ttGenEvt->leptonicDecayW()->pt();
					*leptonicWPx.get() = ttGenEvt->leptonicDecayW()->px();
					*leptonicWPy.get() = ttGenEvt->leptonicDecayW()->py();
					*leptonicWPz.get() = ttGenEvt->leptonicDecayW()->pz();
					*leptonicWEnergy.get() = ttGenEvt->leptonicDecayW()->energy();
					*hadronicWPt.get() = ttGenEvt->hadronicDecayW()->pt();
					*hadronicWPx.get() = ttGenEvt->hadronicDecayW()->px();
					*hadronicWPy.get() = ttGenEvt->hadronicDecayW()->py();
					*hadronicWPz.get() = ttGenEvt->hadronicDecayW()->pz();
					*hadronicWEnergy.get() = ttGenEvt->hadronicDecayW()->energy();
				
					*hadronicdecayquarkPt.get() = ttGenEvt->hadronicDecayQuark()->pt();
					*hadronicdecayquarkPx.get() = ttGenEvt->hadronicDecayQuark()->px();
					*hadronicdecayquarkPy.get() = ttGenEvt->hadronicDecayQuark()->py();
					*hadronicdecayquarkPz.get() = ttGenEvt->hadronicDecayQuark()->pz();
					*hadronicdecayquarkEnergy.get() = ttGenEvt->hadronicDecayQuark()->energy();
					*hadronicdecayquarkbarPt.get() = ttGenEvt->hadronicDecayQuarkBar()->pt();
					*hadronicdecayquarkbarPx.get() = ttGenEvt->hadronicDecayQuarkBar()->px();
					*hadronicdecayquarkbarPy.get() = ttGenEvt->hadronicDecayQuarkBar()->py();
					*hadronicdecayquarkbarPz.get() = ttGenEvt->hadronicDecayQuarkBar()->pz();
					*hadronicdecayquarkbarEnergy.get() = ttGenEvt->hadronicDecayQuarkBar()->energy();

					*SingleLeptonPt.get() = ttGenEvt->singleLepton()->pt();
					*SingleLeptonPx.get() = ttGenEvt->singleLepton()->px();
					*SingleLeptonPy.get() = ttGenEvt->singleLepton()->py();
					*SingleLeptonPx.get() = ttGenEvt->singleLepton()->pz();
					*SingleLeptonEnergy.get() = ttGenEvt->singleLepton()->energy();
					*SingleNeutrinoPt.get() = ttGenEvt->singleNeutrino()->pt();
					*SingleNeutrinoPx.get() = ttGenEvt->singleNeutrino()->px();
					*SingleNeutrinoPy.get() = ttGenEvt->singleNeutrino()->py();
					*SingleNeutrinoPx.get() = ttGenEvt->singleNeutrino()->pz();
					*SingleNeutrinoEnergy.get() = ttGenEvt->singleNeutrino()->energy();

					// Get partons that should result in a gen jet
					const reco::GenParticle * hadronicDecayQuark = ttGenEvt->hadronicDecayQuark();
					const reco::GenParticle * hadronicDecayQuarkBar = ttGenEvt->hadronicDecayQuarkBar();
					const reco::GenParticle * leptonicDecayB = ttGenEvt->leptonicDecayB();
					const reco::GenParticle * hadronicDecayB = ttGenEvt->hadronicDecayB();

					// Put these in a vector to pass in to JetPartonMatching
					const vector< const reco::Candidate* > partonsToMatch = { hadronicDecayQuark, hadronicDecayQuarkBar, leptonicDecayB, hadronicDecayB };

					// Get gen jets
					edm::Handle < reco::GenJetCollection > genJets;
					iEvent.getByLabel(genJetsInputTag_, genJets);

					// Get subset of gen jets that are stored in ntuple
					vector<reco::GenJet> genJetsInNtuple;
					for (reco::GenJetCollection::const_iterator it = genJets->begin(); it != genJets->end(); ++it) {


						if (it->pt() < minGenJetPt_ || fabs(it->eta()) > maxGenJetAbsoluteEta_ )
							continue;

						genJetsInNtuple.push_back( *it );
					}

					// Jet -> parton matching from:
					// https://github.com/cms-sw/cmssw/blob/CMSSW_7_3_X/TopQuarkAnalysis/TopTools/interface/JetPartonMatching.h
					JetPartonMatching matching( partonsToMatch, genJetsInNtuple, 0, true, true, 0.3 );

					// Store indices of matched gen jets
					*leptonicBGenJetIndex = matching.getMatchForParton(2);
				}
			}
		}
	}

	//-----------------------------------------------------------------
	iEvent.put(processID, prefix_ + "ProcessID" + suffix_);
	iEvent.put(ptHat, prefix_ + "PtHat" + suffix_);
	iEvent.put(PUWeight, prefix_ + "PUWeight" + suffix_);
	iEvent.put(pdfWeights, prefix_ + "PDFWeights" + suffix_);
	iEvent.put(Number_interactions, prefix_ + "PileUpInteractions" + suffix_);
	iEvent.put(NumberOfTrueInteractions, prefix_ + "NumberOfTrueInteractions" + suffix_);
	iEvent.put(OriginBX, prefix_ + "PileUpOriginBX" + suffix_);
	iEvent.put(ttbarDecay, prefix_ + "TtbarDecay" + suffix_);

	iEvent.put(leptonicTopPt, prefix_ + "leptonicTopPt" + suffix_);
	iEvent.put(leptonicBGenJetIndex, prefix_ + "leptonicBGenJetIndex" + suffix_);
	iEvent.put(leptonicTopPx, prefix_ + "leptonicTopPx" + suffix_);
	iEvent.put(leptonicTopPy, prefix_ + "leptonicTopPy" + suffix_);
	iEvent.put(leptonicTopPz, prefix_ + "leptonicTopPz" + suffix_);
	iEvent.put(leptonicTopEnergy, prefix_ + "leptonicTopEnergy" + suffix_);
	iEvent.put(hadronicTopPt, prefix_ + "hadronicTopPt" + suffix_);
	iEvent.put(hadronicTopPx, prefix_ + "hadronicTopPx" + suffix_);
	iEvent.put(hadronicTopPy, prefix_ + "hadronicTopPy" + suffix_);
	iEvent.put(hadronicTopPz, prefix_ + "hadronicTopPz" + suffix_);
	iEvent.put(hadronicTopEnergy, prefix_ + "hadronicTopEnergy" + suffix_);

	iEvent.put(leptonicBPt, prefix_ + "leptonicBPt" + suffix_);
	iEvent.put(leptonicBPx, prefix_ + "leptonicBPx" + suffix_);
	iEvent.put(leptonicBPy, prefix_ + "leptonicBPy" + suffix_);
	iEvent.put(leptonicBPz, prefix_ + "leptonicBPz" + suffix_);
	iEvent.put(leptonicBEnergy, prefix_ + "leptonicBEnergy" + suffix_);
	iEvent.put(hadronicBPt, prefix_ + "hadronicBPt" + suffix_);
	iEvent.put(hadronicBPx, prefix_ + "hadronicBPx" + suffix_);
	iEvent.put(hadronicBPy, prefix_ + "hadronicBPy" + suffix_);
	iEvent.put(hadronicBPz, prefix_ + "hadronicBPz" + suffix_);
	iEvent.put(hadronicBEnergy, prefix_ + "hadronicBEnergy" + suffix_);

	iEvent.put(leptonicWPt, prefix_ + "leptonicWPt" + suffix_);
	iEvent.put(leptonicWPx, prefix_ + "leptonicWPx" + suffix_);
	iEvent.put(leptonicWPy, prefix_ + "leptonicWPy" + suffix_);
	iEvent.put(leptonicWPz, prefix_ + "leptonicWPz" + suffix_);
	iEvent.put(leptonicWEnergy, prefix_ + "leptonicWEnergy" + suffix_);
	iEvent.put(hadronicWPt, prefix_ + "hadronicWPt" + suffix_);
	iEvent.put(hadronicWPx, prefix_ + "hadronicWPx" + suffix_);
	iEvent.put(hadronicWPy, prefix_ + "hadronicWPy" + suffix_);
	iEvent.put(hadronicWPz, prefix_ + "hadronicWPz" + suffix_);
	iEvent.put(hadronicWEnergy, prefix_ + "hadronicWEnergy" + suffix_);

	iEvent.put(hadronicdecayquarkPt, prefix_ + "hadronicdecayquarkPt" + suffix_);
	iEvent.put(hadronicdecayquarkPx, prefix_ + "hadronicdecayquarkPx" + suffix_);
	iEvent.put(hadronicdecayquarkPy, prefix_ + "hadronicdecayquarkPy" + suffix_);
	iEvent.put(hadronicdecayquarkPz, prefix_ + "hadronicdecayquarkPz" + suffix_);
	iEvent.put(hadronicdecayquarkEnergy, prefix_ + "hadronicdecayquarkEnergy" + suffix_);
	iEvent.put(hadronicdecayquarkbarPt, prefix_ + "hadronicdecayquarkbarPt" + suffix_);
	iEvent.put(hadronicdecayquarkbarPx, prefix_ + "hadronicdecayquarkbarPx" + suffix_);
	iEvent.put(hadronicdecayquarkbarPy, prefix_ + "hadronicdecayquarkbarPy" + suffix_);
	iEvent.put(hadronicdecayquarkbarPz, prefix_ + "hadronicdecayquarkbarPz" + suffix_);
	iEvent.put(hadronicdecayquarkbarEnergy, prefix_ + "hadronicdecayquarkbarEnergy" + suffix_);

	iEvent.put(SingleLeptonPt, prefix_ + "SingleLeptonPt" + suffix_);
	iEvent.put(SingleLeptonPx, prefix_ + "SingleLeptonPx" + suffix_);
	iEvent.put(SingleLeptonPy, prefix_ + "SingleLeptonPy" + suffix_);
	iEvent.put(SingleLeptonPz, prefix_ + "SingleLeptonPz" + suffix_);
	iEvent.put(SingleLeptonEnergy, prefix_ + "SingleLeptonEnergy" + suffix_);
	iEvent.put(SingleNeutrinoPt, prefix_ + "SingleNeutrinoPt" + suffix_);
	iEvent.put(SingleNeutrinoPx, prefix_ + "SingleNeutrinoPx" + suffix_);
	iEvent.put(SingleNeutrinoPy, prefix_ + "SingleNeutrinoPy" + suffix_);
	iEvent.put(SingleNeutrinoPz, prefix_ + "SingleNeutrinoPz" + suffix_);
	iEvent.put(SingleNeutrinoEnergy, prefix_ + "SingleNeutrinoEnergy" + suffix_);

}
