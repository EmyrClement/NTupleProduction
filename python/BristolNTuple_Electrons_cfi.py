import FWCore.ParameterSet.Config as cms

rootTupleElectrons = cms.EDProducer("BristolNTuple_Electrons",
    TracksInputTag = cms.InputTag('generalTracks'),
    DCSInputTag = cms.InputTag('scalersRawToDigi'),
    InputTag = cms.InputTag('cleanPatElectrons'),
    Prefix = cms.string('Electron.'),
    Suffix = cms.string(''),
    MaxSize = cms.uint32(99),
    VertexInputTag = cms.InputTag('offlineSlimmedPrimaryVertices'),
    storePFIsolation = cms.bool(False),
    debugRelease = cms.bool(False),
    BeamSpotInputTag = cms.InputTag('offlineBeamSpot'),
    ConversionsInputTag = cms.InputTag('allConversions'),
    LikelihoodInputTag = cms.InputTag('egammaIDLikelihood'),
)
