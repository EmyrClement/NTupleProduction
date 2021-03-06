import FWCore.ParameterSet.Config as cms

nTuplePFJets = cms.EDProducer("BristolNTuple_PFJets",
    InputTag = cms.InputTag('patJetsReapplyJEC'),
    Prefix = cms.string('Jets.'),
    Suffix = cms.string(''),
    minJetPtToStore = cms.double(20.),
    MaxSize = cms.uint32(99),
    JECUncertainty = cms.string('AK4PFchs'),
    ReadJECuncertainty = cms.bool(True),
    ReadJEC = cms.bool(False),
    DoVertexAssociation = cms.bool(True),
    VertexInputTag = cms.InputTag('offlineSlimmedPrimaryVertices'),
    isRealData = cms.bool(False),
)
