from ROOT import *
import os
import sys
import math
from time import strftime

Name='_Muon_newQCD'

here= os.popen('pwd').readlines()[0].replace('\n','')
submitter = open('submit.csh','w')

submitter.write('#!/bin/csh\n')
submitter.write('cd '+here)
submitter.write('eval `scramv1 runtime -csh`\n\n')
submitter.write('cd -')
submitter.write('cp '+here +'/MakePlotsSingle_mumu2012_NonEmulatedTriggers.py .\n')
String = "python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy.csv -f CentralValues"+Name+"\n"
submitter.write(String)
submitter.write('cp *.txt '+here+'/ParallelMuonIntegrals\n')
submitter.close()
os.system("bsub -J CentralValues -q 1nh < submit.csh")
os.system("sleep 5")

submitter = open('submit.csh','w')
submitter.write('#!/bin/csh\n')
submitter.write('cd '+here)
submitter.write('eval `scramv1 runtime -csh`\n\n')
submitter.write('cd -')
submitter.write('cp '+here +'/MakePlotsSingle_mumu2012_NonEmulatedTriggers.py .\n')
String = "python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy.csv -pd -f PUDownValues"+Name
submitter.write(String)
submitter.write('cp *.txt '+here+'/ParallelMuonIntegrals\n')
submitter.close()
os.system("bsub -J PUDownValues -q 1nh < submit.csh")
os.system("sleep 5")

submitter = open('submit.csh','w')
submitter.write('#!/bin/csh\n')
submitter.write('cd '+here)
submitter.write('eval `scramv1 runtime -csh`\n\n')
submitter.write('cd -')
submitter.write('cp '+here +'/MakePlotsSingle_mumu2012_NonEmulatedTriggers.py .\n')
String = "python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy.csv -pd -f PUUpValues"+Name
submitter.write(String)
submitter.write('cp *.txt '+here+'/ParallelMuonIntegrals\n')
submitter.close()
os.system("bsub -J PUUpValues -q 1nh < submit.csh")
os.system("sleep 5")

submitter = open('submit.csh','w')
submitter.write('#!/bin/csh\n')
submitter.write('cd '+here)
submitter.write('eval `scramv1 runtime -csh`\n\n')
submitter.write('cd -')
submitter.write('cp '+here +'/MakePlotsSingle_mumu2012_NonEmulatedTriggers.py .\n')
String = "python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_July31_Systematics__MuScaleDown_2014_08_03_17_36_35/SummaryFiles -f MuDownValues"+Name
submitter.write(String)
submitter.write('cp *.txt '+here+'/ParallelMuonIntegrals\n')
submitter.close()
os.system("bsub -J MuDownValues -q 1nh < submit.csh")
os.system("sleep 5")

submitter = open('submit.csh','w')
submitter.write('#!/bin/csh\n')
submitter.write('cd '+here)
submitter.write('eval `scramv1 runtime -csh`\n\n')
submitter.write('cd -')
submitter.write('cp '+here +'/MakePlotsSingle_mumu2012_NonEmulatedTriggers.py .\n')
String = "python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_July31_Systematics__MuScaleUp_2014_08_03_06_53_40/SummaryFiles -f MuUpValues"+Name
submitter.write(String)
submitter.write('cp *.txt '+here+'/ParallelMuonIntegrals\n')
submitter.close()
os.system("bsub -J MuUpValues -q 1nh < submit.csh")
os.system("sleep 5")

submitter = open('submit.csh','w')
submitter.write('#!/bin/csh\n')
submitter.write('cd '+here)
submitter.write('eval `scramv1 runtime -csh`\n\n')
submitter.write('cd -')
submitter.write('cp '+here +'/MakePlotsSingle_mumu2012_NonEmulatedTriggers.py .\n')
String = "python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_July31_Systematics__MuSmear_2014_08_05_11_55_09/SummaryFiles -f MuSmearValues"+Name
submitter.write(String)
submitter.write('cp *.txt '+here+'/ParallelMuonIntegrals\n')
submitter.close()
os.system("bsub -J MuSmearValues -q 1nh < submit.csh")
os.system("sleep 5")

submitter = open('submit.csh','w')
submitter.write('#!/bin/csh\n')
submitter.write('eval `scramv1 runtime -csh`\n\n')
submitter.write('cd -')
submitter.write('cp '+here +'/MakePlotsSingle_mumu2012_NonEmulatedTriggers.py .\n')
String = "python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_July31_Systematics__JetScaleDown_2014_08_02_20_11_32/SummaryFiles -f JetDownValues"+Name
submitter.write(String)
submitter.write('cp *.txt '+here+'/ParallelMuonIntegrals\n')
submitter.close()
os.system("bsub -J JetDownValues -q 1nh < submit.csh")
os.system("sleep 5")

