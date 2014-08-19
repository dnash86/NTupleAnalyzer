from ROOT import *
import os
import sys
import math
from time import strftime

Name='_Muon_newQCD'

os.system('python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy.csv -f CentralValues'+Name)
os.system('kinit -R')
os.system('echo "Nosystematics" >> MuonLog_newQCD.txt')
os.system('cat CentralValues'+Name+'.txt >> MuonLog_newQCD.txt')
os.system('cat CentralValues'+Name+'_Errors.txt >> MuonLog_newQCD.txt')


os.system('python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy.csv -pd -f PUDownValues'+Name)
os.system('kinit -R')
os.system('echo "PU_down" >> MuonLog_newQCD.txt')
os.system('cat PUDownValues'+Name+'.txt >> MuonLog_newQCD.txt')
os.system('cat PUDownValues'+Name+'_Errors.txt >> MuonLog_newQCD.txt')


os.system('python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy.csv -pd -f PUUpValues'+Name)
os.system('kinit -R')
os.system('echo "PU_up" >> MuonLog_newQCD.txt')
os.system('cat PUUpValues'+Name+'.txt >> MuonLog_newQCD.txt')
os.system('cat PUUpValues'+Name+'_Errors.txt >> MuonLog_newQCD.txt')


os.system('python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_July31_Systematics__MuScaleDown_2014_08_03_17_36_35/SummaryFiles -f MuDownValues'+Name)
os.system('kinit -R')
os.system('echo "MuScaleDown" >> MuonLog_newQCD.txt')
os.system('cat MuDownValues'+Name+'.txt >> MuonLog_newQCD.txt')
os.system('cat MuDownValues'+Name+'_Errors.txt >> MuonLog_newQCD.txt')


os.system('python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_July31_Systematics__MuScaleUp_2014_08_03_06_53_40/SummaryFiles -f MuUpValues'+Name)
os.system('kinit -R')
os.system('echo "MuScaleUp" >> MuonLog_newQCD.txt')
os.system('cat MuUpValues'+Name+'.txt >> MuonLog_newQCD.txt')
os.system('cat MuUpValues'+Name+'_Errors.txt >> MuonLog_newQCD.txt')


os.system('python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_July31_Systematics__MuSmear_2014_08_05_11_55_09/SummaryFiles -f MuSmearValues'+Name)
os.system('kinit -R')
os.system('echo "MuSmear" >> MuonLog_newQCD.txt')
os.system('cat MuSmearValues'+Name+'.txt >> MuonLog_newQCD.txt')
os.system('cat MuSmearValues'+Name+'_Errors.txt >> MuonLog_newQCD.txt')


os.system('python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_July31_Systematics__JetScaleDown_2014_08_02_20_11_32/SummaryFiles -f JetDownValues'+Name)
os.system('kinit -R')
os.system('echo "JetScaleDown" >> MuonLog_newQCD.txt')
os.system('cat JetDownValues'+Name+'.txt >> MuonLog_newQCD.txt')
os.system('cat JetDownValues'+Name+'_Errors.txt >> MuonLog_newQCD.txt')


os.system('python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_July31_Systematics__JetScaleUp_2014_08_01_22_07_07/SummaryFiles -f JetUpValues'+Name)
os.system('kinit -R')
os.system('echo "JetScaleUp" >> MuonLog_newQCD.txt')
os.system('cat JetUpValues'+Name+'.txt >> MuonLog_newQCD.txt')
os.system('cat JetUpValues'+Name+'_Errors.txt >> MuonLog_newQCD.txt')


os.system('python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_July31_Systematics__JetSmear_2014_08_04_05_17_00/SummaryFiles -f JetSmearValues'+Name)
os.system('echo "JetSmear" >> MuonLog_newQCD.txt')
os.system('cat JetSmearValues'+Name+'.txt >> MuonLog_newQCD.txt')
os.system('cat JetSmearValues'+Name+'_Errors.txt >> MuonLog_newQCD.txt')


os.system('python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy.csv -s /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_MCShapeMuons_2014_08_08_02_14_04/SummaryFiles/ZJetsJBin_matchingdown.root -f ZMatchDownValues'+Name)
os.system('echo "ZMatchDown" >> MuonLog_newQCD.txt')
os.system('cat ZMatchDownValues'+Name+'.txt >> MuonLog_newQCD.txt')
os.system('cat ZMatchDownValues'+Name+'_Errors.txt >> MuonLog_newQCD.txt')


os.system('python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy.csv -s /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_MCShapeMuons_2014_08_08_02_14_04/SummaryFiles/ZJetsJBin_matchingup.root -f ZMatchUpValues'+Name)
os.system('echo "ZMatchUp" >> MuonLog_newQCD.txt')
os.system('cat ZMatchUpValues'+Name+'.txt >> MuonLog_newQCD.txt')
os.system('cat ZMatchUpValues'+Name+'_Errors.txt >> MuonLog_newQCD.txt')


os.system('python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy.csv -s /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_MCShapeMuons_2014_08_08_02_14_04/SummaryFiles/ZJetsJBin_scaledown.root -f ZScaleDownValues'+Name)
os.system('echo "ZScaleDown" >> MuonLog_newQCD.txt')
os.system('cat ZScaleDownValues'+Name+'.txt >> MuonLog_newQCD.txt')
os.system('cat ZScaleDownValues'+Name+'_Errors.txt >> MuonLog_newQCD.txt')


os.system('python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy.csv -s /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_MCShapeMuons_2014_08_08_02_14_04/SummaryFiles/ZJetsJBin_scaleup.root -f ZScaleUpValues'+Name)
os.system('echo "ZScaleUp" >> MuonLog_newQCD.txt')
os.system('cat ZScaleUpValues'+Name+'.txt >> MuonLog_newQCD.txt')
os.system('cat ZScaleUpValues'+Name+'_Errors.txt >> MuonLog_newQCD.txt')

