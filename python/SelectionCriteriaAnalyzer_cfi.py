import FWCore.ParameterSet.Config as cms

selectionCriteriaAnalyzer = cms.EDFilter('SelectionCriteriaAnalyzer',
    # Specify input collections
    offlineSelectionCriteriaInput      = cms.VInputTag(
                                     cms.InputTag('topPairMuPlusJetsSelectionTagging', 'TopPairMuonPlusJetsSelection.FullSelection', 'Ntuples'),
                                     cms.InputTag('topPairEPlusJetsSelectionTagging', 'TopPairElectronPlusJetsSelection.FullSelection', 'Ntuples'),
                                     cms.InputTag('topPairMuPlusJetsQCDSelectionTagging2', 'TopPairMuonPlusJetsQCDSelection1p5to3.FullSelection', 'Ntuples'),
                                     cms.InputTag('topPairMuPlusJetsQCDSelectionTagging1', 'TopPairMuonPlusJetsQCDSelection3toInf.FullSelection', 'Ntuples'),  
                                     cms.InputTag('topPairEPlusJetsQCDSelectionTagging', 'TopPairElectronPlusJetsQCDSelection.FullSelection', 'Ntuples'),
                                     cms.InputTag('topPairEPlusJetsConversionSelectionTagging', 'TopPairElectronPlusJetsConversionSelection.FullSelection', 'Ntuples'),
            ),
    genSelectionCriteriaInput      = cms.VInputTag(
									# cms.InputTag('ttFullHadronicFilter',       	 '', 'Ntuples'),
									# cms.InputTag('ttFullLeptonicEEFilter',     	 '', 'Ntuples'),
									# cms.InputTag('ttFullLeptonicEMuFilter',    	 '', 'Ntuples'),
									# cms.InputTag('ttFullLeptonicETauFilter',     '', 'Ntuples'),
									# cms.InputTag('ttFullLeptonicFilter',       	 '', 'Ntuples'),
									# cms.InputTag('ttFullLeptonicMuMuFilter',     '', 'Ntuples'),
									# cms.InputTag('ttFullLeptonicMuTauFilter',    '', 'Ntuples'),
									# cms.InputTag('ttFullLeptonicTauTauFilter',   '', 'Ntuples'),
									# cms.InputTag('ttSemiLeptonicTauFilter',    	 '', 'Ntuples'),
									# Only interested in these two decay channels for filtering events
									cms.InputTag('ttSemiLeptonicElectronFilter', '', 'Ntuples'),
									cms.InputTag('ttSemiLeptonicMuonFilter',     '', 'Ntuples'),

            ),
)



