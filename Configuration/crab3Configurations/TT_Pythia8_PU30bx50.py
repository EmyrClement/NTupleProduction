from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'TT_Pythia8_PU30bx50'
config.General.workArea = 'workdirCrab/v1/2015-01-09'
config.General.transferOutputs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'BristolAnalysis/NTupleTools/Configuration/makeTuplesFromMiniAOD_cfg.py'
config.JobType.pyCfgParams = ['isTTbarMC=1']

config.section_("Data")
config.Data.inputDataset = '/TT_Tune4C_13TeV-pythia8-tauola/Phys14DR-AVE30BX50_tsg_PHYS14_ST_V1-v1/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.outLFN = '/store/user/ejclemen/'
config.Data.publication = True
config.Data.publishDataName = 'TT_Pythia8_PU30bx50'

config.section_("Site")
config.Site.storageSite = 'T2_UK_SGrid_Bristol'