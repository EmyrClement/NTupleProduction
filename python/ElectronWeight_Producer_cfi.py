import FWCore.ParameterSet.Config as cms

eventWeightElectrons = cms.EDProducer("ElectronWeight_Producer",
    electronInput=cms.InputTag("topPairEPlusJetsSelection", 'TopPairElectronPlusJetsSelection.signalElectron', 'PAT'),
    jetInput=cms.InputTag("topPairEPlusJetsSelection", 'TopPairElectronPlusJetsSelection.cleanedJets', 'PAT'),
    prefix = cms.string('ElectronWeights.'),
    MCSampleTag = cms.string('Summer12'), #Fall11 or Summer12 or Summer11Leg
    ElectronSystematic = cms.int32(0),
)

