from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'Tbar_tw_PU20bx25'
config.General.workArea = 'workdirCrab'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'BristolAnalysis/NTupleTools/Configuration/makeTuplesFromMiniAOD_cfg.py'

config.section_("Data")
config.Data.inputDataset = '/Tbar_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.outLFN = '/store/user/ejclemen/'
config.Data.publication = True
config.Data.publishDataName = 'Tbar_tw_PU20bx25'

config.section_("Site")
config.Site.storageSite = 'T2_UK_SGrid_Bristol'
