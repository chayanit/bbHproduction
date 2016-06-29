from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'request_DR76X_/MSSMHbb/clange-SUSYGluGluToBBHToBB_M-500_cfg-7841cb5200369ad819ec769a642cd097/USER_2016-06-28'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

# config.JobType.pluginName = 'PrivateMC'
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'config_DIGI76X_step1.py'

config.Data.inputDataset = '/MSSMHbb/clange-SUSYGluGluToBBHToBB_M-500_cfg-7841cb5200369ad819ec769a642cd097/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.outputPrimaryDataset = 'MSSMHbb'
config.Data.unitsPerJob = 1
config.Data.totalUnits = config.Data.unitsPerJob * 500
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'SUSYGluGluToBBHToBB_M-500_cfg_DIGI76X_DIGI76X'

config.Site.storageSite = 'T2_CH_CSCS'
