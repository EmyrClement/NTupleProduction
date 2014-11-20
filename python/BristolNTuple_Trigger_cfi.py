import FWCore.ParameterSet.Config as cms

interestingPaths = [
    'HLT_IsoMu20_eta2p1_v',
    'HLT_Ele24_eta2p1_WP85_v',

    # 7e33 (25ns)
    'HLT_IsoMu20_eta2p1_v',
    'HLT_Ele28_eta2p1_WP85_Gsf_v',

    # 1.4e34 (25ns)
    'HLT_IsoMu24_eta2p1_v',
    'HLT_Ele27_WP80_v', # Currently in MC
    'HLT_Ele32_eta2p1_WP85_Gsf_v',
    'HLT_Ele32_eta2p1_WP85_Gsf_TriCentralPFJet60_50_35_v',
    'HLT_Ele32_eta2p1_WP85_Gsf_TriCentralPFJet40_v',
]

nTupleTrigger = cms.EDProducer("BristolNTuple_Trigger",
    HLTInputTag = cms.InputTag('TriggerResults','','HLT'),
    Prefix=cms.string('HLTIsoMu20eta2p1.'),
    Suffix=cms.string(''),

    PathOfInterest = cms.string('HLT_IsoMu20_eta2p1_v')

)

nTupleTriggerIsoMu20eta2p1 = nTupleTrigger.clone( Prefix='HLTIsoMu20eta2p1.', PathOfInterest='HLT_IsoMu20_eta2p1_v')
nTupleTriggerEle27WP80 = nTupleTrigger.clone( Prefix='HLTEle27WP80.', PathOfInterest='HLT_Ele27_WP80_v')

triggerSequence = cms.Sequence( nTupleTriggerIsoMu20eta2p1 + nTupleTriggerEle27WP80 )
