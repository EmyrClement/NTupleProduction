# import default nTuple stub
from BristolAnalysis.NTupleTools.NTupleTools_cff import *
#NTuple content
from BristolAnalysis.NTupleTools.NTupler_cff import *
setup_ntupler(process, cms, options)

##########################################################################################
#            General
##########################################################################################
process.load( 'TopQuarkAnalysis.TopSkimming.TtFullyHadronicFilter_cfi' )
process.load( 'TopQuarkAnalysis.TopSkimming.TtFullyLeptonicFilter_cfi' )
process.load( 'TopQuarkAnalysis.TopSkimming.TtSemiLeptonicFilter_cfi' )

process.load( 'BristolAnalysis.NTupleTools.TopPairElectronPlusJetsSelectionFilter_cfi' )
process.load( 'BristolAnalysis.NTupleTools.TopPairMuonPlusJetsSelectionFilter_cfi' )

# Selection filters in tagging mode for monitoring cut flow
process.topPairEPlusJetsSelection.taggingMode = cms.bool( True )
process.topPairMuPlusJetsSelection.taggingMode = cms.bool( True )
# Selection filters that will actually apply selection
process.topPairEPlusJetsSelectionApply = process.topPairEPlusJetsSelection.clone( taggingMode = cms.bool(False) )
process.topPairMuPlusJetsSelectionApply = process.topPairMuPlusJetsSelection.clone( taggingMode = cms.bool(False) )
# Selection filters for control regions
process.topPairMuPlusJetsNonIsolatedSelection = process.topPairMuPlusJetsSelection.clone( nonIsolatedMuonSelection = cms.bool(True), taggingMode = cms.bool(False))
process.topPairEPlusJetsNonIsolatedSelection = process.topPairEPlusJetsSelection.clone( nonIsolatedElectronSelection = cms.bool(True), taggingMode = cms.bool(False))
process.topPairEPlusJetsInvertedConversionSelection = process.topPairEPlusJetsSelection.clone( invertedConversionSelection = cms.bool(True), taggingMode = cms.bool(False))

# Filters characterizing tt decay in tagging mode
process.ttFullHadronicFilter.taggingMode = cms.bool( True )
process.ttFullLeptonicFilter.taggingMode = cms.bool( True )
process.ttSemiLeptonicElectronFilter.taggingMode = cms.bool( True )
process.ttSemiLeptonicMuonFilter.taggingMode = cms.bool( True )
process.ttSemiLeptonicTauFilter.taggingMode = cms.bool( True )
process.ttFullLeptonicEEFilter.taggingMode = cms.bool( True )
process.ttFullLeptonicMuMuFilter.taggingMode = cms.bool( True )
process.ttFullLeptonicTauTauFilter.taggingMode = cms.bool( True )
process.ttFullLeptonicETauFilter.taggingMode = cms.bool( True )
process.ttFullLeptonicEMuFilter.taggingMode = cms.bool( True )
process.ttFullLeptonicMuTauFilter.taggingMode = cms.bool( True )

if options.isMCatNLO:
    process.ttFullHadronicFilter.useMCATNLO = cms.bool( True )
    process.ttFullLeptonicFilter.useMCATNLO = cms.bool( True )
    process.ttSemiLeptonicElectronFilter.useMCATNLO = cms.bool( True )
    process.ttSemiLeptonicMuonFilter.useMCATNLO = cms.bool( True )
    process.ttSemiLeptonicTauFilter.useMCATNLO = cms.bool( True )
    process.ttFullLeptonicEEFilter.useMCATNLO = cms.bool( True )
    process.ttFullLeptonicMuMuFilter.useMCATNLO = cms.bool( True )
    process.ttFullLeptonicTauTauFilter.useMCATNLO = cms.bool( True )
    process.ttFullLeptonicETauFilter.useMCATNLO = cms.bool( True )
    process.ttFullLeptonicEMuFilter.useMCATNLO = cms.bool( True )
    process.ttFullLeptonicMuTauFilter.useMCATNLO = cms.bool( True )

if options.CMSSW == '44X':
    process.topPairEPlusJetsSelection.MCSampleTag = cms.string( 'Fall11' )  
    process.topPairMuPlusJetsSelection.MCSampleTag = cms.string( 'Fall11' )  
else:
    process.topPairEPlusJetsSelection.MCSampleTag = cms.string( 'Summer12' )  
    process.topPairMuPlusJetsSelection.MCSampleTag = cms.string( 'Summer12' )

