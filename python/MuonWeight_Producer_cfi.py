import FWCore.ParameterSet.Config as cms

eventWeightMuons = cms.EDProducer("MuonWeight_Producer",
    muonInput=cms.InputTag("topPairMuPlusJetsSelection", 'TopPairMuonPlusJetsSelection.signalMuon', 'PAT'),
    prefix = cms.string('MuonWeights.'),
    MCSampleTag = cms.string('Summer12'), #Fall11 or Summer12 or Summer11Leg
    MuonSystematic = cms.int32(0),
)

