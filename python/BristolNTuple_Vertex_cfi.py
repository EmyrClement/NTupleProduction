import FWCore.ParameterSet.Config as cms

rootTupleVertex = cms.EDProducer("BristolNTuple_Vertex",
    InputTag = cms.InputTag('offlineSlimmedPrimaryVertices'),
    Prefix = cms.string('Vertex.'),
    Suffix = cms.string('')
)

