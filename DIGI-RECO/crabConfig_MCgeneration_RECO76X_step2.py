from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'request_RECO76X_DATASETIN_DATE'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

# config.JobType.pluginName = 'PrivateMC'
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'config_RECO76X_step2.py'

config.Data.inputDataset = 'DATASETIN'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.outputPrimaryDataset = 'MSSMHbb'
config.Data.unitsPerJob = 1
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'DATASETOUT_RECO76X'

config.Site.storageSite = 'T2_CH_CSCS'
