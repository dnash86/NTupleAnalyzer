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
#submitter.write('eval `scramv1 runtime -csh`\n\n')
submitter.write('cmsenv\n\n')
submitter.write('cd -\n')
submitter.write('cp '+here +'/CMSStyle.py .\n')
submitter.write('cp '+here +'/WeightsAndFilters.py .\n')
submitter.write('cp '+here +'/HistoCreation.py .\n')
submitter.write('cp '+here +'/Selection_ee_NewQCDStudy_125jetptcut.csv .\n')
submitter.write('cp '+here +'/FiducialCutsElectron.py .\n')
String = 'python FiducialCutsElectron.py  -I -i Selection_ee_NewQCDStudy_125jetptcut.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_Mar10_EleSystsFromEGM13001_Systematics__EleScaleDown_2015_03_15_15_53_17/SummaryFiles /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_Mar10_EleSystsFromEGM13001_Systematics__EleScaleDown_2015_03_15_15_53_17/SummaryFiles -f EleDownValues'+Name+'\n'
submitter.write(String)
submitter.write('cp *.txt '+here+'/FiducialElectrons0p66Cut_FixedEleSysts\n')
submitter.close()
os.system("bsub -J EleDownValues -q 8nh < submit.csh")
os.system("sleep 5")

submitter = open('submit.csh','w')
submitter.write('#!/bin/csh\n')
submitter.write('cd '+here+'\n')
#submitter.write('eval `scramv1 runtime -csh`\n\n')
submitter.write('cmsenv\n\n')
submitter.write('cd -\n')
submitter.write('cp '+here +'/CMSStyle.py .\n')
submitter.write('cp '+here +'/WeightsAndFilters.py .\n')
submitter.write('cp '+here +'/HistoCreation.py .\n')
submitter.write('cp '+here +'/Selection_ee_NewQCDStudy_125jetptcut.csv .\n')
submitter.write('cp '+here +'/FiducialCutsElectron.py .\n')
String = 'python FiducialCutsElectron.py  -I -i Selection_ee_NewQCDStudy_125jetptcut.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_Mar10_EleSystsFromEGM13001_Systematics__EleScaleUp_2015_03_14_19_43_31/SummaryFiles /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_Mar10_EleSystsFromEGM13001_Systematics__EleScaleUp_2015_03_14_19_43_31/SummaryFiles -f EleUpValues'+Name+'\n'
submitter.write(String)
submitter.write('cp *.txt '+here+'/FiducialElectrons0p66Cut_FixedEleSysts\n')
submitter.close()
os.system("bsub -J EleUpValues -q 8nh < submit.csh")
os.system("sleep 5")

submitter = open('submit.csh','w')
submitter.write('#!/bin/csh\n')
submitter.write('cd '+here+'\n')
#submitter.write('eval `scramv1 runtime -csh`\n\n')
submitter.write('cmsenv\n\n')
submitter.write('cd -\n')
submitter.write('cp '+here +'/CMSStyle.py .\n')
submitter.write('cp '+here +'/WeightsAndFilters.py .\n')
submitter.write('cp '+here +'/HistoCreation.py .\n')
submitter.write('cp '+here +'/Selection_ee_NewQCDStudy_125jetptcut.csv .\n')
submitter.write('cp '+here +'/FiducialCutsElectron.py .\n')
String = 'python FiducialCutsElectron.py  -I -i Selection_ee_NewQCDStudy_125jetptcut.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_Mar10_EleSystsFromEGM13001_Systematics__EleSmear_2015_03_16_08_35_35/SummaryFiles /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_Mar10_EleSystsFromEGM13001_Systematics__EleSmear_2015_03_16_08_35_35/SummaryFiles -f EleSmearValues'+Name+'\n'
submitter.write(String)
submitter.write('cp *.txt '+here+'/FiducialElectrons0p66Cut_FixedEleSysts\n')
submitter.close()
os.system("bsub -J EleSmearValues -q 8nh < submit.csh")
os.system("sleep 5")

