from ROOT import *
import os
import sys
import math
from time import strftime

Name='_Electrons'

here= os.popen('pwd').readlines()[0].replace('\n','')
submitter = open('submit.csh','w')

submitter = open('submit.csh','w')
submitter.write('#!/bin/csh\n')
submitter.write('cd '+here+'\n')
submitter.write('eval `scramv1 runtime -csh`\n\n')
submitter.write('cd -\n')
submitter.write('cp '+here +'/CMSStyle.py .\n')
submitter.write('cp '+here +'/WeightsAndFilters.py .\n')
submitter.write('cp '+here +'/HistoCreation.py .\n')
submitter.write('cp '+here +'/Selection_ee_NewQCDStudy_125jetptcut.csv .\n')
submitter.write('cp '+here +'/MakePlotsSingle_ee2012_NewQCD_NonEmulatedTriggers.py .\n')
String = 'python MakePlotsSingle_ee2012_NewQCD_NonEmulatedTriggers.py  -I -i Selection_ee_NewQCDStudy_125jetptcut.csv -pd -f PUDownValues'+Name+'\n'
submitter.write(String)
submitter.write('cp *.txt '+here+'/ElePUReRun\n')
submitter.close()
os.system("bsub -J PUDownValues -q 8nh < submit.csh")
os.system("sleep 5")

submitter = open('submit.csh','w')
submitter.write('#!/bin/csh\n')
submitter.write('cd '+here+'\n')
submitter.write('eval `scramv1 runtime -csh`\n\n')
submitter.write('cd -\n')
submitter.write('cp '+here +'/CMSStyle.py .\n')
submitter.write('cp '+here +'/WeightsAndFilters.py .\n')
submitter.write('cp '+here +'/HistoCreation.py .\n')
submitter.write('cp '+here +'/Selection_ee_NewQCDStudy_125jetptcut.csv .\n')
submitter.write('cp '+here +'/MakePlotsSingle_ee2012_NewQCD_NonEmulatedTriggers.py .\n')
String = 'python MakePlotsSingle_ee2012_NewQCD_NonEmulatedTriggers.py  -I -i Selection_ee_NewQCDStudy_125jetptcut.csv -pu -f PUUpValues'+Name+'\n'
submitter.write(String)
submitter.write('cp *.txt '+here+'/ElePUReRun\n')
submitter.close()
os.system("bsub -J PUUpValues -q 8nh < submit.csh")
os.system("sleep 5")