if options.applyZselection:
    #apply to filters in tagging mode (for monitoring)
    process.topPairEPlusJetsSelection.tagAndProbeStudies = cms.bool( True )
    process.topPairMuPlusJetsSelection.tagAndProbeStudies = cms.bool( True )
    #apply to actual BLT filters
    process.topPairEPlusJetsSelectionApply.tagAndProbeStudies = cms.bool( True )
    process.topPairMuPlusJetsSelectionApply.tagAndProbeStudies = cms.bool( True )

if options.dropTriggerSelection:
    #apply to filters in tagging mode (for monitoring)
    process.topPairEPlusJetsSelection.dropTriggerSelection = cms.bool( True )
    process.topPairMuPlusJetsSelection.dropTriggerSelection = cms.bool( True )
    #apply to actual BLT filters
    process.topPairEPlusJetsSelectionApply.dropTriggerSelection = cms.bool( True )
    process.topPairMuPlusJetsSelectionApply.dropTriggerSelection = cms.bool( True )

if options.bSelectionInTaggingMode:
    #apply to filters in tagging mode (for monitoring)
    process.topPairEPlusJetsSelection.bSelectionInTaggingMode = cms.bool( True )
    process.topPairMuPlusJetsSelection.bSelectionInTaggingMode = cms.bool( True )
    #apply to actual BLT filters
    process.topPairEPlusJetsSelectionApply.bSelectionInTaggingMode = cms.bool( True )
    process.topPairMuPlusJetsSelectionApply.bSelectionInTaggingMode = cms.bool( True )

electronselectionPrefix = 'TopPairElectronPlusJetsSelection.'
muonselectionPrefix = 'TopPairMuonPlusJetsSelection.'
process.topPairEPlusJetsSelection.prefix = cms.untracked.string( electronselectionPrefix )
process.topPairMuPlusJetsSelection.prefix = cms.untracked.string( muonselectionPrefix )

process.load( "TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff" )

process.MCFiltersInTaggingMode = cms.Sequence( process.makeGenEvt * 
                                                     process.ttFullHadronicFilter * 
                                                     process.ttFullLeptonicFilter * 
                                                     process.ttSemiLeptonicElectronFilter * 
                                                     process.ttSemiLeptonicMuonFilter * 
                                                     process.ttSemiLeptonicTauFilter * 
                                                     process.ttFullLeptonicEEFilter * 
                                                     process.ttFullLeptonicMuMuFilter * 
                                                     process.ttFullLeptonicTauTauFilter * 
                                                     process.ttFullLeptonicETauFilter * 
                                                     process.ttFullLeptonicEMuFilter * 
                                                     process.ttFullLeptonicMuTauFilter )

process.eventFiltersIntaggingMode = cms.Sequence( process.MCFiltersInTaggingMode )

##########################################################################################
#            Selection Config
##########################################################################################
process.load( 'BristolAnalysis.NTupleTools.SelectionAnalyser_cfi' )

# Common things you want to run on all events
process.commonSequence = cms.Sequence(
                      process.pdfWeights * 
                      process.hlTrigReport * 
                      process.egammaIDLikelihood * 
                      process.pfMEtSysShiftCorrSequence * 
                      process.patseq * 
                      process.EventFilters * 
                      getattr( process, "producePatPFMETCorrections" + postfix ) * 
                      getattr( process, "patMETs" + postfix ) * 
                      process.eventFiltersIntaggingMode *
                      process.eventWeightPU *
                      process.ttbarDecayAnalyser
                      )

#===============================================================================
# Electron channel
#===============================================================================

# Copy ntuple config so we can change some of the inputs
# And also have different input collections for the two channels
process.rootNTuplesEPlusJets = copy.copy( process.rootNTuples )
process.rootTupleTreeEPlusJets = process.rootTupleTree.clone( treeName='ePlusJetsTree' )
process.rootTupleTreeEPlusJets.outputCommands.append('keep *_rootTupleGlobalEventVarsEPlusJets_*_*')
process.rootTupleTreeEPlusJets.outputCommands.append('keep *_rootTuplePF2PATJetsEPlusJets_*_*')
process.rootTupleTreeEPlusJets.outputCommands.append('drop *_rootTupleVertex_*_*')
process.rootTupleTreeEPlusJets.outputCommands.append('drop *_nTuplePFMuons_*_*')
process.rootTupleTreeEPlusJets.outputCommands.append('drop *_rootTuplePFElectrons_*_*')
process.rootNTuplesEPlusJets.remove( process.rootTupleTree )
# Add global event variables to ntuple
process.rootTupleGlobalEventVarsEPlusJets = process.rootTupleGlobalEventVars.clone( 
                                                                                   signalLeptonInputTag=cms.InputTag('topPairEPlusJetsSelection', 'TopPairElectronPlusJetsSelection.signalElectron'), 
                                                                                   Channel='EPlusJets', 
                                                                                   metInputTag=cms.InputTag('patMETsPFlow'),
                                                                                   Prefix='Event.',
                                                                                   signalLeptonIndexInputTag=cms.InputTag('topPairEPlusJetsSelection', 'TopPairElectronPlusJetsSelection.signalElectronIndex'),
                                                                                   Suffix='.patMETsPFlow',
                                                                                   )
