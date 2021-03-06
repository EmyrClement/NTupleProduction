def setupTTGenEvent( process, cms ):
	process.load( "TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff" )
	process.initSubset.src = cms.InputTag('prunedGenParticles')
	process.decaySubset.src = cms.InputTag('prunedGenParticles')
	process.decaySubset.runMode = cms.string('Run2')

	process.load( 'TopQuarkAnalysis.TopSkimming.TtFullyHadronicFilter_cfi' )
	process.load( 'TopQuarkAnalysis.TopSkimming.TtFullyLeptonicFilter_cfi' )
	process.load( 'TopQuarkAnalysis.TopSkimming.TtSemiLeptonicFilter_cfi' )

	filters = [
	process.ttFullHadronicFilter,
	process.ttFullLeptonicFilter,
	process.ttSemiLeptonicElectronFilter,
	process.ttSemiLeptonicMuonFilter,
	process.ttSemiLeptonicTauFilter,
	process.ttFullLeptonicEEFilter,
	process.ttFullLeptonicMuMuFilter,
	process.ttFullLeptonicTauTauFilter,
	process.ttFullLeptonicETauFilter,
	process.ttFullLeptonicEMuFilter,
	process.ttFullLeptonicMuTauFilter,
	]


	for filter in filters:
		filter.taggingMode = cms.bool(True)
		filter.src = cms.InputTag("genEvt")
		filter.useTtGenEvent = cms.bool(True)

	process.ttGenEvent = cms.Sequence( process.makeGenEvt *
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
										process.ttFullLeptonicMuTauFilter
										)
