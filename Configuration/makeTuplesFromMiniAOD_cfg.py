import FWCore.ParameterSet.Config as cms

process = cms.Process("Ntuples")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('PLS170_V7AN2::All')

## Source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:/home/ec6821/CMSSW_7_0_9_patch3/src/004C6DA7-FB03-E411-96BD-0025905A497A.root')
)

# Load the selection filters and the selection analyzers
# process.load( 'BristolAnalysis.NTupleTools.SelectionAnalyser_cfi' )
# process.load( 'BristolAnalysis.NTupleTools.TopPairMuonPlusJetsSelectionFilter_cfi' )
process.load( 'BristolAnalysis.NTupleTools.muonSelection_cff')
process.load( 'BristolAnalysis.NTupleTools.electronSelection_cff')

# process.load( 'TopQuarkAnalysis.TopKinFitter.TtSemiLepKinFitProducer_Electrons_cfi' )
# process.kinFitTtSemiLepEvent.jets = cms.InputTag('slimmedJets')
# process.kinFitTtSemiLepEvent.leps = cms.InputTag('slimmedElectrons')
# process.kinFitTtSemiLepEvent.mets = cms.InputTag('slimmedMETs')
# process.load( 'TopQuarkAnalysis.TopKinFitter.TtSemiLepKinFitProducer_Muons_cfi' )

## Maximum Number of Events
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10000) )

from BristolAnalysis.NTupleTools.NTupler_cff import *
setup_ntupler(process, cms )

process.makingNTuplesMuons = cms.Path(
            			# Run selection analyzer sequence
            			# Applies selection in tagging mode and makes cut flow plots
			            process.muonSelectionAnalyzerSequence *
			            # Actually apply the selection
            			process.topPairMuPlusJetsSelection *
            			# Produce ntuples from events that survive the selection
      						process.muonNTuples
                      )

process.makingNTuplesElectrons = cms.Path(
                  # Run selection analyzer sequence
                  # Applies selection in tagging mode and makes cut flow plots
                  process.electronSelectionAnalyzerSequence *
                  # Actually apply the selection
                  process.topPairEPlusJetsSelection *
                  # Produce ntuples from events that survive the selection
                  process.electronNTuples
                  )

process.TFileService = cms.Service("TFileService",
                           fileName=cms.string('ntuple.root')
                           )

# process.out = cms.OutputModule("PoolOutputModule",
#                 fileName = cms.untracked.string("testOutput.root")
#         )

# process.outpath = cms.EndPath(process.out)


