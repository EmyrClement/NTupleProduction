import os, subprocess

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

pathOfCrabWorkdirs = '/storage/db0268/TopCrossSections/NTupleProduction/CMSSW_7_4_15/src/workdirCrab/v29/2015-10-28'

for crabWorkdir in os.listdir(pathOfCrabWorkdirs):
	os.system('crab kill ' + pathOfCrabWorkdirs+crabWorkdir )

