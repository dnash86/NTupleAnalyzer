from ROOT import *
import os
import sys
import math
from time import strftime

Name='_Fiducial2'
Log = 'FiducialLog2.txt'

os.system('python FiducialCutsElectron.py -I -i Selection_ee_NewQCDStudy.csv -f CentralValues'+Name)
os.system('kinit -R')
os.system('echo "NoSystematics" >> '+Log)
os.system('cat CentralValues'+Name+'.txt >> '+Log)
os.system('cat CentralValues'+Name+'_Errors.txt >> '+Log)


os.system('python FiducialCutsElectron.py -I -i Selection_ee_NewQCDStudy.csv -pd -f PUDownValues'+Name)
os.system('kinit -R')
os.system('echo "PU_down" >> '+Log)
os.system('cat PUDownValues'+Name+'.txt >> '+Log)
os.system('cat PUDownValues'+Name+'_Errors.txt >> '+Log)


os.system('python FiducialCutsElectron.py -I -i Selection_ee_NewQCDStudy.csv -pd -f PUUpValues'+Name)
os.system('kinit -R')
os.system('echo "PU_up" >> '+Log)
os.system('cat PUUpValues'+Name+'.txt >> '+Log)
os.system('cat PUUpValues'+Name+'_Errors.txt >> '+Log)


os.system('python FiducialCutsElectron.py -I -i Selection_ee_NewQCDStudy.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_June26_Systematics__EleScaleDown_2014_06_29_12_26_23/SummaryFiles -f EleDownValues'+Name)
os.system('kinit -R')
os.system('echo "MuScaleDown" >> '+Log)
os.system('cat EleDownValues'+Name+'.txt >> '+Log)
os.system('cat EleDownValues'+Name+'_Errors.txt >> '+Log)



os.system('python FiducialCutsElectron.py -I -i Selection_ee_NewQCDStudy.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_June26_Systematics__EleScaleUp_2014_06_26_14_41_45/SummaryFiles -f EleUpValues'+Name)
os.system('kinit -R')
os.system('echo "MuScaleUp" >> '+Log)
os.system('cat EleUpValues'+Name+'.txt >> '+Log)
os.system('cat EleUpValues'+Name+'_Errors.txt >> '+Log)


os.system('python FiducialCutsElectron.py -I -i Selection_ee_NewQCDStudy.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_June26_Systematics__EleSmear_2014_07_01_16_03_04/SummaryFiles -f EleSmearValues'+Name)
os.system('kinit -R')
os.system('echo "MuSmear" >> '+Log)
os.system('cat EleSmearValues'+Name+'.txt >> '+Log)
os.system('cat EleSmearValues'+Name+'_Errors.txt >> '+Log)


os.system('python FiducialCutsElectron.py -I -i Selection_ee_NewQCDStudy.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_June26_Systematics__JetScaleDown_2014_06_29_00_15_08/SummaryFiles -f JetDownValues'+Name)
os.system('kinit -R')
os.system('echo "JetScaleDown" >> '+Log)
os.system('cat JetDownValues'+Name+'.txt >> '+Log)
os.system('cat JetDownValues'+Name+'_Errors.txt >> '+Log)


os.system('python FiducialCutsElectron.py -I -i Selection_ee_NewQCDStudy.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_June26_Systematics__JetScaleUp_2014_06_27_18_22_36/SummaryFiles -f JetUpValues'+Name)
os.system('kinit -R')
os.system('echo "JetScaleUp" >> '+Log)
os.system('cat JetUpValues'+Name+'.txt >> '+Log)
os.system('cat JetUpValues'+Name+'_Errors.txt >> '+Log)


os.system('python FiducialCutsElectron.py -I -i Selection_ee_NewQCDStudy.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_June26_Systematics__JetSmear_2014_06_29_17_51_55/SummaryFiles -f JetSmearValues'+Name)
os.system('kinit -R')
os.system('echo "JetSmear" >> '+Log)
os.system('cat JetSmearValues'+Name+'.txt >> '+Log)
os.system('cat JetSmearValues'+Name+'_Errors.txt >> '+Log)



os.system('python FiducialCutsElectron.py -I -i Selection_ee_NewQCDStudy.csv -s /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_MCShape_Electrons_2014_07_08_15_11_58/SummaryFiles/ZJetsJBin_matchingdown.root -f ZMatchDownValues'+Name)
os.system('echo "ZMatchDown" >> '+Log)
os.system('cat ZMatchDownValues'+Name+'.txt >> '+Log)
os.system('cat ZMatchDownValues'+Name+'_Errors.txt >> '+Log)


os.system('python FiducialCutsElectron.py -I -i Selection_ee_NewQCDStudy.csv -s /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_MCShape_Electrons_2014_07_08_15_11_58/SummaryFiles/ZJetsJBin_matchingup.root -f ZMatchUpValues'+Name)
os.system('echo "ZMatchUp" >> '+Log)
os.system('cat ZMatchUpValues'+Name+'.txt >> '+Log)
os.system('cat ZMatchUpValues'+Name+'_Errors.txt >> '+Log)


os.system('python FiducialCutsElectron.py -I -i Selection_ee_NewQCDStudy.csv -s /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_MCShape_Electrons_2014_07_08_15_11_58/SummaryFiles/ZJetsJBin_scaledown.root -f ZScaleDownValues'+Name)
os.system('echo "ZScaleDown" >> '+Log)
os.system('cat ZScaleDownValues'+Name+'.txt >> '+Log)
os.system('cat ZScaleDownValues'+Name+'_Errors.txt >> '+Log)


os.system('python FiducialCutsElectron.py -I -i Selection_ee_NewQCDStudy.csv -s /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_MCShape_Electrons_2014_07_08_15_11_58/SummaryFiles/ZJetsJBin_scaleup.root -f ZScaleUpValues'+Name)
os.system('echo "ZScaleUp" >> '+Log)
os.system('cat ZScaleUpValues'+Name+'.txt >> '+Log)
os.system('cat ZScaleUpValues'+Name+'_Errors.txt >> '+Log)

