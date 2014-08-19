from ROOT import *
import os
import sys
import math
from time import strftime


#from ProcessHistos import *

from CMSStyle import *
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

Files_qcd = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ForQCDStudy_QCDReRunEdmundCS_NoPtJetElimination_2014_02_07_21_29_51/SummaryFiles'
#Files_qcd = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ForQCDStudy_QCDVeryStrict_2014_04_13_21_31_02/SummaryFiles'


Files_ee='/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_PDF_PDFRunElectrons_2014_06_24_00_50_55/SummaryFiles/'
TreeName = 'PhysicalVariables'


#################################
# Parsing arguments

a=sys.argv
InputCuts=False
UseOutputDir=False
PlotHistos=False
Test=False
IntegrateOnly=False
FileLocation='blank'
for n in range(len(a)):
    if a[n]=='-i' or a[n]=='--input_cutcard':
        InputCuts=True
        ifile=a[n+1]
        print "Will use the input cut card for selection"
    

    if a[n]=='-f' or a[n]=='--final_selection_cutcard':
        fselfile=a[n+1]
    if a[n]=='-o' or a[n]=='--output_dir':
        OutputDir=a[n+1]
        UseOutputDir=True
    if a[n]=='-t' or a[n]=='--test':
        Test=True
    if a[n]=='-e' or a[n]=='--errors':
        FileLocation = a[n+1]
        for f in os.popen('cmsLs '+FileLocation+'| grep ".root" | gawk \'{print $NF}\' | gawk -F "/" \'{print $NF}\'').readlines():
            
            exec(f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+FileLocation+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
if not InputCuts:
    print "No input cut card, will use standard selection"



#exec("ZJetsJBin = TFile.Open(\"/tmp/dnash/NTupleAnalyzer_V00_02_06_David_2012_PDF_PDFRunElectrons_2014_06_18_16_26_14/NTupleAnalyzer_V00_02_06_David_2012_PDF_DY1JetsToLL_Bin4part8of8_PDFRunElectrons.root\")"+".Get(\""+TreeName+"\")")



print "Loading..."
print Files_ee
for f in os.popen('cmsLs '+Files_ee+'| grep ".root" | gawk \'{print $NF}\' | gawk -F "/" \'{print $NF}\'').readlines():
        #print " = TFile.Open(\"root://eoscms//eos/cms/"+Files_ee+"/"+f.replace("\n","")
        exec(f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_ee+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
###############################################

    
def DoIntegrals(Type,JustIntegrate,lq_choice, selection, emuselection, qcdselection, use_emu, drawSub, variable, variable_emu, variable_qcd, xlabel,zscale,ttscaler):
    #Make the label
    Label=[xlabel,"Number of events"]
    binning = [5,0,500]    
    Luminosity = "19600"
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

    if "LQ" in Type:
        h_Signal=MakeHisto('h_Signal','LQToUE_Single_L_0p2',LQToUE_Single_L_0p2,variable,binning,selection+Filters+LumiAndPU+lq_choice,SignalStyle,Label)
        h_LQToUE_Single_L0p4=MakeHisto('h_LQToUE_Single_L0p4','LQToUE_Single_L0p4',LQToUE_Single_L_0p4,variable,binning,selection+Filters+LumiAndPU+lq_choice,SignalStyle,Label)
        h_Signal.Add(h_LQToUE_Single_L0p4)
        h_LQToUE_Single_L0p6=MakeHisto('h_LQToUE_Single_L0p6','LQToUE_Single_L0p6',LQToUE_Single_L_0p6,variable,binning,selection+Filters+LumiAndPU+lq_choice,SignalStyle,Label)
        h_Signal.Add(h_LQToUE_Single_L0p6)
        h_LQToUE_Single_L0p8=MakeHisto('h_LQToUE_Single_L0p8','LQToUE_Single_L0p8',LQToUE_Single_L_0p8,variable,binning,selection+Filters+LumiAndPU+lq_choice,SignalStyle,Label)
        h_Signal.Add(h_LQToUE_Single_L0p8)
        h_LQToUE_Single_L1p0=MakeHisto('h_LQToUE_Single_L1p0','LQToUE_Single_L1p0',LQToUE_Single_L_1p0,variable,binning,selection+Filters+LumiAndPU+lq_choice,SignalStyle,Label)
        h_Signal.Add(h_LQToUE_Single_L1p0)
        SignalIntegral=h_Signal.Integral()
        #print SignalIntegral
        return SignalIntegral

    if "Background" in Type:
        #h_WJets=MakeHisto('h_WJets','W+Jets',WJetsJBin,variable,binning,selection+LumiAndPU+Filters,WStackStyle,Label)
        #h_DiBoson=MakeHisto('h_DiBoson','DiBoson',DiBoson,variable,binning,selection+LumiAndPU+Filters,DiBosonStackStyle,Label)
        #h_SingleTop=MakeHisto('h_SingleTop','SingleTop',SingleTop,variable,binning,selection+LumiAndPU+Filters,StopStackStyle,Label)    

        h_ZJets=MakeHisto('h_ZJets','Z+Jets',ZJetsJBin,variable,binning,selection+'*('+str(zscale)+')'+LumiAndPU+Filters,ZStackStyle,Label)
        #h_GJets=MakeHisto('h_GJets','#gamma+Jets',Gjets,variable,binning,selection+LumiAndPU+Filters,GJetsStackStyle,Label)
        #Backgrounds=[h_WJets,h_QCD,h_TTBar,h_ZJets]
        #Backgrounds=[h_WJets,h_TTBar,h_ZJets]
        Backgrounds=[h_ZJets]

        BackgroundIntegral = sum(k.Integral() for k in Backgrounds)
        return BackgroundIntegral
        
    #Adding up backgrounds...
    #h_WJets.SetTitle("Other Backgrounds")
    #h_WJets.Add(h_DiBoson)
    #h_WJets.Add(h_SingleTop)
    #h_WJets.Add(h_GJets)


    
    

def DoIntegralsOld(JustIntegrate,lq_choice, selection, emuselection, qcdselection, use_emu, drawSub, variable, variable_emu, variable_qcd, xlabel,zscale,ttscaler):
    SetStyle()
    channel = "ee"
    Luminosity = "19600"
    binning = [5,0,500]
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
    #h_Signal=MakeHisto('h_Signal','LQToUE_Single_L_0p2',LQToUE_Single_L_0p2,variable,binning,selection+Filters+lq_choice,SignalStyle,Label)
    #h_LQToUE_Single_L0p4=MakeHisto('h_LQToUE_Single_L0p4','LQToUE_Single_L0p4',LQToUE_Single_L_0p4,variable,binning,selection+Filters+lq_choice,SignalStyle,Label)
    #h_Signal.Add(h_LQToUE_Single_L0p4)
    #h_LQToUE_Single_L0p6=MakeHisto('h_LQToUE_Single_L0p6','LQToUE_Single_L0p6',LQToUE_Single_L_0p6,variable,binning,selection+Filters+lq_choice,SignalStyle,Label)
    #h_Signal.Add(h_LQToUE_Single_L0p6)
    #h_LQToUE_Single_L0p8=MakeHisto('h_LQToUE_Single_L0p8','LQToUE_Single_L0p8',LQToUE_Single_L_0p8,variable,binning,selection+Filters+lq_choice,SignalStyle,Label)
    #h_Signal.Add(h_LQToUE_Single_L0p8)
    #h_LQToUE_Single_L1p0=MakeHisto('h_LQToUE_Single_L1p0','LQToUE_Single_L1p0',LQToUE_Single_L_1p0,variable,binning,selection+Filters+lq_choice,SignalStyle,Label)
    #h_Signal.Add(h_LQToUE_Single_L1p0)

    #h_Data=MakeHisto('h_Data','Data',DoublePhotonData,variable,binning,selection+Filters,DataRecoStyle,Label)

    #h_WJets=MakeHisto('h_WJets','W+Jets',WJetsJBin,variable,binning,selection+LumiAndPU+Filters,WStackStyle,Label)
    #h_DiBoson=MakeHisto('h_DiBoson','DiBoson',DiBoson,variable,binning,selection+LumiAndPU+Filters,DiBosonStackStyle,Label)
    #h_SingleTop=MakeHisto('h_SingleTop','SingleTop',SingleTop,variable,binning,selection+LumiAndPU+Filters,StopStackStyle,Label)    

    h_ZJets=MakeHisto('h_ZJets','Z+Jets',ZJetsJBin,variable,binning,selection+'*('+str(zscale)+')'+LumiAndPU+Filters,ZStackStyle,Label)


    if False:
        h_TTBar=MakeHisto('h_TTBar','t#bar{t}',emu_SingleMuData,variable_emu,binning,emuselection+Filters,TTStackStyle,Label)
        h_emu_WJets=MakeHisto('h_emu_WJets','W+Jets',emu_WJetsJBin,variable_emu,binning,emuselection+LumiAndPU+Filters,TTStackStyle,Label)
        h_emu_DiBoson=MakeHisto('h_emu_DiBoson','DiBoson',emu_DiBoson,variable_emu,binning,emuselection+LumiAndPU+Filters,TTStackStyle,Label)
        h_emu_ZJets=MakeHisto('h_emu_ZJets','Z+Jets',emu_ZJetsJBin,variable_emu,binning,emuselection+LumiAndPU+Filters,TTStackStyle,Label)
        h_emu_SingleTop=MakeHisto('h_emu_SingleTop','SingleTop',emu_SingleTop,variable_emu,binning,emuselection+LumiAndPU+Filters,TTStackStyle,Label)
        #h_emu_GJets=MakeHisto('h_Gjets','t#bar{t}',emu_Gjets,variable,binning,tt_sel_weight,GJetsStackStyle,Label)

        h_TTBar.Add(h_emu_WJets,-1)
        h_TTBar.Add(h_emu_DiBoson,-1)
        h_TTBar.Add(h_emu_ZJets,-1)
        h_TTBar.Add(h_emu_SingleTop,-1)

        h_TTBar.Scale(ttscaler)

    #If the channel is ee, include G Jets background and the QCD fake rate sample
    if True:
        #h_GJets=MakeHisto('h_GJets','#gamma+Jets',Gjets,variable,binning,selection+LumiAndPU+Filters,GJetsStackStyle,Label)
        #if (zscale != 1.00):
        if False:
            h_QCD=MakeHisto('h_QCD','Data',qcd_SinglePhotonData,variable_qcd,binning,qcdselection+Filters,QCDStackStyle,Label)

            h_qcd_WJets=MakeHisto('h_qcd_WJets','W+Jets',qcd_WJetsJBin,variable_qcd,binning,qcdselection+LumiAndPU+Filters,WStackStyle,Label)
            h_qcd_DiBoson=MakeHisto('h_qcd_DiBoson','DiBoson',qcd_DiBoson,variable_qcd,binning,qcdselection+LumiAndPU+Filters,DiBosonStackStyle,Label)
            h_qcd_ZJets=MakeHisto('h_qcd_ZJets','Z+Jets',qcd_ZJetsJBin,variable_qcd,binning,qcdselection+LumiAndPU+Filters,ZStackStyle,Label)
            h_qcd_SingleTop=MakeHisto('h_qcd_SingleTop','SingleTop',qcd_SingleTop,variable_qcd,binning,qcdselection+LumiAndPU+Filters,StopStackStyle,Label)
            h_qcd_GJets=MakeHisto('h_qcd_Gjets','t#bar{t}',qcd_Gjets,variable_qcd,binning,qcdselection+LumiAndPU+Filters,GJetsStackStyle,Label)
            h_qcd_TTBar=MakeHisto('h_qcd_TTBar','t#bar{t}',qcd_TTBarDBin,variable_qcd,binning,qcdselection+LumiAndPU+Filters,TTStackStyle,Label)

            h_QCD.Add(h_qcd_WJets,-1)
            h_QCD.Add(h_qcd_DiBoson,-1)
            h_QCD.Add(h_qcd_ZJets,-1)
            h_QCD.Add(h_qcd_SingleTop,-1)
            h_QCD.Add(h_qcd_GJets,-1)
            h_QCD.Add(h_qcd_TTBar,-1)
            
            nBins = binning[0]
            
            for i in range(nBins):
                if (h_QCD.GetBinContent(i) <= 0):
                    h_QCD.SetBinContent(i,0.0001)

       


    #Adding up backgrounds...
    #h_WJets.SetTitle("Other Backgrounds")
    #h_WJets.Add(h_DiBoson)
    #h_WJets.Add(h_SingleTop)
    #h_WJets.Add(h_GJets)
    #Backgrounds=[h_WJets,h_QCD,h_TTBar,h_ZJets]
    #Backgrounds=[h_WJets,h_TTBar,h_ZJets]
    Backgrounds=[h_ZJets]

    BackgroundIntegral = sum(k.Integral() for k in Backgrounds)
    #DataIntegral = h_Data.Integral()

    #print "Data = " + str(DataIntegral)
    #print "Background = " + str(BackgroundIntegral)
    return BackgroundIntegral
    

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


def GetUncertainty(PDF,length,Selection,Selection_emu,Selection_qcd,lq_choice,znorm,ttscaler,use_emu,Type):
    MaxValue = 0
    MinValue = 9999999
    BaseValue = DoIntegrals(Type,False,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, False,  "N_Vertices", "N_Vertices", "N_Vertices", "N_{Vertices}" , znorm, ttscaler)
    for i in range(length):
        ThisSelection = Selection + "*"+PDF+"["+str(i)+"]"
        ThisSelection_emu = Selection_emu + "*"+PDF+"["+str(i)+"]"
        ThisSelection_qcd = Selection_qcd + "*"+PDF+"["+str(i)+"]"
        ThisValue=DoIntegrals(Type,False,lq_choice, ThisSelection, ThisSelection_emu, ThisSelection_qcd, use_emu, False,  "N_Vertices", "N_Vertices", "N_Vertices", "N_{Vertices}" , znorm, ttscaler)
        if ThisValue > MaxValue:
            MaxValue = ThisValue
        if ThisValue < MinValue:
            MinValue = ThisValue

    onesigma = (( (MaxValue-MinValue)/2 )/BaseValue)
    
    #These values represent 2 sigma for CTEQ, need to adjust to 1 sigma
    if 'CTEQ' in PDF:
        onesigma = onesigma / 1.645

    print "1 sigma = " + str(onesigma)

def integrate():


    use_emu = False
    ttscaler = 0.5942599
    znorm = 0.96072
    #znorm = 1.0001
    #znorm = 1.0

    Trigger = '*(CurrentDoubleElePass>0.5)'
    Trigger_emu = '*(HLTMu40TriggerPass>0.5)'
    Trigger_qcd = '*((SinglePhotonTriggerPass>0.5)*SinglePhotonTriggerPrescale)'


    lq_choice = "*(LQmass==700)*(LQisCMu==0)*(LQcoupling==1.0)*(1/1000)"
    if InputCuts:
        Selections = GetSelections(ifile)
        Selection = Selections[0]
        Selection_emu = Selections[1]
        Selection_qcd = Selections[2]

    GetUncertainty("WEIGHTS_CTEQ",52,Selection,Selection_emu,Selection_qcd,lq_choice,znorm,ttscaler,use_emu,"LQ")
    GetUncertainty("WEIGHTS_NNPDF",100,Selection,Selection_emu,Selection_qcd,lq_choice,znorm,ttscaler,use_emu,"LQ")
    GetUncertainty("WEIGHTS_MSTW",40,Selection,Selection_emu,Selection_qcd,lq_choice,znorm,ttscaler,use_emu,"LQ")

    #GetUncertainty("WEIGHTS_CTEQ",52,Selection,Selection_emu,Selection_qcd,lq_choice,znorm,ttscaler,use_emu,"Background")
    #GetUncertainty("WEIGHTS_NNPDF",100,Selection,Selection_emu,Selection_qcd,lq_choice,znorm,ttscaler,use_emu,"Background")
    #GetUncertainty("WEIGHTS_MSTW",40,Selection,Selection_emu,Selection_qcd,lq_choice,znorm,ttscaler,use_emu,"Background")
    



def main():
    integrate()

main()
