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
submitter.write('cp '+here +'/CMS_lumi.py .\n')
submitter.write('cp '+here +'/WeightsAndFilters.py .\n')
submitter.write('cp '+here +'/HistoCreation.py .\n')
submitter.write('cp '+here +'/Selection_ee_NewQCDStudy_125jetptcut.csv .\n')
submitter.write('cp '+here +'/FiducialCutsElectron.py .\n')
String = 'python FiducialCutsElectron.py  -I -i Selection_ee_NewQCDStudy_125jetptcut.csv -f CentralValues'+Name+'\n'
submitter.write(String)
submitter.write('cp *.txt '+here+'/FiducialElectrons0p75Cut\n')
submitter.close()
os.system("bsub -J CentralValues -q 8nh < submit.csh")
os.system("sleep 5")

submitter = open('submit.csh','w')
submitter.write('#!/bin/csh\n')
submitter.write('cd '+here+'\n')
#submitter.write('eval `scramv1 runtime -csh`\n\n')
submitter.write('cmsenv\n\n')
submitter.write('cd -\n')
submitter.write('cp '+here +'/CMSStyle.py .\n')
submitter.write('cp '+here +'/CMS_lumi.py .\n')
submitter.write('cp '+here +'/WeightsAndFilters.py .\n')
submitter.write('cp '+here +'/HistoCreation.py .\n')
submitter.write('cp '+here +'/Selection_ee_NewQCDStudy_125jetptcut.csv .\n')
submitter.write('cp '+here +'/FiducialCutsElectron.py .\n')
String = 'python FiducialCutsElectron.py  -I -i Selection_ee_NewQCDStudy_125jetptcut.csv -pd -f PUDownValues'+Name+'\n'
submitter.write(String)
submitter.write('cp *.txt '+here+'/FiducialElectrons0p75Cut\n')
submitter.close()
os.system("bsub -J PUDownValues -q 8nh < submit.csh")
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
String = 'python FiducialCutsElectron.py  -I -i Selection_ee_NewQCDStudy_125jetptcut.csv -pd -f PUUpValues'+Name+'\n'
submitter.write(String)
submitter.write('cp *.txt '+here+'/FiducialElectrons0p75Cut\n')
submitter.close()
os.system("bsub -J PUUpValues -q 8nh < submit.csh")
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
String = 'python FiducialCutsElectron.py  -I -i Selection_ee_NewQCDStudy_125jetptcut.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_June26_Systematics__EleScaleDown_2014_06_29_12_26_23/SummaryFiles /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_Oct29FixedGenMassesStatusOne_Systematics__EleScaleDown_2014_10_30_08_50_59/SummaryFiles -f EleDownValues'+Name+'\n'
submitter.write(String)
submitter.write('cp *.txt '+here+'/FiducialElectrons0p75Cut\n')
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
String = 'python FiducialCutsElectron.py  -I -i Selection_ee_NewQCDStudy_125jetptcut.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_June26_Systematics__EleScaleUp_2014_06_26_14_41_45/SummaryFiles /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_Oct29FixedGenMassesStatusOne_Systematics__EleScaleUp_2014_10_29_22_18_24/SummaryFiles/ -f EleUpValues'+Name+'\n'
submitter.write(String)
submitter.write('cp *.txt '+here+'/FiducialElectrons0p75Cut\n')
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
String = 'python FiducialCutsElectron.py  -I -i Selection_ee_NewQCDStudy_125jetptcut.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_June26_Systematics__EleSmear_2014_07_01_16_03_04/SummaryFiles /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_Oct29FixedGenMassesStatusOne_Systematics__EleSmear_2014_10_30_16_55_46/SummaryFiles/ -f EleSmearValues'+Name+'\n'
submitter.write(String)
submitter.write('cp *.txt '+here+'/FiducialElectrons0p75Cut\n')
submitter.close()
os.system("bsub -J EleSmearValues -q 8nh < submit.csh")
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
String = 'python FiducialCutsElectron.py  -I -i Selection_ee_NewQCDStudy_125jetptcut.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_Oct29FixedGenMassesStatusOne_Systematics__JetScaleDown_2014_11_01_16_10_00/SummaryFiles/ /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_Oct29FixedGenMassesStatusOne_Systematics__JetScaleDown_2014_11_01_16_10_00/SummaryFiles/ -f JetDownValues'+Name+'\n'
submitter.write(String)
submitter.write('cp *.txt '+here+'/FiducialElectrons0p75Cut\n')
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
submitter.write('cp *.txt '+here+'/FiducialElectrons0p75Cut\n')
submitter.close()
os.system("bsub -J JetSmear -q 8nh < submit.csh")
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
String = 'python FiducialCutsElectron.py  -I -i Selection_ee_NewQCDStudy_125jetptcut.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_June26_Systematics__JetScaleUp_2014_06_27_18_22_36/SummaryFiles /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_Oct29FixedGenMassesStatusOne_Systematics__JetScaleUp_2014_10_30_20_01_04/SummaryFiles -f JetUpValues'+Name+'\n'
submitter.write(String)
submitter.write('cp *.txt '+here+'/FiducialElectrons0p75Cut\n')
submitter.close()
os.system("bsub -J JetUpValues -q 8nh < submit.csh")
os.system("sleep 5")
#submitter = open('submit.csh','w')
#submitter.write('#!/bin/csh\n')
#submitter.write('cd '+here+'\n')
##submitter.write('eval `scramv1 runtime -csh`\n\n')
#submitter.write('cd -\n')
#submitter.write('cp '+here +'/CMSStyle.py .\n')
#submitter.write('cp '+here +'/WeightsAndFilters.py .\n')
#submitter.write('cp '+here +'/HistoCreation.py .\n')
#submitter.write('cp '+here +'/Selection_ee_NewQCDStudy_125jetptcut.csv .\n')
#submitter.write('cp '+here +'/FiducialCutsElectron.py .\n')
#String = 'python FiducialCutsElectron.py  -I -i Selection_ee_NewQCDStudy_125jetptcut.csv -s /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_MCShapeElectrons_2014_08_08_13_02_05/SummaryFiles/ZJetsJBin_matchingdown.root -f ZMatchDownValues'+Name+'\n'
#submitter.write(String)
#submitter.write('cp *.txt '+here+'/FiducialElectrons0p75Cut\n')
#submitter.close()
#os.system("bsub -J ZMatchDownValues -q 8nh < submit.csh")


