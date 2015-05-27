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
submitter.write('cp '+here +'/FiducialCutsElectron.py .\n')
String = 'python FiducialCutsElectron.py  -I -i Selection_ee_NewQCDStudy_125jetptcut.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_Oct29FixedGenMassesStatusOne_Systematics__JetScaleDown_2014_11_01_16_10_00/SummaryFiles/ /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_Oct29FixedGenMassesStatusOne_Systematics__JetScaleDown_2014_11_01_16_10_00/SummaryFiles/ -f JetDownValues'+Name+'\n'
submitter.write(String)
submitter.write('cp *.txt '+here+'/FiducialElectronsFile1p0Sel\n')
submitter.close()
os.system("bsub -J JetDownValues -q 8nh < submit.csh")
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
submitter.write('cp '+here +'/FiducialCutsElectron.py .\n')
String = 'python FiducialCutsElectron.py  -I -i Selection_ee_NewQCDStudy_125jetptcut.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_June26_Systematics__JetSmear_2014_06_29_17_51_55/SummaryFiles /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_Oct29FixedGenMassesStatusOne_Systematics__JetSmear_2014_10_30_13_45_57/SummaryFiles/ -f JetSmearValues'+Name+'\n'
submitter.write(String)
submitter.write('cp *.txt '+here+'/FiducialElectronsFile1p0Sel\n')
submitter.close()
os.system("bsub -J JetSmear -q 8nh < submit.csh")
os.system("sleep 5")
