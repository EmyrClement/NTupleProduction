import FWCore.ParameterSet.Config as cms
from BristolAnalysis.NTupleTools.BristolNTuple_PFCandidates_cfi import nTuplePFCands
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

njettiness = Njettiness.clone(
    src = cms.InputTag('nTuplePFCands', 'OneJet'),
	measureDefinition = cms.uint32(1),
)

# addNJettiness = cms.Sequence( nTuplePFCands * njettiness )

addNJettiness = cms.Sequence( njettiness  )
