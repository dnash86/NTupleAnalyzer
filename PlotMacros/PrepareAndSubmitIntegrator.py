from ROOT import *
import os
import sys
import math
from time import strftime




FileTemplate = os.popen('cat ForPDFUncertainties.py').readlines()

for i in range(52):
    Submitter = open('ParallelFiles2/WEIGHTS_CTEQ'+str(i)+'.csh','w') 
    Submitter.write('#!/bin/csh\n')
    Submitter.write('cd /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros\n')
    Submitter.write('eval `scramv1 runtime -csh`\n')
    Submitter.write('cd -\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/ForPDFMakePlotsSingle_ee2012_NewQCD_NonEmulatedTriggers.py .\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/WeightsAndFilters.py .\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/CMSStyle.py .\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/HistoCreation.py .\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/Selection_ee_NewQCDStudy_125jetptcut.csv .\n')
    Submitter.write('python ForPDFMakePlotsSingle_ee2012_NewQCD_NonEmulatedTriggers.py -A WEIGHTS_CTEQ '+str(i)+' -I -i Selection_ee_NewQCDStudy_125jetptcut.csv -f IntegralOutput\n')
    Submitter.write('cp IntegralOutput.txt /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/ParallelFiles2/IntegralOutputWEIGHTS_CTEQ'+str(i)+'.txt \n')
    Submitter.close()
   
    os.system('bsub -q 8nh -J CountFinalSel_WEIGHTS_CTEQ'+str(i)+' < ParallelFiles2/WEIGHTS_CTEQ'+str(i)+'.csh')

for i in range(100):
    File = open('ParallelFiles2/WEIGHTS_NNPDF'+str(i)+'.csh','w') 
    Submitter = open('ParallelFiles2/WEIGHTS_NNPDF'+str(i)+'.csh','w') 
    Submitter.write('#!/bin/csh\n')
    Submitter.write('cd /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros\n')
    Submitter.write('eval `scramv1 runtime -csh`\n')
    Submitter.write('cd -\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/ForPDFMakePlotsSingle_ee2012_NewQCD_NonEmulatedTriggers.py .\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/WeightsAndFilters.py .\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/HistoCreation.py .\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/CMSStyle.py .\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/Selection_ee_NewQCDStudy_125jetptcut.csv .\n')
    Submitter.write('python ForPDFMakePlotsSingle_ee2012_NewQCD_NonEmulatedTriggers.py -A WEIGHTS_NNPDF '+str(i)+' -I -i Selection_ee_NewQCDStudy_125jetptcut.csv -f IntegralOutput\n')
    Submitter.write('cp IntegralOutput.txt /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/ParallelFiles2/IntegralOutputWEIGHTS_NNPDF'+str(i)+'.txt \n')
    Submitter.close()
     
    os.system('bsub -q 8nh -J CountFinalSel_WEIGHTS_NNPDF'+str(i)+' < ParallelFiles2/WEIGHTS_NNPDF'+str(i)+'.csh')

for i in range(40):
    Submitter = open('ParallelFiles2/WEIGHTS_MSTW'+str(i)+'.csh','w') 
    Submitter.write('#!/bin/csh\n')
    Submitter.write('cd /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros\n')
    Submitter.write('eval `scramv1 runtime -csh`\n')
    Submitter.write('cd -\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/ForPDFMakePlotsSingle_ee2012_NewQCD_NonEmulatedTriggers.py .\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/WeightsAndFilters.py .\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/HistoCreation.py .\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/CMSStyle.py .\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/Selection_ee_NewQCDStudy_125jetptcut.csv .\n')
    Submitter.write('python ForPDFMakePlotsSingle_ee2012_NewQCD_NonEmulatedTriggers.py -A WEIGHTS_MSTW '+str(i)+' -I -i Selection_ee_NewQCDStudy_125jetptcut.csv -f IntegralOutput\n')
    Submitter.write('cp IntegralOutput.txt /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/ParallelFiles2/IntegralOutputWEIGHTS_MSTW'+str(i)+'.txt \n')
    Submitter.close()

    os.system('bsub -q 8nh -J CountFinalSel_WEIGHTS_MSTW'+str(i)+' < ParallelFiles2/WEIGHTS_MSTW'+str(i)+'.csh')