process.rootTupleGlobalEventVarsEPlusJetsPatType1CorrectedPFMet = process.rootTupleGlobalEventVars.clone( 
                                                                                   signalLeptonInputTag=cms.InputTag('topPairEPlusJetsSelection', 'TopPairElectronPlusJetsSelection.signalElectron'), 
                                                                                   metInputTag=cms.InputTag('patType1CorrectedPFMet'),
                                                                                   Channel='EPlusJets', 
                                                                                   Prefix='Event.',
                                                                                   signalLeptonIndexInputTag=cms.InputTag('topPairEPlusJetsSelection', 'TopPairElectronPlusJetsSelection.signalElectronIndex'),
                                                                                   Suffix='.patType1CorrectedPFMet',
                                                                                   )
process.rootNTuplesEPlusJets *= process.rootTupleGlobalEventVarsEPlusJets
process.rootNTuplesEPlusJets *= process.rootTupleGlobalEventVarsEPlusJetsPatType1CorrectedPFMet
process.rootNTuplesEPlusJets *= process.rootTupleTreeEPlusJets

# Use the jet collection produced by the selection filter in tagging mode for calculation of HT etc.
process.rootTupleGlobalEventVarsEPlusJets.jetInputTag = cms.InputTag("topPairEPlusJetsSelection", 'TopPairElectronPlusJetsSelection.cleanedJets')
# Use signal electrons for ST etc,
process.rootTupleGlobalEventVarsEPlusJets.signalLeptonIndexInputTag = cms.InputTag("topPairEPlusJetsSelection", 'TopPairElectronPlusJetsSelection.signalElectron')
process.rootTupleGlobalEventVarsEPlusJets.signalLeptonIndexInputTag = cms.InputTag('topPairEPlusJetsSelection', 'TopPairElectronPlusJetsSelection.signalElectronIndex')

# Same for global variables calculated with other MET
process.rootTupleGlobalEventVarsEPlusJetsPatType1CorrectedPFMet.jetInputTag = cms.InputTag("topPairEPlusJetsSelection", 'TopPairElectronPlusJetsSelection.cleanedJets')
process.rootTupleGlobalEventVarsEPlusJetsPatType1CorrectedPFMet.signalLeptonIndexInputTag = cms.InputTag("topPairEPlusJetsSelection", 'TopPairElectronPlusJetsSelection.signalElectron')
process.rootTupleGlobalEventVarsEPlusJetsPatType1CorrectedPFMet.signalLeptonIndexInputTag = cms.InputTag('topPairEPlusJetsSelection', 'TopPairElectronPlusJetsSelection.signalElectronIndex')

# Replace jet collection that ends up in ntuple to cleaned collection
process.rootTuplePF2PATJetsEPlusJets = process.rootTuplePF2PATJets.clone( 
                                                                         InputTag=cms.InputTag("topPairEPlusJetsSelection", 'TopPairElectronPlusJetsSelection.cleanedJets'), 
                                                                         Prefix='cleanedJetsPFlowEPlusJets.' )
process.rootNTuplesEPlusJets.replace( process.rootTuplePF2PATJets, process.rootTuplePF2PATJetsEPlusJets )

# Run selection twice.  First time in tagging mode so we can run the selection analyser
# and get meaningful results.
# Then run selection and reject events
process.ePlusJetsSelection = cms.Path( 
                      process.commonSequence *
                      process.topPairEPlusJetsSelection *
                      process.topPairEPlusJetsSelectionAnalyser *
                      process.topPairEPlusJetsSelectionApply *
                      process.rootNTuplesEPlusJets
                      )

