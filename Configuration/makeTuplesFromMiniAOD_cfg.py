import FWCore.ParameterSet.Config as cms

process = cms.Process("Ntuples")

## Source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:/afs/cern.ch/work/e/ejclemen/004C6DA7-FB03-E411-96BD-0025905A497A.root')
)

## Maximum Number of Events
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )


process.load('BristolAnalysis.NTupleTools.Ntuple_cff')
process.nTupleMuons.InputTag = cms.InputTag('slimmedMuons')
process.nTupleMuons.Prefix = cms.string('Muons.')
process.rootTupleElectrons.InputTag = cms.InputTag('slimmedElectrons')
process.rootTupleElectrons.Prefix = cms.string('Electrons.')

process.rootTupleTree = cms.EDAnalyzer("RootTupleMakerV2_Tree",
        treeName = cms.string('tree'),
        outputCommands=cms.untracked.vstring(
           'drop *',
            # muons
            'keep *_nTupleMuons_*_*',
            # electrons
            'keep *_nTupleElectrons_*_*',
        )
    )

process.rootNTuples = cms.Sequence(
        # muons
        process.nTupleMuons +
        # electrons
        # process.rootTupleElectrons +
        # Make ntuple
        process.rootTupleTree)

process.makingNTuples = cms.Path(
						process.rootNTuples
                      )

process.TFileService = cms.Service("TFileService",
                           fileName=cms.string('ntuple.root')
                           )
