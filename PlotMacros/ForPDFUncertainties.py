from ROOT import *
import os
import sys
import math
from time import strftime


#from ProcessHistos import *

#from CMSStyle import *
from HistoCreation import *
from WeightsAndFilters import *

#################################
#   Loading trees...


#Files_emu = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_Foremu_TTBarReRun_2014_03_05_13_19_56/SummaryFiles'
Files_emu = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_Foremu_EMu_ReRun_2014_04_30_22_04_51/SummaryFiles'
#Files_ee = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_ReRunOldNTuples_2014_02_25_21_20_15/SummaryFiles'
#Files_ee = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_ReRun_OrderFixed_2014_05_06_15_52_31/SummaryFiles'

##  Less skimmed samples
#Files_ee='/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_ElectronSmallerSkim_2014_06_10_01_46_29/SummaryFiles/'
#Files_ee='/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_FixElectronEta_2014_06_25_01_52_27/SummaryFiles'
#Files_ee='/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_FixBEFilter_2014_06_24_00_50_34/SummaryFiles'
Files_qcd = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ForQCDStudy_QCDReRunEdmundCS_NoPtJetElimination_2014_02_07_21_29_51/SummaryFiles'
#Files_qcd = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ForQCDStudy_QCDVeryStrict_2014_04_13_21_31_02/SummaryFiles'

OptimizationFile = '/afs/cern.ch/user/d/dnash/CMSSW_5_0_0/src/NTupleAnalyzer/Optimization/Ele_ValuesSSB.txt'

Files_ee = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_PDF_PDFRunElectrons_2014_06_24_00_50_55/SummaryFiles'
TreeName = 'PhysicalVariables'


Trigger = '*(CurrentDoubleElePass>0.5)'
Trigger_emu = '*(HLTMu40TriggerPass>0.5)'


#################################
# Parsing arguments

a=sys.argv
InputCuts=False
UseOutputDir=False
PlotHistos=False
Test=False
IntegrateOnly=False
PreselIntegrateOnly=False
FileLocation='blank'
CollectOnly=False
for n in range(len(a)):
    if a[n]=='-i' or a[n]=='--input_cutcard':
        InputCuts=True
        ifile=a[n+1]
        print "Will use the input cut card for selection"
    if a[n]=='-p' or a[n]=='--plot':
        PlotHistos=True
    if a[n]=='-I' or a[n]=='--integrate':
        IntegrateOnly=True
    if a[n]=='-P' or a[n]=='--presel_integrate':
        PreselIntegrateOnly=True
    if a[n]=='-f' or a[n]=='--final_selection_cutcard':
        fselfile=a[n+1]
    if a[n]=='-o' or a[n]=='--output_dir':
        OutputDir=a[n+1]
        UseOutputDir=True
    if a[n]=='-t' or a[n]=='--test':
        Test=True
    if a[n]=='-e' or a[n]=='--errors':
        FileLocation = a[n+1]
    if a[n]=='-c' or a[n]=='--CollectOnly':
        CollectOnly=True
    
        #for f in os.popen('cmsLs '+FileLocation+'| grep ".root" | gawk \'{print $NF}\' | gawk -F "/" \'{print $NF}\'').readlines():
            
        #exec(f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+FileLocation+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
if not InputCuts:
    print "No input cut card, will use standard selection"




