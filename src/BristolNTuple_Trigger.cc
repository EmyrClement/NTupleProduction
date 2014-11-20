#include "BristolAnalysis/NTupleTools/interface/BristolNTuple_Trigger.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutRecord.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "BristolAnalysis/NTupleTools/interface/PatUtilities.h"

using namespace std;

BristolNTuple_Trigger::BristolNTuple_Trigger(const edm::ParameterSet& iConfig) :
		hltInputTag_(iConfig.getParameter < edm::InputTag > ("HLTInputTag")), //
		pathOfInterest_(iConfig.getParameter <std::string> ("PathOfInterest")), //
		prefix_(iConfig.getParameter <std::string> ("Prefix")), //
		suffix_(iConfig.getParameter < std::string > ("Suffix")) {

	produces < bool > (prefix_ + "Fired" + suffix_ );
	// produces < unsigned short > (prefix_ + "Version" + suffix_ );
	// produces < unsigned short > (prefix_ + "Prescale" + suffix_ );
}

void BristolNTuple_Trigger::beginRun(edm::Run& iRun, const edm::EventSetup& iSetup) {
}

void BristolNTuple_Trigger::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {

	std::auto_ptr < bool > fired(new bool(false));
	// std::auto_ptr < unsigned short > version(new unsigned short);
	// std::auto_ptr < unsigned short > prescale(new unsigned short);

	edm::Handle < edm::TriggerResults > triggerResults;
	iEvent.getByLabel(hltInputTag_, triggerResults);

    const edm::TriggerNames &names = iEvent.triggerNames(*triggerResults);
	unsigned int triggerIndex = 9999;
    for (unsigned int i = 0, n = triggerResults->size(); i < n; ++i) {
    	if ( names.triggerName(i).find(pathOfInterest_) != std::string::npos ) {
    		triggerIndex = i;
    	}
	}

	if ( triggerIndex < triggerResults->size() ) {
		*fired = triggerResults->accept(triggerIndex);
	}
	else {
		std::cout << "Looking for : " << pathOfInterest_ << " but failed" << std::endl;
	}

	//-----------------------------------------------------------------
	// put vectors in the event

	iEvent.put(fired, prefix_ + "Fired" + suffix_);
	// iEvent.put(version, prefix_ + "Version" + suffix_ );
	// iEvent.put(prescale, prefix_ + "Prescale" + suffix_ );

}