# Electron QCD control regions
# Non isolated
process.rootNTuplesEPlusJetsNonIsolated = copy.copy( process.rootNTuples )
process.rootTupleTreeEPlusJetsNonIsolated = process.rootTupleTree.clone( treeName='ePlusJetsNonIsolatedTree' )
process.rootTupleTreeEPlusJetsNonIsolated.outputCommands.append('keep *_rootTupleGlobalEventVarsEPlusJetsNonIsolated_*_*')
process.rootTupleTreeEPlusJetsNonIsolated.outputCommands.append('keep *_rootTuplePF2PATJetsEPlusJetsNonIsolated_*_*')
process.rootTupleTreeEPlusJetsNonIsolated.outputCommands.append('drop *_rootTupleVertex_*_*')
process.rootTupleTreeEPlusJetsNonIsolated.outputCommands.append('drop *_nTuplePFMuons_*_*')
process.rootTupleTreeEPlusJetsNonIsolated.outputCommands.append('drop *_rootTuplePFElectrons_*_*')
process.rootNTuplesEPlusJetsNonIsolated.remove( process.rootTupleTree )
process.rootTupleGlobalEventVarsEPlusJetsNonIsolated = process.rootTupleGlobalEventVars.clone( 
                                                                                   signalLeptonInputTag=cms.InputTag('topPairEPlusJetsNonIsolatedSelection', 'TopPairElectronPlusJetsSelection.signalElectron'), 
                                                                                   Channel='EPlusJets', 
                                                                                   metInputTag=cms.InputTag('patMETsPFlow'),
                                                                                   Prefix='Event.',
                                                                                   signalLeptonIndexInputTag=cms.InputTag('topPairEPlusJetsNonIsolatedSelection', 'TopPairElectronPlusJetsSelection.signalElectronIndex'),
                                                                                   Suffix='.patMETsPFlow.nonIsolated',
                                                                                   )
process.rootTupleGlobalEventVarsEPlusJetsPatType1CorrectedPFMetNonIsolated = process.rootTupleGlobalEventVars.clone( 
                                                                                   signalLeptonInputTag=cms.InputTag('topPairEPlusJetsNonIsolatedSelection', 'TopPairElectronPlusJetsSelection.signalElectron'), 
                                                                                   metInputTag=cms.InputTag('patType1CorrectedPFMet'),
                                                                                   Channel='EPlusJets', 
                                                                                   Prefix='Event.',
                                                                                   signalLeptonIndexInputTag=cms.InputTag('topPairEPlusJetsNonIsolatedSelection', 'TopPairElectronPlusJetsSelection.signalElectronIndex'),
                                                                                   Suffix='.patType1CorrectedPFMet.nonIsolated',
                                                                                   )
process.rootNTuplesEPlusJetsNonIsolated *= process.rootTupleGlobalEventVarsEPlusJetsNonIsolated
process.rootNTuplesEPlusJetsNonIsolated *= process.rootTupleGlobalEventVarsEPlusJetsPatType1CorrectedPFMetNonIsolated
process.rootNTuplesEPlusJetsNonIsolated *= process.rootTupleTreeEPlusJetsNonIsolated
process.rootTupleGlobalEventVarsEPlusJetsNonIsolated.jetInputTag = cms.InputTag("topPairEPlusJetsNonIsolatedSelection", 'TopPairElectronPlusJetsSelection.cleanedJets')
process.rootTupleGlobalEventVarsEPlusJetsNonIsolated.signalLeptonIndexInputTag = cms.InputTag("topPairEPlusJetsNonIsolatedSelection", 'TopPairElectronPlusJetsSelection.signalElectron')
process.rootTupleGlobalEventVarsEPlusJetsNonIsolated.signalLeptonIndexInputTag = cms.InputTag('topPairEPlusJetsNonIsolatedSelection', 'TopPairElectronPlusJetsSelection.signalElectronIndex')
process.rootTupleGlobalEventVarsEPlusJetsPatType1CorrectedPFMetNonIsolated.jetInputTag = cms.InputTag("topPairEPlusJetsNonIsolatedSelection", 'TopPairElectronPlusJetsSelection.cleanedJets')
process.rootTupleGlobalEventVarsEPlusJetsPatType1CorrectedPFMetNonIsolated.signalLeptonIndexInputTag = cms.InputTag("topPairEPlusJetsNonIsolatedSelection", 'TopPairElectronPlusJetsSelection.signalElectron')
process.rootTupleGlobalEventVarsEPlusJetsPatType1CorrectedPFMetNonIsolated.signalLeptonIndexInputTag = cms.InputTag('topPairEPlusJetsNonIsolatedSelection', 'TopPairElectronPlusJetsSelection.signalElectronIndex')
process.rootTuplePF2PATJetsEPlusJetsNonIsolated = process.rootTuplePF2PATJets.clone( 
                                                                         InputTag=cms.InputTag("topPairEPlusJetsNonIsolatedSelection", 'TopPairElectronPlusJetsSelection.cleanedJets'), 
                                                                         Prefix='cleanedJetsPFlowEPlusJets.nonIsolated' )