print "Loading..."
print Files_ee
if FileLocation=='blank':
    for f in os.popen('cmsLs '+Files_ee+' | grep -v Data | grep ".root" | gawk \'{print $NF}\' | gawk -F "/" \'{print $NF}\'').readlines():
        #print " = TFile.Open(\"root://eoscms//eos/cms/"+Files_ee+"/"+f.replace("\n","")
        exec(f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_ee+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
        #print f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_ee+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")"
        #print f.replace('-','_').replace(".root\n","")
else:
    print "DoublePhotonData= TFile.Open(\"root://eoscms//eos/cms/"+Files_ee+"/"+"DoublePhotonData.root"+"\")"+".Get(\""+TreeName+"\")"
    exec("DoublePhotonData= TFile.Open(\"root://eoscms//eos/cms/"+Files_ee+"/"+"DoublePhotonData.root"+"\")"+".Get(\""+TreeName+"\")")   
    for f in os.popen('cmsLs '+FileLocation+'| grep ".root" | gawk \'{print $NF}\' | gawk -F "/" \'{print $NF}\'').readlines():
        exec(f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+FileLocation+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")       
    
for f in os.popen('cmsLs '+Files_emu+'| grep ".root" | grep -v LQTo | gawk \'{print $NF}\' | gawk -F "/" \'{print $NF}\'').readlines():
    exec('emu_'+f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_emu+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
    print 'emu_'+f.replace('-','_').replace(".root\n","")

for f in os.popen('cmsLs '+Files_qcd+'| grep ".root" | grep -v LQTo | gawk \'{print $NF}\' | gawk -F "/" \'{print $NF}\'').readlines():
    exec('qcd_'+f.replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_qcd+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
    #print 'qcd_'+f.replace('-','_').replace(".root\n","")
print "...done loading"

###############################################

            

def collect():
    FileList = os.popen('ls ParallelFiles/*NNPDF*.txt').readlines()
    SmallestBackgroundEventCount = [99999.]*113
    SmallestSignalEventCount = [99999.]*113
    LargestBackgroundEventCount = [0]*113
    LargestSignalEventCount = [0]*113
    for line in FileList:
        CurrentFile = os.popen('cat '+line.replace('\n','')).readlines()
        #print CurrentFile
        for i in range(len(CurrentFile)):
            Background = float(CurrentFile[i].replace('\n','').split(',')[0])
            Signal = float(CurrentFile[i].replace('\n','').split(',')[1])

            if Background > LargestBackgroundEventCount[i]:
                print LargestBackgroundEventCount[i]
                LargestBackgroundEventCount[i]=Background
            if Signal > LargestSignalEventCount[i]:
                LargestSignalEventCount[i]=Signal

                #print Background + ", " + str(SmallestBackgroundEventCount[i])
            if Background < SmallestBackgroundEventCount[i]:
                SmallestBackgroundEventCount[i]=Background
            if Signal < SmallestSignalEventCount[i]:
                SmallestSignalEventCount[i]=Signal
    for i in range(len(SmallestBackgroundEventCount)):
        print "Range = " +str(SmallestBackgroundEventCount[i])+" - " +str(LargestBackgroundEventCount[i])
    for i in range(len(SmallestSignalEventCount)):
        print "Range = " +str(SmallestSignalEventCount[i])+" - " +str(LargestSignalEventCount[i])

def integrate():
    if InputCuts:
        Selections = GetSelections(ifile)
        Selection = Selections[0]
        Selection_emu = Selections[1]
        Selection_qcd = Selections[2]
    else:
        Selection = '((Pt_HEEPele1>45)*(Pt_HEEPele2>45)*(Pt_pfjet1>45)*(deltaR_HEEPele1ele2>0.3)*((abs(Eta_HEEPele1)<2.1)*(abs(Eta_HEEPele2)<2.1))*(M_HEEPele1ele2>110))*(ST_pf_ee_single> 250)'

        Selection_emu = '((Pt_muon1>45)*(Pt_HEEPele1>45)*(Pt_pfjet1>45)*(deltaR_muon1HEEPele1>0.3)*((abs(Eta_muon1)<2.1)*(abs(Eta_HEEPele1)<2.1))*(M_muon1HEEPele1>110))*(ST_pf_emu_single> 250)'
        
        Selection_qcd = '((Pt_QCDele1>45)*(Pt_QCDele2>45)*(Pt_pfjet1>45)*(deltaR_QCDele1ele2>0.3)*((abs(Eta_QCDele1)<2.1)*(abs(Eta_QCDele2)<2.1))*(M_QCDele1ele2>110))*((Pt_QCDele1+Pt_QCDele2+Pt_pfjet1)>250)'

    

    #Trigger = '*(CurrentDoubleElePass>0.5)'
    #Trigger_emu = '*(HLTMu40TriggerPass>0.5)'
    #Trigger_qcd = '*((SinglePhotonTriggerPass>0.5)*SinglePhotonTriggerPrescale)'

    #Selection +=Trigger
    #Selection_emu +=Trigger_emu
    #Selection_qcd += Trigger     
    
    JustIntegrate=True
    drawSub = False
    use_emu = False
    ttscaler = 0.5942599
    znorm = 0.98580048415651985403
        
    chargebinning=[11,-5,5]

    filetag = "Preselection"
    xtag = " ["+filetag+"]"
    File = open('IntegralOutput.txt','w') 
    for i in range(5):
        if i == 0:
            MassRangeLength = 16
            Coupling = "L-0p2"
        if i == 1:
            MassRangeLength = 16
            Coupling = "L-0p4"
        if i == 2:
            MassRangeLength = 25
            Coupling = "L-0p6"
        if i == 3:
            MassRangeLength = 25
            Coupling = "L-0p8"
        if i == 4:
            MassRangeLength = 31
            Coupling = "L-1p0"

        for x in [(300+100*y) for y in range(MassRangeLength)]:
            lq_choice = "*(LQmass=="+str(x)+")*(LQisCMu==0)*(LQcoupling=="+str( (float)(i+1)/5)+")*(1/1000)"
            AdditionalCut = ""
            #print lq_choice
            #Cuts=os.popen("grep -A 1 "+Coupling+ " /afs/cern.ch/work/d/dnash/CMSSW_5_0_0/src/NTupleAnalyzer/Optimization/Ele_SSB_log2.txt  | grep -A 1 \"Mass = " + str(x) + "\" | grep ST_pf").readline().replace('\n','')
            Cuts=os.popen("grep -A 1 "+Coupling+ " /afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/Ele_SSB_log2.txt  | grep -A 1 \"Mass = " + str(x) + "\" | grep ST_pf").readline().replace('\n','')
            String = DrawHisto(JustIntegrate,lq_choice, Cuts+"*"+Selection+AdditionalCut, Selection_emu+AdditionalCut, Cuts+"*"+Selection_qcd+AdditionalCut, use_emu, drawSub, chargebinning, "Charge_HEEPele1*Charge_HEEPele2", "Charge_HEEPele1*Charge_muon1","Charge_HEEPele1*Charge_HEEPele2", "Combined charge " +xtag, znorm, ttscaler,filetag)
            #print String

            File.write(String+'\n')
    File.close()
            
            

                   
def preselintegrate():
    if InputCuts:
        Selections = GetSelections(ifile)
        Selection = Selections[0]
        Selection_emu = Selections[1]
        Selection_qcd = Selections[2]
    else:
        Selection = '((Pt_HEEPele1>45)*(Pt_HEEPele2>45)*(Pt_pfjet1>45)*(deltaR_HEEPele1ele2>0.3)*((abs(Eta_HEEPele1)<2.1)*(abs(Eta_HEEPele2)<2.1))*(M_HEEPele1ele2>110))*(ST_pf_ee_single> 250)'

        Selection_emu = '((Pt_muon1>45)*(Pt_HEEPele1>45)*(Pt_pfjet1>45)*(deltaR_muon1HEEPele1>0.3)*((abs(Eta_muon1)<2.1)*(abs(Eta_HEEPele1)<2.1))*(M_muon1HEEPele1>110))*(ST_pf_emu_single> 250)'
        
        Selection_qcd = '((Pt_QCDele1>45)*(Pt_QCDele2>45)*(Pt_pfjet1>45)*(deltaR_QCDele1ele2>0.3)*((abs(Eta_QCDele1)<2.1)*(abs(Eta_QCDele2)<2.1))*(M_QCDele1ele2>110))*((Pt_QCDele1+Pt_QCDele2+Pt_pfjet1)>250)'

    

    #Trigger = '*(CurrentDoubleElePass>0.5)'
    #Trigger_emu = '*(HLTMu40TriggerPass>0.5)'
    #Trigger_qcd = '*((SinglePhotonTriggerPass>0.5)*SinglePhotonTriggerPrescale)'

    #Selection +=Trigger
    #Selection_emu +=Trigger_emu
    #Selection_qcd += Trigger     
    
    JustIntegrate=True
    drawSub = False
    use_emu = False
    ttscaler = 0.5942599
    znorm = 0.98580048415651985403
        
    chargebinning=[11,-5,5]

    filetag = "Preselection"
    xtag = " ["+filetag+"]"

    for i in range(5):
        if i == 0:
            MassRangeLength = 16
            Coupling = "L-0p2"
        if i == 1:
            MassRangeLength = 16
            Coupling = "L-0p4"
        if i == 2:
            MassRangeLength = 25
            Coupling = "L-0p6"
        if i == 3:
            MassRangeLength = 25
            Coupling = "L-0p8"
        if i == 4:
            MassRangeLength = 31
            Coupling = "L-1p0"

        for x in [(300+100*y) for y in range(MassRangeLength)]:
            lq_choice = "*(LQmass=="+str(x)+")*(LQisCMu==0)*(LQcoupling=="+str( (float)(i+1)/5)+")*(1/1000)"
            AdditionalCut = ""
            Cuts="1.0"
            String = DrawHisto(JustIntegrate,lq_choice, Cuts+"*"+Selection+AdditionalCut, Selection_emu+AdditionalCut, Cuts+"*"+Selection_qcd+AdditionalCut, use_emu, drawSub, chargebinning, "Charge_HEEPele1*Charge_HEEPele2", "Charge_HEEPele1*Charge_muon1","Charge_HEEPele1*Charge_HEEPele2", "Combined charge " +xtag, znorm, ttscaler,filetag)
            print String
            File = open('IntegralOutput.txt','a') 
            File.write(String+'\n')
            File.close()
            
            

                   
    
    
def DrawHisto(JustIntegrate,lq_choice, selection, emuselection, qcdselection, use_emu, drawSub, binning, variable, variable_emu, variable_qcd, xlabel,zscale,ttscaler,tag):
    #SetStyle()
    channel = "ee"
    Luminosity = "19600"

    MaxRescaler=10.
    if "delta" in variable:
        MaxRescaler=10000.
    # Set canvases
    if drawSub:
        c1 = TCanvas("c1","",800,800)
        pad1 = TPad("pad1","The pad 60% of the height",0.0,0.4,1.0,1.0,0)
        pad2 = TPad("pad2","The pad 20% of the height",0.0,0.2,1.0,0.4,0)
        pad2r = TPad("pad2r","The ptad 20% of the height",0.0,0.0,1.0,0.2,0)
        pad1.Draw()
        pad2.Draw()
        pad2r.Draw()
    else:
        c1 = TCanvas("c1","",800,480)
        pad1 = TPad("pad1","The pad 60% of the height",0.0,0.0,1.0,1.0,0)	
        pad1.Draw()
        
    pad1.cd()
    pad1.SetLogy()
    
    # Set gStyle
    gStyle.SetOptLogy()
    gStyle.SetOptStat(0)
    

    #Make the label
    Label=[xlabel,"Number of events"]
    
    #Set the style for each dataset   Format:  FillStyle,MarkerStyle,MarkerSize,LineWidth,Colors
    DataRecoStyle=[0,21,0.0,2,1]
    WStackStyle=[3007,21,.00001,2,9]
    TTStackStyle=[3005,21,.00001,2,4]
    ZStackStyle=[3004,21,.00001,2,2]
    DiBosonStackStyle=[3006,21,.00001,2,9]
    StopStackStyle=[3006,21,.00001,2,3]
    QCDStackStyle=[3006,21,.00001,2,3]
    GJetsStackStyle=[3009,21,.00001,2,5]

    SignalStyle=[0,22,0.7,3,1]

    ### Make the plots
    
    #print selection
    h_Signal=MakeHisto('h_Signal','LQToUE_Single_L_0p2',LQToUE_Single_L_0p2,variable,binning,selection+DoubleENonEmulatedTrigger+LumiAndPU+Filters+lq_choice,SignalStyle,Label)
    h_LQToUE_Single_L0p4=MakeHisto('h_LQToUE_Single_L0p4','LQToUE_Single_L0p4',LQToUE_Single_L_0p4,variable,binning,selection+DoubleENonEmulatedTrigger+LumiAndPU+Filters+lq_choice,SignalStyle,Label)
    h_Signal.Add(h_LQToUE_Single_L0p4)
    h_LQToUE_Single_L0p6=MakeHisto('h_LQToUE_Single_L0p6','LQToUE_Single_L0p6',LQToUE_Single_L_0p6,variable,binning,selection+DoubleENonEmulatedTrigger+LumiAndPU+Filters+lq_choice,SignalStyle,Label)
    h_Signal.Add(h_LQToUE_Single_L0p6)
    h_LQToUE_Single_L0p8=MakeHisto('h_LQToUE_Single_L0p8','LQToUE_Single_L0p8',LQToUE_Single_L_0p8,variable,binning,selection+DoubleENonEmulatedTrigger+LumiAndPU+Filters+lq_choice,SignalStyle,Label)
    h_Signal.Add(h_LQToUE_Single_L0p8)
    h_LQToUE_Single_L1p0=MakeHisto('h_LQToUE_Single_L1p0','LQToUE_Single_L1p0',LQToUE_Single_L_1p0,variable,binning,selection+DoubleENonEmulatedTrigger+LumiAndPU+Filters+lq_choice,SignalStyle,Label)
    h_Signal.Add(h_LQToUE_Single_L1p0)

    #h_Data=MakeHisto('h_Data','Data',DoublePhotonData,variable,binning,selection+Filters,DataRecoStyle,Label)

    h_WJets=MakeHisto('h_WJets','W+Jets',WJetsJBin,variable,binning,selection+DoubleENonEmulatedTrigger+LumiAndPU+Filters,WStackStyle,Label)
    h_DiBoson=MakeHisto('h_DiBoson','DiBoson',DiBoson,variable,binning,selection+DoubleENonEmulatedTrigger+LumiAndPU+Filters,DiBosonStackStyle,Label)
    h_SingleTop=MakeHisto('h_SingleTop','SingleTop',SingleTop,variable,binning,selection+DoubleENonEmulatedTrigger+LumiAndPU+Filters,StopStackStyle,Label)    

    h_ZJets=MakeHisto('h_ZJets','Z+Jets',ZJetsJBin,variable,binning,selection+'*('+str(zscale)+')'+DoubleENonEmulatedTrigger+LumiAndPU+Filters,ZStackStyle,Label)
    #print "Made the normal plots"

    if use_emu:
        h_TTBar=MakeHisto('h_TTBar','t#bar{t}',emu_SingleMuData,variable_emu,binning,Trigger_emu+emuselection+Filters,TTStackStyle,Label)
        h_emu_WJets=MakeHisto('h_emu_WJets','W+Jets',emu_WJetsJBin,variable_emu,binning,emuselection+SingleMuNonEmulatedTrigger+LumiAndPU+Filters,TTStackStyle,Label)
        h_emu_DiBoson=MakeHisto('h_emu_DiBoson','DiBoson',emu_DiBoson,variable_emu,binning,emuselection+SingleMuNonEmulatedTrigger+LumiAndPU+Filters,TTStackStyle,Label)
        h_emu_ZJets=MakeHisto('h_emu_ZJets','Z+Jets',emu_ZJetsJBin,variable_emu,binning,emuselection+SingleMuNonEmulatedTrigger+LumiAndPU+Filters,TTStackStyle,Label)
        h_emu_SingleTop=MakeHisto('h_emu_SingleTop','SingleTop',emu_SingleTop,variable_emu,binning,emuselection+SingleMuNonEmulatedTrigger+LumiAndPU+Filters,TTStackStyle,Label)
        #h_emu_GJets=MakeHisto('h_Gjets','t#bar{t}',emu_Gjets,variable,binning,tt_sel_weight,GJetsStackStyle,Label)

        h_TTBar.Add(h_emu_WJets,-1)
        h_TTBar.Add(h_emu_DiBoson,-1)
        h_TTBar.Add(h_emu_ZJets,-1)
        h_TTBar.Add(h_emu_SingleTop,-1)

        h_TTBar.Scale(ttscaler)
    else:
        h_TTBar=MakeHisto('h_TTBar','t#bar{t}',TTBarDBin,variable,binning,selection+DoubleENonEmulatedTrigger+LumiAndPU+Filters,TTStackStyle,Label)

    #print "Made the ttbar plots"

    #If the channel is ee, include G Jets background and the QCD fake rate sample
    h_GJets=MakeHisto('h_GJets','#gamma+Jets',Gjets,variable,binning,selection+DoubleENonEmulatedTrigger+LumiAndPU+Filters,GJetsStackStyle,Label)
    if (zscale != 1.00):

        #if (zscale != 1.00):
        if False:
            h_QCD=MakeHisto('h_QCD','Data',DoublePhotonData,variable,binning,qcdselection+Filters,QCDStackStyle,Label)

            h_qcd_WJets=MakeHisto('h_qcd_WJets','W+Jets',WJetsJBin,variable,binning,qcdselection+DoubleENonEmulatedTrigger+LumiAndPU+Filters,WStackStyle,Label)
            h_qcd_DiBoson=MakeHisto('h_qcd_DiBoson','DiBoson',DiBoson,variable,binning,qcdselection+DoubleENonEmulatedTrigger+LumiAndPU+Filters,DiBosonStackStyle,Label)
            h_qcd_ZJets=MakeHisto('h_qcd_ZJets','Z+Jets',ZJetsJBin,variable,binning,qcdselection+DoubleENonEmulatedTrigger+LumiAndPU+Filters,ZStackStyle,Label)
            h_qcd_SingleTop=MakeHisto('h_qcd_SingleTop','SingleTop',SingleTop,variable,binning,qcdselection+DoubleENonEmulatedTrigger+LumiAndPU+Filters,StopStackStyle,Label)
            h_qcd_GJets=MakeHisto('h_qcd_Gjets','#gamma+Jets',Gjets,variable,binning,qcdselection+DoubleENonEmulatedTrigger+LumiAndPU+Filters,GJetsStackStyle,Label)
            h_qcd_TTBar=MakeHisto('h_qcd_TTBar','t#bar{t}',TTBarDBin,variable,binning,qcdselection+DoubleENonEmulatedTrigger+LumiAndPU+Filters,TTStackStyle,Label)

            #print "QCD Integral = " + str(h_QCD.Integral())
            h_QCD.Add(h_qcd_WJets,-1)
            #print "QCD Integral = " + str(h_QCD.Integral())
            h_QCD.Add(h_qcd_DiBoson,-1)
            #print "QCD Integral = " + str(h_QCD.Integral())
            h_QCD.Add(h_qcd_ZJets,-1)
            #print "QCD Integral = " + str(h_QCD.Integral())
            h_QCD.Add(h_qcd_SingleTop,-1)
            #print "QCD Integral = " + str(h_QCD.Integral())
            h_QCD.Add(h_qcd_GJets,-1)
            #print "QCD Integral = " + str(h_QCD.Integral())
            h_QCD.Add(h_qcd_TTBar,-1)
            #print "QCD Integral = " + str(h_QCD.Integral())
            
            nBins = binning[0]

    if JustIntegrate:
        return str(h_TTBar.Integral()+h_ZJets.Integral()+h_DiBoson.Integral()+h_SingleTop.Integral()+h_WJets.Integral()+h_GJets.Integral()) + ","+str(h_Signal.Integral())



def GetSelections(ifile):
    import csv
    csvfile=open(ifile,'r')
    WriteToSelection=False
    WriteToSelection_emu=False
    WriteToSelection_qcd=False
    Selections=['','','']
    for row in csv.reader(csvfile):
        print row
        if row[0] == "#Selection":
            WriteToSelection=True
            WriteToSelection_emu=False
            WriteToSelection_qcd=False
        if row[0] == "#Selection_emu":
            WriteToSelection_emu=True
            WriteToSelection=False
            WriteToSelection_qcd=False
        if row[0] == "#Selection_qcd":
            WriteToSelection_qcd=True
            WriteToSelection_emu=False
            WriteToSelection=False
        if (row[0][0]!='#') and (len(row)==3):
            if WriteToSelection:
                if Selections[0]!='': Selections[0] += '*'
                Selections[0] += '('+row[0]+row[1]+row[2]+')'
            if WriteToSelection_emu:
                if Selections[1]!='': Selections[1] += '*'
                Selections[1] += '('+row[0]+row[1]+row[2]+')'
            if WriteToSelection_qcd:
                if Selections[2]!='': Selections[2] += '*'
                Selections[2] += '('+row[0]+row[1]+row[2]+')'
    print Selections
    return Selections


def main():
    if PlotHistos:
        plot()
    if IntegrateOnly:
        integrate()
    if PreselIntegrateOnly:
        preselintegrate()
    if CollectOnly:
        collect()

main()
