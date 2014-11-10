import FWCore.ParameterSet.Config as cms

rootTupleMET = cms.EDProducer("BristolNTuple_MET",
    InputTag=cms.InputTag('slimmedMETs'),
    Prefix=cms.string('MET.'),
    Suffix=cms.string(''),
)
