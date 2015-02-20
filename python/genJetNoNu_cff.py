def setupGenJetNoNu( process, cms ):
	process.load('RecoJets.Configuration.GenJetParticles_cff')
	process.genParticlesForJetsNoNu.src = cms.InputTag('packedGenParticles')
	process.load('RecoJets.Configuration.RecoGenJets_cff')
	process.load('PhysicsTools.PatAlgos.slimming.slimmedGenJets_cfi')
	# process.slimmedGenJetsNoNu = process.slimmedGenJets.clone( src = cms.InputTag('ak4GenJetsNoNu','','Ntuples'), packedGenParticles = cms.InputTag('packedGenParticles','','PAT') )

	process.genJetsNoNuSequence = cms.Sequence(
	    process.genParticlesForJetsNoNu +
	    process.ak4GenJetsNoNu #+
	    # process.slimmedGenJetsNoNu
	    )