#submitter = open('submit.csh','w')
#submitter.write('#!/bin/csh\n')
#submitter.write('cd '+here+'\n')
##submitter.write('eval `scramv1 runtime -csh`\n\n')
#submitter.write('cd -\n')
#submitter.write('cp '+here +'/CMSStyle.py .\n')
#submitter.write('cp '+here +'/WeightsAndFilters.py .\n')
#submitter.write('cp '+here +'/HistoCreation.py .\n')
#submitter.write('cp '+here +'/Selection_ee_NewQCDStudy_125jetptcut.csv .\n')
#submitter.write('cp '+here +'/FiducialCutsElectron.py .\n')
#String = 'python FiducialCutsElectron.py  -I -i Selection_ee_NewQCDStudy_125jetptcut.csv -s /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_MCShapeElectrons_2014_08_08_13_02_05/SummaryFiles/ZJetsJBin_matchingup.root -f ZMatchUpValues'+Name+'\n'
#submitter.write(String)
#submitter.write('cp *.txt '+here+'/FiducialElectrons0p75Cut\n')
#submitter.close()
#os.system("bsub -J ZMatchUpValues -q 8nh < submit.csh")


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
String = 'python FiducialCutsElectron.py  -I -i Selection_ee_NewQCDStudy_125jetptcut.csv -s /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_FastSimZElectrons_2014_09_05_15_20_20/SummaryFiles/ZJetsJBin_scaledown.root -f ZScaleDownValues'+Name+'\n'
submitter.write(String)
submitter.write('cp *.txt '+here+'/FiducialElectrons0p75Cut\n')
submitter.close()
os.system("bsub -J ZScaleDownValues -q 8nh < submit.csh")
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
String = 'python FiducialCutsElectron.py  -I -i Selection_ee_NewQCDStudy_125jetptcut.csv -s /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_FastSimZElectrons_2014_09_05_15_20_20/SummaryFiles/ZJetsJBin_scaleup.root -f ZScaleUpValues'+Name+'\n'
submitter.write(String)
submitter.write('cp *.txt '+here+'/FiducialElectrons0p75Cut\n')
submitter.close()
os.system("bsub -J ZScaleUpValues -q 8nh < submit.csh")
os.system("sleep 5")
