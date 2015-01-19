from WMCore.Configuration import Configuration
from BristolAnalysis.NTupleTools.Configuration.BLT_unfold import input_files
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'TT_8TeV_mcatnlo_BLTUnfold_NoSkim'
config.General.transferLogs = True
config.section_('JobType')
config.JobType.psetName = 'BristolAnalysis/NTupleTools/test/unfoldingBLT_cfg.py'
config.JobType.pluginName = 'Analysis'
config.JobType.inputFiles = input_files

config.JobType.pyCfgParams = ['useData=0', 'dataType=TTJets-mcatnlo', 'isTTbarMC=1', 'skim=NoSkim', 'CMSSW=53X', 'centreOfMassEnergy=8', 'storePDFWeights=0', 'applyType0METcorrection=1', 'applySysShiftCorrection=1', 'isMCatNLO=1']
config.section_('Data')
config.Data.inputDataset = '/TT_8TeV-mcatnlo/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'
config.Data.unitsPerJob = 3
config.Data.splitting = 'FileBased'
config.section_('User')
config.section_('Site')
config.Site.storageSite = 'T2_UK_SGrid_Bristol'
