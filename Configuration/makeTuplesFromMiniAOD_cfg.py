import FWCore.ParameterSet.Config as cms

process = cms.Process("Ntuples")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('PLS170_V7AN2::All')

## Source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:/home/ec6821/CMSSW_7_0_9_patch3/src/004C6DA7-FB03-E411-96BD-0025905A497A.root')
)

## Maximum Number of Events
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

from BristolAnalysis.NTupleTools.NTupler_cff import *
setup_ntupler(process, cms )

process.makingNTuples = cms.Path(
						process.nTuples
                      )

process.TFileService = cms.Service("TFileService",
                           fileName=cms.string('ntuple.root')
                           )
