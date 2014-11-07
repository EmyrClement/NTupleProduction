import FWCore.ParameterSet.Config as cms

rootTuplePFJets = cms.EDProducer("BristolNTuple_PFJets",
    InputTag = cms.InputTag('cleanPatJetsAK5PF'),
    Prefix = cms.string('PFJet.'),
    Suffix = cms.string(''),
    MaxSize = cms.uint32(99),
    JECUncertainty = cms.string('AK5PF'),
    ReadJECuncertainty = cms.bool(False),
    DoVertexAssociation = cms.bool(True),
    VertexInputTag = cms.InputTag('offlineSlimmedPrimaryVertices'),
    isRealData = cms.bool(False)
)
