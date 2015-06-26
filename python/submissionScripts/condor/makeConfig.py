import os
import glob
from mergeROOTFilesWithCompression import getGroupedFilesToUse

pathOfCrabWorkdirs = '/storage/ec6821/NTupleProd/CMSSW_7_4_4_patch2/src/workdirCrab/v20/2015-06-11/'

version = pathOfCrabWorkdirs.split('/')[-3]

ntupleBaseDir = '/gpfs_phys/storm/cms/user/ejclemen/'

outputBaseDir = '/hdfs/TopQuarkGroup/run2/ntuples/'
outputDirHdfs = outputBaseDir + version + '/'

configFile = open('mergeConfig.py','w');

configFile.write('outputDir = "' + outputDirHdfs + '"\n')
configFile.write('jobs = [\n')

if not os.path.exists(outputDirHdfs):
	os.mkdir(outputDirHdfs)

print "There are ",len(os.listdir(pathOfCrabWorkdirs))," samples"
nJobs = 0
for crabWorkdir in os.listdir(pathOfCrabWorkdirs):

	crabLogFile = open(pathOfCrabWorkdirs+'/'+crabWorkdir+'/crab.log','r')

	gotTaskName = False
	gotRequestName = False
	gotInputDataset = False
	taskName = ''
	requestName = ''
	inputDataset = ''
	for line in crabLogFile.readlines():

		# Get info to put together output ntuple location
		if not gotTaskName and line.find('Task name')>=0:
			tasknameTemp = line
			tasknameTemp = tasknameTemp.split('Task name:')[-1]
			tasknameTemp = tasknameTemp.split('_')
			tasknameTemp = tasknameTemp[0].strip() + '_' + tasknameTemp[1].strip()
			taskName = tasknameTemp.split(':')[0]
			gotTaskName = True
		elif not gotRequestName and line.find('publishDataName')>=0:
			requestName = line.split('\'')[-2]
			gotRequestName = True
		elif not gotInputDataset and line.find('inputDataset')>=0:
			inputDataset = line.split('/')[1]
			gotInputDataset = True

		if gotTaskName and gotRequestName and gotInputDataset :
			break

	crabLogFile.close()

	# Check if this has already been merged/exists in hdfs
	# print outputDirHdfs + '/' + requestName
	# if os.path.exists(outputDirHdfs + '/' + requestName):
	# 	continue

	ntupleDir = ntupleBaseDir + '/' + inputDataset + '/' + requestName + '/' + taskName

	files, uniqueFiles, allButUsedFiles, groupedFiles = getGroupedFilesToUse( ntupleDir + '/*/' )

	if len(groupedFiles) <= 5:
		configFile.write('\t["'+requestName + '",\t"' + ntupleDir + '/",\t-1\t],\n')
		nJobs += 1
	else :
		for job in range(0,len(groupedFiles)):
			configFile.write('\t["'+requestName + '",\t"' + ntupleDir + '/",\t'+str(job)+'\t],\n')
			nJobs += 1

configFile.write(']\n')
configFile.close()

print 'There are %s jobs' % nJobs