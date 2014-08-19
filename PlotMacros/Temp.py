from ROOT import *
import os
import sys
import math
from time import strftime


for i in range(40):
    File = open('ParallelFiles_mumu/WEIGHTS_MSTW'+str(i)+'.py','w') 
    Submitter = open('ParallelFiles_mumu/WEIGHTS_MSTW'+str(i)+'.csh','w') 
    Submitter.write('#!/bin/csh\n')
    Submitter.write('cd /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros\n')
    Submitter.write('eval `scramv1 runtime -csh`\n')
    Submitter.write('cd -\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/MakePlotsSingle_mumu2012_NonEmulatedTriggers.py .\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/WeightsAndFilters.py .\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/HistoCreation.py .\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/Selection_mumu_NewQCDStudy_125jetptcut.csv .\n')
    Submitter.write('python WEIGHTS_MSTW'+str(i)+'.py -A WEIGHTS_MSTW['+str(i)+'] -P -i Selection_mumu_NewQCDStudy_125jetptcut.csv -f IntegralOutput.txt\n')
    Submitter.write('cp IntegralOutput.txt /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/ParallelFiles_mumu/IntegralOutputWEIGHTS_MSTW'+str(i)+'.txt \n')
    Submitter.close()

    os.system('bsub -q 8nh -J CountFinalSel_WEIGHTS_MSTW'+str(i)+' < ParallelFilesPresel_mumu/WEIGHTS_MSTW'+str(i)+'.csh')
