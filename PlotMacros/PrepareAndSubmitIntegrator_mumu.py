from ROOT import *
import os
import sys
import math
from time import strftime



for i in range(52):
    Submitter = open('ParallelFiles_mumu/WEIGHTS_CTEQ'+str(i)+'.csh','w') 
    Submitter.write('#!/bin/csh\n')
    Submitter.write('cd /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros\n')
    Submitter.write('eval `scramv1 runtime -csh`\n')
    Submitter.write('cd -\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/ForPDFMakePlotsSingle_mumu2012_NonEmulatedTriggers.py .\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/WeightsAndFilters.py .\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/HistoCreation.py .\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/CMSStyle.py .\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/Selection_mumu_NewQCDStudy_125jetptcut.csv .\n')
    Submitter.write('python ForPDFMakePlotsSingle_mumu2012_NonEmulatedTriggers.py -A WEIGHTS_CTEQ '+str(i)+' -I -i Selection_mumu_NewQCDStudy_125jetptcut.csv -f IntegralOutput \n')
    Submitter.write('cp IntegralOutput.txt /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/ParallelFiles_mumu/IntegralOutputWEIGHTS_CTEQ'+str(i)+'.txt \n')
    Submitter.close()
              
    os.system('bsub -q 1nh -J CountFinalSel_WEIGHTS_CTEQ'+str(i)+' < ParallelFiles_mumu/WEIGHTS_CTEQ'+str(i)+'.csh')

for i in range(100):
    File = open('ParallelFiles_mumu/WEIGHTS_NNPDF'+str(i)+'.py','w') 
    Submitter = open('ParallelFiles_mumu/WEIGHTS_NNPDF'+str(i)+'.csh','w') 
    Submitter.write('#!/bin/csh\n')
    Submitter.write('cd /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros\n')
    Submitter.write('eval `scramv1 runtime -csh`\n')
    Submitter.write('cd -\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/ForPDFMakePlotsSingle_mumu2012_NonEmulatedTriggers.py .\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/WeightsAndFilters.py .\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/HistoCreation.py .\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/CMSStyle.py .\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/Selection_mumu_NewQCDStudy_125jetptcut.csv .\n')
    Submitter.write('python ForPDFMakePlotsSingle_mumu2012_NonEmulatedTriggers.py -A WEIGHTS_NNPDF '+str(i)+' -I -i Selection_mumu_NewQCDStudy_125jetptcut.csv -f IntegralOutput\n')
    Submitter.write('cp IntegralOutput.txt /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/ParallelFiles_mumu/IntegralOutputWEIGHTS_NNPDF'+str(i)+'.txt \n')
    Submitter.close()
                    
    os.system('bsub -q 1nh -J CountFinalSel_WEIGHTS_NNPDF'+str(i)+' < ParallelFiles_mumu/WEIGHTS_NNPDF'+str(i)+'.csh')

for i in range(40):
    Submitter = open('ParallelFiles_mumu/WEIGHTS_MSTW'+str(i)+'.csh','w') 
    Submitter.write('#!/bin/csh\n')
    Submitter.write('cd /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros\n')
    Submitter.write('eval `scramv1 runtime -csh`\n')
    Submitter.write('cd -\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/ForPDFMakePlotsSingle_mumu2012_NonEmulatedTriggers.py .\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/WeightsAndFilters.py .\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/HistoCreation.py .\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/CMSStyle.py .\n')
    Submitter.write('cp  /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/Selection_mumu_NewQCDStudy_125jetptcut.csv .\n')
    Submitter.write('python ForPDFMakePlotsSingle_mumu2012_NonEmulatedTriggers.py -A WEIGHTS_MSTW '+str(i)+' -I -i Selection_mumu_NewQCDStudy_125jetptcut.csv -f IntegralOutput\n')
    Submitter.write('cp IntegralOutput.txt /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/ParallelFiles_mumu/IntegralOutputWEIGHTS_MSTW'+str(i)+'.txt \n')
    Submitter.close()
  
    os.system('bsub -q 1nh -J CountFinalSel_WEIGHTS_MSTW'+str(i)+' < ParallelFiles_mumu/WEIGHTS_MSTW'+str(i)+'.csh')
