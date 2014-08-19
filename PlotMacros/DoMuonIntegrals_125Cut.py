from ROOT import *
import os
import sys
import math
from time import strftime


os.system('python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_125jetptcut.csv -f CentralValues_Muon_125jetptcut')
os.system('kinit -R')
os.system('python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_125jetptcut.csv -pd -f PUDownValues_Muon_125jetptcut')
os.system('kinit -R')
os.system('python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_125jetptcut.csv -pd -f PUUpValues_Muon_125jetptcut')
os.system('kinit -R')
os.system('python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_125jetptcut.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_July31_Systematics__MuScaleDown_2014_08_03_17_36_35/SummaryFiles -f MuDownValues_Muon_125jetptcut')
os.system('kinit -R')
os.system('python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_125jetptcut.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_July31_Systematics__MuScaleUp_2014_08_03_06_53_40/SummaryFiles -f MuUpValues_Muon_125jetptcut')
os.system('kinit -R')
os.system('python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_125jetptcut.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_July31_Systematics__MuSmear_2014_08_05_11_55_09/SummaryFiles -f MuSmearValues_Muon_125jetptcut')
os.system('kinit -R')
os.system('python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_125jetptcut.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_July31_Systematics__JetScaleDown_2014_08_02_20_11_32/SummaryFiles -f JetDownValues_Muon_125jetptcut')
os.system('kinit -R')
os.system('python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_125jetptcut.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_July31_Systematics__JetScaleUp_2014_08_01_22_07_07/SummaryFiles -f JetUpValues_Muon_125jetptcut')
os.system('kinit -R')
os.system('python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_125jetptcut.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_July31_Systematics__JetSmear_2014_08_04_05_17_00/SummaryFiles -f JetSmearValues_Muon_125jetptcut')

