import FWCore.ParameterSet.Config as cms

rootTupleTrigger = cms.EDProducer("BristolNTuple_Trigger",
    L1InputTag  = cms.InputTag('gtDigis'),
    HLTInputTag = cms.InputTag('TriggerResults','','HLT'),
    Prefix=cms.string('Trigger.'),
    Suffix=cms.string(''),
    HLTPathsOfInterest_Signal = cms.vstring(


    #========== 2015 data ==============
    # 5e33 (50ns)
    'HLT_IsoMu20_v',
    'HLT_IsoMu20_eta2p1_v',
    'HLT_Ele24_eta2p1_WP85_v',

    # 7e33 (25ns)
    'HLT_IsoMu20_v',
    'HLT_IsoMu20_eta2p1_v',
    'HLT_Ele28_eta2p1_WP85_Gsf_v',

    # 1.4e34 (25ns)
    'HLT_IsoMu24_eta2p1_v',
    'HLT_Ele32_eta2p1_WP85_Gsf_v',
    'HLT_Ele32_eta2p1_WP85_Gsf_TriCentralPFJet60_50_35_v',
    'HLT_Ele32_eta2p1_WP85_Gsf_TriCentralPFJet40_v',
 ),                              
    HLTPathsOfInterest_Other = cms.vstring(
))
