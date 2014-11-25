import FWCore.ParameterSet.Config as cms

topPairEPlusJetsSelection = cms.EDFilter('TopPairElectronPlusJetsSelectionFilter',
    # Specify input collections
    jetInput=cms.InputTag("slimmedJets"),
    electronInput=cms.InputTag("slimmedElectrons"),
    muonInput=cms.InputTag("slimmedMuons"),
    HLTInput=cms.InputTag('TriggerResults', '', 'HLT'),

    # Lepton cuts
    minSignalElectronPt=cms.double(30.),
    maxSignalElectronEta=cms.double(2.5),
    minLooseMuonPt=cms.double(10.),
    maxLooseMuonEta=cms.double(2.5),
    minLooseElectronPt=cms.double(20.),
    maxLooseElectronEta=cms.double(2.5),

    #jet cuts
    min1JetPt=cms.double(30.),
    min2JetPt=cms.double(30.),
    min3JetPt=cms.double(30.),
    min4JetPt=cms.double(30.),

    # Jet cleaning delta R
    cleaningDeltaR=cms.double(0.3),

    # B Jet Selection
    bJetDiscriminator=cms.string('combinedSecondaryVertexBJetTags'),
    minBJetDiscriminator=cms.double(0.679),
    
    prefix=cms.untracked.string('TopPairElectronPlusJetsSelection.'),
    MCSampleTag = cms.string('Summer12'),#Fall11 or Summer12 or Summer11Leg

    #flags
    debug=cms.untracked.bool(False),
    taggingMode=cms.bool(False),

    tagAndProbeStudies = cms.bool(False),
    dropTriggerSelection = cms.bool(False),
    bSelectionInTaggingMode = cms.bool(False),
    nonIsolatedElectronSelection = cms.bool(False),
    invertedConversionSelection = cms.bool(False),
)