process.rootNTuplesEPlusJetsNonIsolated.replace( process.rootTuplePF2PATJets, process.rootTuplePF2PATJetsEPlusJetsNonIsolated )

process.ePlusJetsNonIsolatedSelection = cms.Path( 
                      process.commonSequence *
                      process.topPairEPlusJetsNonIsolatedSelection *
                      process.rootNTuplesEPlusJetsNonIsolated
                      )

# Inverted Conversions
process.rootNTuplesEPlusJetsInvertedConversion = copy.copy( process.rootNTuples )
process.rootTupleTreeEPlusJetsInvertedConversion = process.rootTupleTree.clone( treeName='ePlusJetsInvertedConversionTree' )
process.rootTupleTreeEPlusJetsInvertedConversion.outputCommands.append('keep *_rootTupleGlobalEventVarsEPlusJetsInvertedConversion_*_*')
process.rootTupleTreeEPlusJetsInvertedConversion.outputCommands.append('keep *_rootTuplePF2PATJetsEPlusJetsInvertedConversion_*_*')
process.rootTupleTreeEPlusJetsInvertedConversion.outputCommands.append('drop *_rootTupleVertex_*_*')
process.rootTupleTreeEPlusJetsInvertedConversion.outputCommands.append('drop *_nTuplePFMuons_*_*')
process.rootTupleTreeEPlusJetsInvertedConversion.outputCommands.append('drop *_rootTuplePFElectrons_*_*')
process.rootNTuplesEPlusJetsInvertedConversion.remove( process.rootTupleTree )
process.rootTupleGlobalEventVarsEPlusJetsInvertedConversion = process.rootTupleGlobalEventVars.clone( 
                                                                                   signalLeptonInputTag=cms.InputTag('topPairEPlusJetsInvertedConversionSelection', 'TopPairElectronPlusJetsSelection.signalElectron'), 
                                                                                   Channel='EPlusJets', 
                                                                                   metInputTag=cms.InputTag('patMETsPFlow'),
                                                                                   Prefix='Event.',
                                                                                   signalLeptonIndexInputTag=cms.InputTag('topPairEPlusJetsInvertedConversionSelection', 'TopPairElectronPlusJetsSelection.signalElectronIndex'),
                                                                                   Suffix='.patMETsPFlow.InvertedConversion',
                                                                                   )
process.rootTupleGlobalEventVarsEPlusJetsPatType1CorrectedPFMetInvertedConversion = process.rootTupleGlobalEventVars.clone( 
                                                                                   signalLeptonInputTag=cms.InputTag('topPairEPlusJetsInvertedConversionSelection', 'TopPairElectronPlusJetsSelection.signalElectron'), 
                                                                                   metInputTag=cms.InputTag('patType1CorrectedPFMet'),
                                                                                   Channel='EPlusJets', 
                                                                                   Prefix='Event.',
                                                                                   signalLeptonIndexInputTag=cms.InputTag('topPairEPlusJetsInvertedConversionSelection', 'TopPairElectronPlusJetsSelection.signalElectronIndex'),
                                                                                   Suffix='.patType1CorrectedPFMet.InvertedConversion',
                                                                                   )
