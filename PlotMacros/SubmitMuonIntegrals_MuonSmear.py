from ROOT import *
import os
import sys
import math
from time import strftime

Name='_Muon_newQCD'

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
submitter.write('cp '+here +'/Selection_mumu_NewQCDStudy_125jetptcut.csv .\n')
submitter.write('cp '+here +'/MakePlotsSingle_mumu2012_NonEmulatedTriggers.py .\n')
String = "python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy_125jetptcut.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_Oct13_FixedGenMass_Systematics__MuScaleDown_2014_10_14_15_09_30/SummaryFiles -f MuDownValues"+Name+'\n'
submitter.write(String)
submitter.write('cp *.txt '+here+'/ParallelMuonIntegrals_MuonSyst2\n')
submitter.close()
os.system("bsub -J MuDownValues -q 1nh < submit.csh")
os.system("sleep 5")

submitter = open('submit.csh','w')
submitter.write('#!/bin/csh\n')
submitter.write('cd '+here+'\n')
submitter.write('eval `scramv1 runtime -csh`\n\n')
submitter.write('cd -\n')
submitter.write('cp '+here +'/CMSStyle.py .\n')
submitter.write('cp '+here +'/WeightsAndFilters.py .\n')
submitter.write('cp '+here +'/HistoCreation.py .\n')
submitter.write('cp '+here +'/Selection_mumu_NewQCDStudy_125jetptcut.csv .\n')
submitter.write('cp '+here +'/MakePlotsSingle_mumu2012_NonEmulatedTriggers.py .\n')
String = "python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy_125jetptcut.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_Oct13_FixedGenMass_Systematics__MuScaleUp_2014_10_13_20_47_09/SummaryFiles -f MuUpValues"+Name+'\n'
submitter.write(String)
submitter.write('cp *.txt '+here+'/ParallelMuonIntegrals_MuonSyst2\n')
submitter.close()
os.system("bsub -J MuUpValues -q 1nh < submit.csh")
os.system("sleep 5")

submitter = open('submit.csh','w')
submitter.write('#!/bin/csh\n')
submitter.write('cd '+here+'\n')
submitter.write('eval `scramv1 runtime -csh`\n\n')
submitter.write('cd -\n')
submitter.write('cp '+here +'/CMSStyle.py .\n')
submitter.write('cp '+here +'/WeightsAndFilters.py .\n')
submitter.write('cp '+here +'/HistoCreation.py .\n')
submitter.write('cp '+here +'/Selection_mumu_NewQCDStudy_125jetptcut.csv .\n')
submitter.write('cp '+here +'/MakePlotsSingle_mumu2012_NonEmulatedTriggers.py .\n')
String = "python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -I -i Selection_mumu_NewQCDStudy_125jetptcut.csv -e /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_Oct13_FixedGenMass_Systematics__MuSmear_2014_10_15_06_59_08/SummaryFiles -f MuSmearValues"+Name+'\n'
submitter.write(String)
submitter.write('cp *.txt '+here+'/ParallelMuonIntegrals_MuonSyst2\n')
submitter.close()
os.system("bsub -J MuSmearValues -q 1nh < submit.csh")
os.system("sleep 5")
