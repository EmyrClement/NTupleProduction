import FWCore.ParameterSet.Config as cms

process = cms.Process("Ntuples")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('PLS170_V7AN2::All')

## Source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:/home/ec6821/CMSSW_7_2_2/src/06843FC5-8370-E411-9B8C-0025905A60AA.root')
)

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

# Get options from command line
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('python')
from BristolAnalysis.NTupleTools.NTupleOptions_cff import *
getOptions( options )

# TT Gen Event configuration
from BristolAnalysis.NTupleTools.ttGenConfig_cff import *
setupTTGenEvent( process, cms )

# Hit fit
from BristolAnalysis.NTupleTools.hitFit_cff import *
setupHitFit( process, cms )

# Load the selection filters and the selection analyzers
process.load( 'BristolAnalysis.NTupleTools.muonSelection_cff')
process.load( 'BristolAnalysis.NTupleTools.electronSelection_cff')

if options.tagAndProbe:
  process.topPairEPlusJetsSelection.tagAndProbeStudies = cms.bool( True )
  process.topPairEPlusJetsSelectionTagging.tagAndProbeStudies = cms.bool( True )
  process.topPairEPlusJetsSelection.jetSelectionInTaggingMode = cms.bool( True )
  process.topPairEPlusJetsSelectionTagging.jetSelectionInTaggingMode = cms.bool( True )
  
## Maximum Number of Events
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(5000) )

from BristolAnalysis.NTupleTools.NTupler_cff import *
setup_ntupler(process, cms )

process.makingNTuplesMuons = cms.Path(
            			# Run selection analyzer sequence
            			# Applies selection in tagging mode and makes cut flow plots
			            process.muonSelectionAnalyzerSequence *
			            # Actually apply the selection
            			process.topPairMuPlusJetsSelection *

                  # Produce TTGen event and store info
                  process.ttGenEvent *
            		  
                  # Produce ntuples from events that survive the selection
      						process.muonNTuples
                      )

process.makingNTuplesElectrons = cms.Path(
                  # Run selection analyzer sequence
                  # Applies selection in tagging mode and makes cut flow plots
                  process.electronSelectionAnalyzerSequence *
                  # Actually apply the selection
                  process.topPairEPlusJetsSelection *

                  # Produce TTGen event and store info 
                  process.ttGenEvent *

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