process.rootNTuplesEPlusJetsInvertedConversion *= process.rootTupleGlobalEventVarsEPlusJetsInvertedConversion
process.rootNTuplesEPlusJetsInvertedConversion *= process.rootTupleGlobalEventVarsEPlusJetsPatType1CorrectedPFMetInvertedConversion
process.rootNTuplesEPlusJetsInvertedConversion *= process.rootTupleTreeEPlusJetsInvertedConversion
process.rootTupleGlobalEventVarsEPlusJetsInvertedConversion.jetInputTag = cms.InputTag("topPairEPlusJetsInvertedConversionSelection", 'TopPairElectronPlusJetsSelection.cleanedJets')
process.rootTupleGlobalEventVarsEPlusJetsInvertedConversion.signalLeptonIndexInputTag = cms.InputTag("topPairEPlusJetsInvertedConversionSelection", 'TopPairElectronPlusJetsSelection.signalElectron')
process.rootTupleGlobalEventVarsEPlusJetsInvertedConversion.signalLeptonIndexInputTag = cms.InputTag('topPairEPlusJetsInvertedConversionSelection', 'TopPairElectronPlusJetsSelection.signalElectronIndex')
process.rootTupleGlobalEventVarsEPlusJetsPatType1CorrectedPFMetInvertedConversion.jetInputTag = cms.InputTag("topPairEPlusJetsInvertedConversionSelection", 'TopPairElectronPlusJetsSelection.cleanedJets')
process.rootTupleGlobalEventVarsEPlusJetsPatType1CorrectedPFMetInvertedConversion.signalLeptonIndexInputTag = cms.InputTag("topPairEPlusJetsInvertedConversionSelection", 'TopPairElectronPlusJetsSelection.signalElectron')
process.rootTupleGlobalEventVarsEPlusJetsPatType1CorrectedPFMetInvertedConversion.signalLeptonIndexInputTag = cms.InputTag('topPairEPlusJetsInvertedConversionSelection', 'TopPairElectronPlusJetsSelection.signalElectronIndex')
process.rootTuplePF2PATJetsEPlusJetsInvertedConversion = process.rootTuplePF2PATJets.clone( 
                                                                         InputTag=cms.InputTag("topPairEPlusJetsInvertedConversionSelection", 'TopPairElectronPlusJetsSelection.cleanedJets'), 
                                                                         Prefix='cleanedJetsPFlowEPlusJets.InvertedConversion' )
process.rootNTuplesEPlusJetsInvertedConversion.replace( process.rootTuplePF2PATJets, process.rootTuplePF2PATJetsEPlusJetsInvertedConversion )

process.ePlusJetsInvertedConversionSelection = cms.Path( 
                      process.commonSequence *
                      process.topPairEPlusJetsInvertedConversionSelection *
                      process.rootNTuplesEPlusJetsInvertedConversion
                      )

#===============================================================================
# Muon channel
#===============================================================================
# Same as above
process.rootNTuplesMuPlusJets = copy.copy( process.rootNTuples )
process.rootTupleTreeMuPlusJets = process.rootTupleTree.clone( treeName='muPlusJetsTree' )
process.rootTupleTreeMuPlusJets.outputCommands.append('keep *_rootTupleGlobalEventVarsMuPlusJets_*_*')
process.rootTupleTreeMuPlusJets.outputCommands.append('keep *_rootTuplePF2PATJetsMuPlusJets_*_*')
process.rootTupleTreeMuPlusJets.outputCommands.append('drop *_rootTupleVertex_*_*')
process.rootTupleTreeMuPlusJets.outputCommands.append('drop *_nTuplePFMuons_*_*')
process.rootTupleTreeMuPlusJets.outputCommands.append('drop *_rootTuplePFElectrons_*_*')
process.rootNTuplesMuPlusJets.remove( process.rootTupleTree )
process.rootTupleGlobalEventVarsMuPlusJets = process.rootTupleGlobalEventVars.clone( 
                                                                                    signalLeptonInputTag=cms.InputTag('topPairMuPlusJetsSelection', 'TopPairMuonPlusJetsSelection.signalMuon'), 
                                                                                    Channel='MuPlusJets',
                                                                                    metInputTag=cms.InputTag('patMETsPFlow'),
                                                                                    Prefix='Event.',
                                                                                    signalLeptonIndexInputTag=cms.InputTag('topPairMuPlusJetsSelection', 'TopPairMuonPlusJetsSelection.signalMuonIndex'),
                                                                                    Suffix='.patMETsPFlow',
                                                                                    )
process.rootTupleGlobalEventVarsMuPlusJetsPatType1CorrectedPFMet = process.rootTupleGlobalEventVars.clone( 
                                                                                    signalLeptonInputTag=cms.InputTag('topPairMuPlusJetsSelection', 'TopPairMuonPlusJetsSelection.signalMuon'), 
                                                                                    Channel='MuPlusJets',
                                                                                    metInputTag=cms.InputTag('patType1CorrectedPFMet'),
                                                                                    Prefix='Event.',
                                                                                    signalLeptonIndexInputTag=cms.InputTag('topPairMuPlusJetsSelection', 'TopPairMuonPlusJetsSelection.signalMuonIndex'),
                                                                                    Suffix='.patType1CorrectedPFMet',
                                                                                    )
