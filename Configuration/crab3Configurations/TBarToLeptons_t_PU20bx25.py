from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'TBarToLeptons_t_PU20bx25'
config.General.workArea = 'workdirCrab/v1/2015-01-09'
config.General.transferOutputs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'BristolAnalysis/NTupleTools/Configuration/makeTuplesFromMiniAOD_cfg.py'

config.section_("Data")
config.Data.inputDataset = '/TBarToLeptons_t-channel_Tune4C_CSA14_13TeV-aMCatNLO-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.outLFN = '/store/user/ejclemen/'
config.Data.publication = True
config.Data.publishDataName = 'TBarToLeptons_t_PU20bx25'

config.section_("Site")
config.Site.storageSite = 'T2_UK_SGrid_Bristol'