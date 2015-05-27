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
submitter.write('cp '+here +'/CMS_lumi.py .\n')
submitter.write('cp '+here +'/WeightsAndFilters.py .\n')
submitter.write('cp '+here +'/HistoCreation.py .\n')
submitter.write('cp '+here +'/Selection_ee_NewQCDStudy_125jetptcut.csv .\n')
submitter.write('cp '+here +'/ElectronPtLLRescales.csv .\n')
submitter.write('cp '+here +'/MakePlotsSingle_ee2012_NewQCD_NonEmulatedTriggers.py .\n')
String = 'python MakePlotsSingle_ee2012_NewQCD_NonEmulatedTriggers.py  -I -i Selection_ee_NewQCDStudy_125jetptcut.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_June26_Systematics__JetScaleDown_2014_06_29_00_15_08/SummaryFiles/ /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_Oct29FixedGenMassesStatusOne_Systematics__JetScaleDown_2014_11_01_16_10_00/SummaryFiles/ -r ElectronPtLLRescales.csv -f JetDownValues'+Name+'\n'
submitter.write(String)
submitter.write('cp *.txt '+here+'/ParallelElectronIntegrals_Rescaled\n')
submitter.close()
os.system("bsub -J JetDownValues -q 8nh < submit.csh")
os.system("sleep 5")

submitter = open('submit.csh','w')
submitter.write('#!/bin/csh\n')
submitter.write('cd '+here+'\n')
submitter.write('eval `scramv1 runtime -csh`\n\n')
submitter.write('cd -\n')
submitter.write('cp '+here +'/CMSStyle.py .\n')
submitter.write('cp '+here +'/CMS_lumi.py .\n')
submitter.write('cp '+here +'/WeightsAndFilters.py .\n')
submitter.write('cp '+here +'/HistoCreation.py .\n')
submitter.write('cp '+here +'/Selection_ee_NewQCDStudy_125jetptcut.csv .\n')
submitter.write('cp '+here +'/ElectronPtLLRescales.csv .\n')
submitter.write('cp '+here +'/MakePlotsSingle_ee2012_NewQCD_NonEmulatedTriggers.py .\n')
String = 'python MakePlotsSingle_ee2012_NewQCD_NonEmulatedTriggers.py  -I -i Selection_ee_NewQCDStudy_125jetptcut.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_June26_Systematics__JetScaleUp_2014_06_27_18_22_36/SummaryFiles  /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_Oct29FixedGenMassesStatusOne_Systematics__JetScaleUp_2014_10_30_20_01_04/SummaryFiles  -r ElectronPtLLRescales.csv -f JetUpValues'+Name+'\n'
submitter.write(String)
submitter.write('cp *.txt '+here+'/ParallelElectronIntegrals_Rescaled\n')
submitter.close()
os.system("bsub -J JetUpValues -q 8nh < submit.csh")
os.system("sleep 5")