process.rootNTuplesMuPlusJets *= process.rootTupleGlobalEventVarsMuPlusJets
process.rootNTuplesMuPlusJets *= process.rootTupleGlobalEventVarsMuPlusJetsPatType1CorrectedPFMet
process.rootNTuplesMuPlusJets *= process.rootTupleTreeMuPlusJets
process.rootTupleGlobalEventVarsMuPlusJets.jetInputTag = cms.InputTag("topPairMuPlusJetsSelection", 'TopPairMuonPlusJetsSelection.cleanedJets')
process.rootTupleGlobalEventVarsMuPlusJets.signalLeptonInputTag = cms.InputTag("topPairMuPlusJetsSelection", 'TopPairMuonPlusJetsSelection.signalMuon')
process.rootTupleGlobalEventVarsMuPlusJets.signalLeptonIndexInputTag = cms.InputTag('topPairMuPlusJetsSelection', 'TopPairMuonPlusJetsSelection.signalMuonIndex')
process.rootTupleGlobalEventVarsMuPlusJetsPatType1CorrectedPFMet.jetInputTag = cms.InputTag("topPairMuPlusJetsSelection", 'TopPairMuonPlusJetsSelection.cleanedJets')
process.rootTupleGlobalEventVarsMuPlusJetsPatType1CorrectedPFMet.signalLeptonInputTag = cms.InputTag("topPairMuPlusJetsSelection", 'TopPairMuonPlusJetsSelection.signalMuon')
process.rootTupleGlobalEventVarsMuPlusJetsPatType1CorrectedPFMet.signalLeptonIndexInputTag = cms.InputTag('topPairMuPlusJetsSelection', 'TopPairMuonPlusJetsSelection.signalMuonIndex')

process.rootTuplePF2PATJetsMuPlusJets = process.rootTuplePF2PATJets.clone( 
                                                                          InputTag=cms.InputTag("topPairMuPlusJetsSelection", 'TopPairMuonPlusJetsSelection.cleanedJets'), 
                                                                          Prefix='cleanedJetsPFlowMuPlusJets.' )
process.rootNTuplesMuPlusJets.replace( process.rootTuplePF2PATJets, process.rootTuplePF2PATJetsMuPlusJets )

process.muPlusJetsSelection = cms.Path( 
                      process.commonSequence *
                      process.topPairMuPlusJetsSelection *
                      process.topPairMuPlusJetsSelectionAnalyser *
                      process.topPairMuPlusJetsSelectionApply *
                      process.rootNTuplesMuPlusJets
                      )

# Muon QCD control region
process.rootNTuplesMuPlusJetsNonIsolated = copy.copy( process.rootNTuples )
process.rootTupleTreeMuPlusJetsNonIsolated = process.rootTupleTree.clone( treeName='muPlusJetsNonIsolatedTree' )
process.rootTupleTreeMuPlusJetsNonIsolated.outputCommands.append('keep *_rootTupleGlobalEventVarsMuPlusJetsNonIsolated_*_*')
process.rootTupleTreeMuPlusJetsNonIsolated.outputCommands.append('keep *_rootTuplePF2PATJetsMuPlusJetsNonIsolated_*_*')
process.rootTupleTreeMuPlusJetsNonIsolated.outputCommands.append('drop *_rootTupleVertex_*_*')
process.rootTupleTreeMuPlusJetsNonIsolated.outputCommands.append('drop *_nTuplePFMuons_*_*')
process.rootTupleTreeMuPlusJetsNonIsolated.outputCommands.append('drop *_rootTuplePFElectrons_*_*')
process.rootNTuplesMuPlusJetsNonIsolated.remove( process.rootTupleTree )
process.rootTupleGlobalEventVarsMuPlusJetsNonIsolated = process.rootTupleGlobalEventVars.clone( 
                                                                                    signalLeptonInputTag=cms.InputTag('topPairMuPlusJetsNonIsolatedSelection', 'TopPairMuonPlusJetsSelection.signalMuon'), 
                                                                                    Channel='MuPlusJets',
                                                                                    metInputTag=cms.InputTag('patMETsPFlow'),
                                                                                    Prefix='Event.',
                                                                                    signalLeptonIndexInputTag=cms.InputTag('topPairMuPlusJetsNonIsolatedSelection', 'TopPairMuonPlusJetsSelection.signalMuonIndex'),
                                                                                    Suffix='.patMETsPFlow.nonIsolated',
                                                                                    )
process.rootTupleGlobalEventVarsMuPlusJetsPatType1CorrectedPFMetNonIsolated = process.rootTupleGlobalEventVars.clone( 
                                                                                    signalLeptonInputTag=cms.InputTag('NonIsolated', 'TopPairMuonPlusJetsSelection.signalMuon'), 
                                                                                    Channel='MuPlusJets',
                                                                                    metInputTag=cms.InputTag('patType1CorrectedPFMet'),
                                                                                    Prefix='Event.',
                                                                                    signalLeptonIndexInputTag=cms.InputTag('topPairMuPlusJetsNonIsolatedSelection', 'TopPairMuonPlusJetsSelection.signalMuonIndex'),
                                                                                    Suffix='.patType1CorrectedPFMet.nonIsolated',
                                                                                    )