submitter = open('submit.csh','w')
submitter.write('#!/bin/csh\n')
submitter.write('cd '+here)
submitter.write('eval `scramv1 runtime -csh`\n\n')
submitter.write('cd -')
submitter.write('cp '+here +'/MakePlotsSingle_mumu2012_NonEmulatedTriggers.py .\n')
String = "python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_July31_Systematics__JetScaleUp_2014_08_01_22_07_07/SummaryFiles -f JetUpValues"+Name
submitter.write(String)
submitter.write('cp *.txt '+here+'/ParallelMuonIntegrals\n')
submitter.close()
os.system("bsub -J JetUpValues -q 1nh < submit.csh")
os.system("sleep 5")

submitter = open('submit.csh','w')
submitter.write('#!/bin/csh\n')
submitter.write('cd '+here)
submitter.write('eval `scramv1 runtime -csh`\n\n')
submitter.write('cd -')
submitter.write('cp '+here +'/MakePlotsSingle_mumu2012_NonEmulatedTriggers.py .\n')
String = "python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_July31_Systematics__JetSmear_2014_08_04_05_17_00/SummaryFiles -f JetSmearValues"+Name
submitter.write(String)
submitter.write('cp *.txt '+here+'/ParallelMuonIntegrals\n')
submitter.close()
os.system("bsub -J JetSmearValues -q 1nh < submit.csh")
os.system("sleep 5")

submitter = open('submit.csh','w')
submitter.write('#!/bin/csh\n')
submitter.write('cd '+here)
submitter.write('eval `scramv1 runtime -csh`\n\n')
submitter.write('cd -')
submitter.write('cp '+here +'/MakePlotsSingle_mumu2012_NonEmulatedTriggers.py .\n')
String = "python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy.csv -s /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_MCShapeMuons_2014_08_08_02_14_04/SummaryFiles/ZJetsJBin_matchingdown.root -f ZMatchDownValues"+Name
submitter.write(String)
submitter.write('cp *.txt '+here+'/ParallelMuonIntegrals\n')
submitter.close()
os.system("bsub -J ZMatchDownValues -q 1nh < submit.csh")
os.system("sleep 5")

submitter = open('submit.csh','w')
submitter.write('#!/bin/csh\n')
submitter.write('cd '+here)
submitter.write('eval `scramv1 runtime -csh`\n\n')
submitter.write('cd -')
submitter.write('cp '+here +'/MakePlotsSingle_mumu2012_NonEmulatedTriggers.py .\n')
String = "python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy.csv -s /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_MCShapeMuons_2014_08_08_02_14_04/SummaryFiles/ZJetsJBin_matchingup.root -f ZMatchUpValues"+Name
submitter.write(String)
submitter.write('cp *.txt '+here+'/ParallelMuonIntegrals\n')
submitter.close()
os.system("bsub -J ZMatchUpValues -q 1nh < submit.csh")
os.system("sleep 5")

submitter = open('submit.csh','w')
submitter.write('#!/bin/csh\n')
submitter.write('cd '+here)
submitter.write('eval `scramv1 runtime -csh`\n\n')
submitter.write('cd -')
submitter.write('cp '+here +'/MakePlotsSingle_mumu2012_NonEmulatedTriggers.py .\n')
String = "python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy.csv -s /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_MCShapeMuons_2014_08_08_02_14_04/SummaryFiles/ZJetsJBin_scaledown.root -f ZScaleDownValues"+Name
submitter.write(String)
submitter.write('cp *.txt '+here+'/ParallelMuonIntegrals\n')
submitter.close()
os.system("bsub -J ZScaleDownValues -q 1nh < submit.csh")
os.system("sleep 5")


submitter = open('submit.csh','w')
submitter.write('#!/bin/csh\n')
submitter.write('cd '+here)
submitter.write('eval `scramv1 runtime -csh`\n\n')
submitter.write('cd -')
submitter.write('cp '+here +'/MakePlotsSingle_mumu2012_NonEmulatedTriggers.py .\n')
String = "python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy.csv -s /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_MCShapeMuons_2014_08_08_02_14_04/SummaryFiles/ZJetsJBin_scaleup.root -f ZScaleUpValues"+Name
submitter.write(String)
submitter.write('cp *.txt '+here+'/ParallelMuonIntegrals\n')
submitter.close()
os.system("bsub -J ZScaleUpValues -q 1nh < submit.csh")
