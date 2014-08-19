from ROOT import *
import os
import sys
import math
from time import strftime

Name='_Muon_newQCD'

here= os.popen('pwd').readlines()[0].replace('\n','')
submitter = open('submit.csh','w')

submitter.write('#!/bin/csh\n')
submitter.write('cd '+here+'\n')
submitter.write('eval `scramv1 runtime -csh`\n\n')
submitter.write('cd -\n')
submitter.write('cp '+here +'/CMSStyle.py .\n')
submitter.write('cp '+here +'/WeightsAndFilters.py .\n')
submitter.write('cp '+here +'/HistoCreation.py .\n')
submitter.write('cp '+here +'/Selection_mumu_NewQCDStudy_justz.csv .\n')
submitter.write('cp '+here +'/MakePlotsSingle_mumu2012_NonEmulatedTriggers.py .\n')
String = "python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -P -i Selection_mumu_NewQCDStudy_justz.csv -f CentralValues"+Name+"\n"
submitter.write(String)
submitter.write('cp *.txt '+here+'/MuonIntegralsJustZ\n')
submitter.close()
os.system("bsub -J CentralValues -q 1nh < submit.csh")
os.system("sleep 5")

submitter = open('submit.csh','w')
submitter.write('#!/bin/csh\n')
submitter.write('cd '+here+'\n')
submitter.write('eval `scramv1 runtime -csh`\n\n')
submitter.write('cd -\n')
submitter.write('cp '+here +'/CMSStyle.py .\n')
submitter.write('cp '+here +'/WeightsAndFilters.py .\n')
submitter.write('cp '+here +'/HistoCreation.py .\n')
submitter.write('cp '+here +'/Selection_mumu_NewQCDStudy_justz.csv .\n')
submitter.write('cp '+here +'/MakePlotsSingle_mumu2012_NonEmulatedTriggers.py .\n')
String = "python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -P -i Selection_mumu_NewQCDStudy_justz.csv -s /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_MCShapeMuons_2014_08_08_02_14_04/SummaryFiles/ZJetsJBin_matchingdown.root -f ZMatchDownValues"+Name+'\n'
submitter.write(String)
submitter.write('cp *.txt '+here+'/MuonIntegralsJustZ\n')
submitter.close()
os.system("bsub -J ZMatchDownValues -q 1nh < submit.csh")
os.system("sleep 5")

submitter = open('submit.csh','w')
submitter.write('#!/bin/csh\n')
submitter.write('cd '+here+'\n')
submitter.write('eval `scramv1 runtime -csh`\n\n')
submitter.write('cd -\n')
submitter.write('cp '+here +'/CMSStyle.py .\n')
submitter.write('cp '+here +'/WeightsAndFilters.py .\n')
submitter.write('cp '+here +'/HistoCreation.py .\n')
submitter.write('cp '+here +'/Selection_mumu_NewQCDStudy_justz.csv .\n')
submitter.write('cp '+here +'/MakePlotsSingle_mumu2012_NonEmulatedTriggers.py .\n')
String = "python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -P -i Selection_mumu_NewQCDStudy_justz.csv -s /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_MCShapeMuons_2014_08_08_02_14_04/SummaryFiles/ZJetsJBin_matchingup.root -f ZMatchUpValues"+Name+'\n'
submitter.write(String)
submitter.write('cp *.txt '+here+'/MuonIntegralsJustZ\n')
submitter.close()
os.system("bsub -J ZMatchUpValues -q 1nh < submit.csh")
os.system("sleep 5")

submitter = open('submit.csh','w')
submitter.write('#!/bin/csh\n')
submitter.write('cd '+here+'\n')
submitter.write('eval `scramv1 runtime -csh`\n\n')
submitter.write('cd -\n')
submitter.write('cp '+here +'/CMSStyle.py .\n')
submitter.write('cp '+here +'/WeightsAndFilters.py .\n')
submitter.write('cp '+here +'/HistoCreation.py .\n')
submitter.write('cp '+here +'/Selection_mumu_NewQCDStudy_justz.csv .\n')
submitter.write('cp '+here +'/MakePlotsSingle_mumu2012_NonEmulatedTriggers.py .\n')
String = "python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -P -i Selection_mumu_NewQCDStudy_justz.csv -s /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_MCShapeMuons_2014_08_08_02_14_04/SummaryFiles/ZJetsJBin_scaledown.root -f ZScaleDownValues"+Name+'\n'
submitter.write(String)
submitter.write('cp *.txt '+here+'/MuonIntegralsJustZ\n')
submitter.close()
os.system("bsub -J ZScaleDownValues -q 1nh < submit.csh")
os.system("sleep 5")


submitter = open('submit.csh','w')
submitter.write('#!/bin/csh\n')
submitter.write('cd '+here+'\n')
submitter.write('eval `scramv1 runtime -csh`\n\n')
submitter.write('cd -\n')
submitter.write('cp '+here +'/CMSStyle.py .\n')
submitter.write('cp '+here +'/WeightsAndFilters.py .\n')
submitter.write('cp '+here +'/HistoCreation.py .\n')
submitter.write('cp '+here +'/Selection_mumu_NewQCDStudy_justz.csv .\n')
submitter.write('cp '+here +'/MakePlotsSingle_mumu2012_NonEmulatedTriggers.py .\n')
String = "python MakePlotsSingle_mumu2012_NonEmulatedTriggers.py -P -i Selection_mumu_NewQCDStudy_justz.csv -s /store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_MCShapeMuons_2014_08_08_02_14_04/SummaryFiles/ZJetsJBin_scaleup.root -f ZScaleUpValues"+Name+'\n'
submitter.write(String)
submitter.write('cp *.txt '+here+'/MuonIntegralsJustZ\n')
submitter.close()
os.system("bsub -J ZScaleUpValues -q 1nh < submit.csh")