process.rootNTuplesMuPlusJetsNonIsolated *= process.rootTupleGlobalEventVarsMuPlusJetsNonIsolated
process.rootNTuplesMuPlusJetsNonIsolated *= process.rootTupleGlobalEventVarsMuPlusJetsPatType1CorrectedPFMetNonIsolated
process.rootNTuplesMuPlusJetsNonIsolated *= process.rootTupleTreeMuPlusJetsNonIsolated
process.rootTupleGlobalEventVarsMuPlusJetsNonIsolated.jetInputTag = cms.InputTag("topPairMuPlusJetsNonIsolatedSelection", 'TopPairMuonPlusJetsSelection.cleanedJets')
process.rootTupleGlobalEventVarsMuPlusJetsNonIsolated.signalLeptonInputTag = cms.InputTag("topPairMuPlusJetsNonIsolatedSelection", 'TopPairMuonPlusJetsSelection.signalMuon')
process.rootTupleGlobalEventVarsMuPlusJetsNonIsolated.signalLeptonIndexInputTag = cms.InputTag('topPairMuPlusJetsNonIsolatedSelection', 'TopPairMuonPlusJetsSelection.signalMuonIndex')
process.rootTupleGlobalEventVarsMuPlusJetsPatType1CorrectedPFMetNonIsolated.jetInputTag = cms.InputTag("topPairMuPlusJetsNonIsolatedSelection", 'TopPairMuonPlusJetsSelection.cleanedJets')
process.rootTupleGlobalEventVarsMuPlusJetsPatType1CorrectedPFMetNonIsolated.signalLeptonInputTag = cms.InputTag("topPairMuPlusJetsNonIsolatedSelection", 'TopPairMuonPlusJetsSelection.signalMuon')
process.rootTupleGlobalEventVarsMuPlusJetsPatType1CorrectedPFMetNonIsolated.signalLeptonIndexInputTag = cms.InputTag('topPairMuPlusJetsNonIsolatedSelection', 'TopPairMuonPlusJetsSelection.signalMuonIndex')
process.rootTuplePF2PATJetsMuPlusJetsNonIsolated = process.rootTuplePF2PATJets.clone( 
                                                                          InputTag=cms.InputTag("topPairMuPlusJetsNonIsolatedSelection", 'TopPairMuonPlusJetsSelection.cleanedJets'), 
                                                                          Prefix='cleanedJetsPFlowMuPlusJets.nonIsolated.')
process.rootNTuplesMuPlusJetsNonIsolated.replace( process.rootTuplePF2PATJets, process.rootTuplePF2PATJetsMuPlusJetsNonIsolated )

process.muPlusJetsNonIsolatedSelection = cms.Path( 
                      process.commonSequence *
                      process.topPairMuPlusJetsNonIsolatedSelection *
                      process.rootNTuplesMuPlusJetsNonIsolated
                      )

if options.useData or not options.isTTbarMC:
    process.eventFiltersIntaggingMode.remove( process.MCFiltersInTaggingMode )
    
if options.useData or not options.isTTbarMC:
    process.commonSequence.remove( process.ttbarDecayAnalyser )

if not options.setupMETmanually:
    process.commonSequence.remove( getattr( process, "producePatPFMETCorrections" + postfix ) )
    process.commonSequence.remove( getattr( process, "patMETs" + postfix ) )

if not options.printEventContent:
    process.commonSequence.remove(process.printEventContent)
    
if options.useData or not options.storePDFWeights:
        process.commonSequence.remove(process.pdfWeights)

if options.bSelectionInTaggingMode:
    process.topPairEPlusJetsSelectionApply.bSelectionInTaggingMode =  bSelectionInTaggingMode=cms.bool(True)
    process.topPairMuPlusJetsSelectionApply.bSelectionInTaggingMode =  bSelectionInTaggingMode=cms.bool(True)
    process.rootTupleTreeMuPlusJets.treeName='muPlusJetsTree_noBTag'
    process.rootTupleTreeEPlusJets.treeName='ePlusJetsTree_noBTag'
    pass
   
# Keep pu weights for data, so 
# if options.useData:
#     process.commonSequence.remove(process.eventWeightPU) 