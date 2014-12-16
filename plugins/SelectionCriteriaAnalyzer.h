#ifndef BristolSelectionCriteriaAnalyzer
#define BristolSelectionCriteriaAnalyzer

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Utilities/interface/InputTag.h"


namespace SelectionCriteria {
enum SelectionCriteria {
	MuonSelection,
	ElectronSelection,
	NUMBER_OF_SELECTION_STEPS
};

const std::string StringSelectionCriteria[NUMBER_OF_SELECTION_STEPS] = { //
		"MuonSelection", //
		"ElectronSelection"
		};
}


class SelectionCriteriaAnalyzer: public edm::EDFilter {
public:
	explicit SelectionCriteriaAnalyzer(const edm::ParameterSet&);
	virtual ~SelectionCriteriaAnalyzer();

	virtual void beginJob();
	virtual bool filter(edm::Event&, const edm::EventSetup&);
	virtual void endJob();
	virtual void beginRun(edm::Run &, const edm::EventSetup &);

	static void fillDescriptions(edm::ConfigurationDescriptions & descriptions);
private:
	// virtual void setupEventContent(edm::Event& iEvent);

	//config
	std::vector<edm::InputTag> selectionCriteriaInput_;

	bool passMuonSelection_, passElectronSelection_;

};

#endif

