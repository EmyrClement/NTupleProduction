from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'DYJetsToLL_M50_PU20bx25'
config.General.workArea = 'workdirCrab/v1/2014-12-31'
config.General.transferOutputs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'BristolAnalysis/NTupleTools/Configuration/makeTuplesFromMiniAOD_cfg.py'

config.section_("Data")
config.Data.inputDataset = '/DYJetsToLL_M-50_13TeV-madgraph-pythia8/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.outLFN = '/store/user/ejclemen/'
config.Data.publication = True
config.Data.publishDataName = 'DYJetsToLL_M50_PU20bx25'

config.section_("Site")
config.Site.storageSite = 'T2_UK_SGrid_Bristol'
