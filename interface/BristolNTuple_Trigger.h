#ifndef BristolNTupleTrigger
#define BristolNTupleTrigger
#include <string>

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"

class BristolNTuple_Trigger : public edm::EDProducer {
 public:
  explicit BristolNTuple_Trigger(const edm::ParameterSet&);

 private:
  void produce( edm::Event &, const edm::EventSetup & );
  void beginRun( edm::Run &, const edm::EventSetup & );
  //unsigned int findTrigger(const std::string& triggerWildCard);

  const edm::InputTag   hltInputTag_;
  const std::string pathOfInterest_;
  HLTConfigProvider hltConfig_;
  const std::string     prefix_,suffix_;
};

#endif
