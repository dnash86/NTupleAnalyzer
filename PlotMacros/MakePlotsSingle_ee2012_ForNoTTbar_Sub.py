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
Files_ee = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_ReRun_OrderFixed_2014_05_06_15_52_31/SummaryFiles'
Files_qcd = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ForQCDStudy_QCDReRunEdmundCS_NoPtJetElimination_2014_02_07_21_29_51/SummaryFiles'
#Files_qcd = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ForQCDStudy_QCDVeryStrict_2014_04_13_21_31_02/SummaryFiles'

TreeName = 'PhysicalVariables'

print "Loading..."
for f in os.popen('cmsLs '+Files_ee+'| grep ".root" | gawk \'{print $NF}\' | gawk -F "/" \'{print $NF}\'').readlines():
    exec(f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_ee+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
    #print f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_ee+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")"
    print f.replace('-','_').replace(".root\n","")
    
for f in os.popen('cmsLs '+Files_emu+'| grep ".root" | grep -v LQTo | gawk \'{print $NF}\' | gawk -F "/" \'{print $NF}\'').readlines():
    exec('emu_'+f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_emu+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
    #print 'emu_'+f.replace('-','_').replace(".root\n","")

for f in os.popen('cmsLs '+Files_qcd+'| grep ".root" | grep -v LQTo | gawk \'{print $NF}\' | gawk -F "/" \'{print $NF}\'').readlines():
    exec('qcd_'+f.replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_qcd+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
    #print 'qcd_'+f.replace('-','_').replace(".root\n","")
print "...done loading"

#################################
# Parsing arguments

a=sys.argv
InputCuts=False
for n in range(len(a)):
    if a[n]=='-i' or a[n]=='--input_cutcard':
        InputCuts=True
        ifile=a[n+1]
        print "Will use the input cut card for selection"
    if a[n]=='-p' or a[n]=='--plot':
        PlotHistos=True
    if a[n]=='-i' or a[n]=='--integrate':
        IntegrateOnly=True
    if a[n]=='-f' or a[n]=='--final_selection_cutcard':
        fselfile=a[n+1]
    if a[n]=='-o' or a[n]=='--output_dir':
        OutputDir=a[n+1]
        UseOutputDir=True
if not InputCuts:
    print "No input cut card, will use standard selection"

###############################################

def DrawHisto(JustIntegrate,lq_choice, selection, emuselection, qcdselection, use_emu, drawSub, binning, variable, variable_emu, variable_qcd, xlabel,zscale,ttscaler,tag):
    SetStyle()
    channel = "ee"
    Luminosity = "19600"
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
    
    h_Signal=MakeHisto('h_Signal','LQToUE_Single_L_0p2',LQToUE_Single_L_0p2,variable,binning,selection+Filters+lq_choice,SignalStyle,Label)
    h_LQToUE_Single_L0p4=MakeHisto('h_LQToUE_Single_L0p4','LQToUE_Single_L0p4',LQToUE_Single_L_0p4,variable,binning,selection+Filters+lq_choice,SignalStyle,Label)
    h_Signal.Add(h_LQToUE_Single_L0p4)
    h_LQToUE_Single_L0p6=MakeHisto('h_LQToUE_Single_L0p6','LQToUE_Single_L0p6',LQToUE_Single_L_0p6,variable,binning,selection+Filters+lq_choice,SignalStyle,Label)
    h_Signal.Add(h_LQToUE_Single_L0p6)
    h_LQToUE_Single_L0p8=MakeHisto('h_LQToUE_Single_L0p8','LQToUE_Single_L0p8',LQToUE_Single_L_0p8,variable,binning,selection+Filters+lq_choice,SignalStyle,Label)
    h_Signal.Add(h_LQToUE_Single_L0p8)
    h_LQToUE_Single_L1p0=MakeHisto('h_LQToUE_Single_L1p0','LQToUE_Single_L1p0',LQToUE_Single_L_1p0,variable,binning,selection+Filters+lq_choice,SignalStyle,Label)
    h_Signal.Add(h_LQToUE_Single_L1p0)

    h_Data=MakeHisto('h_Data','Data',DoublePhotonData,variable,binning,selection+Filters,DataRecoStyle,Label)

    h_WJets=MakeHisto('h_WJets','W+Jets',WJetsJBin,variable,binning,selection+LumiAndPU+Filters,WStackStyle,Label)
    h_DiBoson=MakeHisto('h_DiBoson','DiBoson',DiBoson,variable,binning,selection+LumiAndPU+Filters,DiBosonStackStyle,Label)
    h_SingleTop=MakeHisto('h_SingleTop','SingleTop',SingleTop,variable,binning,selection+LumiAndPU+Filters,StopStackStyle,Label)    

    h_ZJets=MakeHisto('h_ZJets','Z+Jets',ZJetsJBin,variable,binning,selection+'*('+str(zscale)+')'+LumiAndPU+Filters,ZStackStyle,Label)
    print "Made the normal plots"

    if use_emu:
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
    else:
        h_TTBar=MakeHisto('h_TTBar','t#bar{t}',TTBarDBin,variable,binning,selection+LumiAndPU+Filters,TTStackStyle,Label)

    print "Made the ttbar plots"

    #If the channel is ee, include G Jets background and the QCD fake rate sample
    if channel == "ee":
        h_GJets=MakeHisto('h_GJets','#gamma+Jets',Gjets,variable,binning,qcdselection+LumiAndPU+Filters,GJetsStackStyle,Label)
        if (zscale != 1.00):
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

        else:
            h_QCD=MakeHisto('h_qcd_Data','Data',qcd_SinglePhotonData,variable_qcd,binning,qcdselection+Filters,DataRecoStyle,Label)
            h_QCD.Scale(0.0000000000000001) 
    
    print "Made the QCD plots"

    #If the channel is mumu, no need to include G Jets and use the mu enriched QCD sample
    #if channel = "mumu":
    #    h_QCDMu=MakeHisto('h_QCDMu','QCD',QCDMu,variable,binning,tt_sel_weight,QCDStackStyle,Label)
                                   

    #Adding up backgrounds...
    h_WJets.SetTitle("Other Backgrounds")
    h_WJets.Add(h_DiBoson)
    h_WJets.Add(h_SingleTop)
    h_WJets.Add(h_GJets)
    Backgrounds=[h_WJets,h_QCD,h_TTBar,h_ZJets]
    

    MCStack = THStack ("MCStack","")
    BackgroundIntegral = sum(k.Integral() for k in Backgrounds)
    DataIntegral = h_Data.Integral()
    print "Data = " + str(DataIntegral)
    print "Background = " + str(BackgroundIntegral)
    print "tt : " + str(h_TTBar.Integral())
    print "z : " + str(h_ZJets.Integral())
    print "qcd : " + str(h_QCD.Integral())
        
                                   
    print 'Stacking...  '	
    for histo in Backgrounds:
        MCStack.Add(histo)
        histo.SetMaximum(10*h_Data.GetMaximum())
                                   
    MCStack.Draw("HIST")
    c1.cd(1).SetLogy()

    MCStack.SetMinimum(.1)
    MCStack.SetMaximum(10*h_Data.GetMaximum())                              
    MCStack=BeautifyStack(MCStack,Label)
    h_Signal.SetLineStyle(3)
    h_Signal.Draw("HISTSAME")
    #h_Signal.Draw("HISTSAME")
    h_Data.Draw("HISTEPSAME")

    leg=TLegend(0.6,0.63,0.91,0.91,"","brNDC")
    leg.SetTextFont(132)
    leg.SetFillColor(0)
    leg.SetBorderSize(0)
    leg.AddEntry(h_Data,"Data 2012, "+Luminosity+" pb^{-1}")
    leg.AddEntry(h_ZJets,"Z/#gamma* + jets")
    leg.AddEntry(h_QCD,"QCD multijets")

    leg.AddEntry(h_Signal,"LQ Mass = 700, #lambda = 1.0")

    if (not use_emu):
        leg.AddEntry(h_TTBar,"t#bar{t}")
    if (use_emu):
        leg.AddEntry(h_TTBar,"t#bar{t} data driven")
	
    leg.AddEntry(h_WJets,"Other backgrounds")
    leg.Draw("SAME")

    h_Data.SetMinimum(.1)
    h_Data.SetMaximum(1.2*(h_Data.GetMaximum()))

    txt = TLatex((binning[2]-binning[1])*.02+binning[1],.3*5.0*h_Data.GetMaximum(), "Work in Progress")
    txt.SetTextFont(132)
    txt.SetTextSize(0.06)
    txt.Draw()
    if drawSub:
        pad2.cd()
	
        h_comp = TH1F("h_comp","",binning[0],binning[1],binning[2])
        h_compr = TH1F("h_compr","",binning[0],binning[1],binning[2])	
	
        h_bg = TH1F("h_bg","",binning[0],binning[1],binning[2])

        h_bg.Sumw2()
        for histo in Backgrounds:
            h_bg.Add(histo)
	
        nbinsx = binning[0]	
        ibin = 0
	
        chi2 = 0.0
	
        ndat = 0.0
        nbg = 0.0
        err_nbg = 0.0
        err_total = 0.0
	
        datmean = 0.0
        mcmean = 0.0
	
        xminl = 0
        xmaxl = 0
	
        for ibin in range(nbinsx):
            
            ndat = 1.0*(h_Data.GetBinContent(ibin))
            nbg = 1.0*(h_bg.GetBinContent(ibin))
            datmean += 1.0*(h_Data.GetBinContent(ibin))*h_Data.GetBinCenter(ibin)
            err_nbg = 1.0*(h_bg.GetBinError(ibin))
            err_total = sqrt(  pow(err_nbg,2.0) + ndat )
            
            mcmean += 1.0*(h_bg.GetBinContent(ibin))*h_bg.GetBinCenter(ibin)
            if (ndat!=0):
                chi2 += pow((ndat -nbg),2.0)/pow(ndat,0.5)
            
            h_comp.SetBinContent(ibin,0.0 )
            h_compr.SetBinContent(ibin,0.0 )
            if (ndat!=0 and nbg != 0):
                h_comp.SetBinContent(ibin, (ndat - nbg)/err_total )
            if (ndat!=0 and nbg != 0):
                h_compr.SetBinContent(ibin, (ndat - nbg)/nbg )
            if (ndat!=0 and nbg != 0):
                h_compr.SetBinError(ibin, (err_total)/nbg )

        h_comp.GetYaxis().SetTitle("N(#sigma) Diff.")
        h_comp.GetYaxis().SetTitleFont(132)
        h_comp.GetYaxis().SetTitleSize(.17)
        h_comp.GetYaxis().SetLabelSize(.11)
        h_comp.GetXaxis().SetLabelSize(.11)	
        h_comp.GetYaxis().SetTitleOffset(.25)
	
        line0 = TLine(binning[1],0,binning[2],0)
        line2u = TLine(binning[1],2,binning[2],2)
        line2d = TLine(binning[1],-2,binning[2],-2)
	
        h_comp.SetMinimum(-8)
        h_comp.SetMaximum(8)
        h_comp.SetMarkerStyle(21)
        h_comp.SetMarkerSize(0.5)
	
	
        h_comp.Draw("p")
        line0.Draw("SAME")
        line2u.Draw("SAME")
        line2d.Draw("SAME")
		
		
        pad2r.cd()
	
        h_compr.GetYaxis().SetTitle("Frac. Diff.")
        h_compr.GetYaxis().SetTitleFont(132)
        h_compr.GetYaxis().SetTitleSize(.17)
        h_compr.GetYaxis().SetLabelSize(.11)
        h_compr.GetXaxis().SetLabelSize(.11)	
        h_compr.GetYaxis().SetTitleOffset(.25)
	   
        h_compr.SetMinimum(-2.0)
        h_compr.SetMaximum(2.0)
        h_compr.SetLineColor(kRed)
        h_compr.SetLineWidth(2)
        h_compr.SetMarkerColor(kRed)
        h_compr.SetMarkerStyle(1)
        h_compr.SetMarkerSize(0.0)
	
        h_compr.Draw("ep")
        line0.Draw("SAME")
        print "Made the chi2 plots"
	if UseOutputDir:
            c1.Print(OutputDir+"/"+variable+"_"+tag+".png");
        else:
            c1.Print("PlotsSingleSub_ee2012/"+variable+"_"+tag+".png");

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




def plot():
    JustIntegrate=False
    drawSub = True
    use_emu = False
    ttscaler = 0.5942599
    znorm = 0.9629


    if InputCuts:
        Selections = GetSelections(ifile)
        Selection = Selections[0]
        Selection_emu = Selections[1]
        Selection_qcd = Selections[2]
    else:
        Selection = '((Pt_HEEPele1>45)*(Pt_HEEPele2>45)*(Pt_pfjet1>45)*(deltaR_HEEPele1ele2>0.3)*((abs(Eta_HEEPele1)<2.5)*(abs(Eta_HEEPele2)<2.5))*(M_HEEPele1ele2>110))*(ST_pf_ee_single> 250)'

        Selection_emu = '((Pt_muon1>45)*(Pt_HEEPele1>45)*(Pt_pfjet1>45)*(deltaR_muon1HEEPele1>0.3)*((abs(Eta_muon1)<2.5)*(abs(Eta_HEEPele1)<2.5))*(M_muon1HEEPele1>110))*(ST_pf_emu_single> 250)'

        Selection_qcd = '((Pt_QCDele1>45)*(Pt_QCDele2>45)*(Pt_pfjet1>45)*(deltaR_QCDele1ele2>0.3)*((abs(Eta_QCDele1)<2.5)*(abs(Eta_QCDele2)<2.5))*(M_QCDele1ele2>110))*((Pt_QCDele1+Pt_QCDele2+Pt_pfjet1)>250)'

    EndcapRegion = "0.0614298 -6.12052e-05 *Pt_QCDele1"
    BarrelRegion = "( (Pt_QCDele1 < 150) *( 0.0364505 -0.000108329 * Pt_QCDele1 ))+"
    BarrelRegion = BarrelRegion + "( (Pt_QCDele1> 150) *( 0.00836961 -9.02694e-06*Pt_QCDele1 ))"
    FakeRateValue = "*("
    FakeRateValue = FakeRateValue + "( (abs(Eta_QCDele1)< 1.442) *(pow("+BarrelRegion+",2)))+"
    FakeRateValue = FakeRateValue + "( (abs(Eta_QCDele1)> 1.56) *(pow("+EndcapRegion+",2)))"
    FakeRateValue = FakeRateValue + ")"

    Selection_qcd += FakeRateValue

    Trigger = '*(CurrentDoubleElePass>0.5)'
    Trigger_emu = '*(HLTMu40TriggerPass>0.5)'
    Trigger_qcd = '*((SinglePhotonTriggerPass>0.5)*SinglePhotonTriggerPrescale)'

    Selection +=Trigger
    Selection_emu +=Trigger_emu
    Selection_qcd += Trigger_qcd

    lq_choice = "*(LQmass==700)*(LQisCMu==0)*(LQcoupling==1.0)*(1/1000)"

    ptbinning = [50,0,1000]
    etabinning = [48,-2.4,2.4]
    mbinning = [50,0,2000]
    stbinning = [50,0,2000]
    vertexbinning = [45,-0.5,44.5]

    filetag = "Preselection"
    xtag = " ["+filetag+"]"

    print "About to start drawing the Histos..."
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, mbinning, "M_singleLQ_epfjet_Masshigh", "M_singleLQ_emusel_Masshigh","max(M_QCDele1pfjet1,M_QCDele2pfjet1)", "M_{e jet} " +xtag, znorm, ttscaler,filetag)

    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, vertexbinning, "N_Vertices", "N_Vertices", "N_Vertices", "N_{Vertices}" +xtag, znorm, ttscaler,filetag)	

    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, ptbinning, "Pt_HEEPele1", "max(Pt_HEEPele1,Pt_muon1)","Pt_QCDele1", "p_{T} (e_{1}) (GeV) " +xtag,znorm, ttscaler,filetag)
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd,use_emu , drawSub, ptbinning,  "Pt_HEEPele2", "min(Pt_HEEPele1,Pt_muon1)", "Pt_QCDele2","p_{T} (e_{2}) (GeV) " +xtag,znorm, ttscaler,filetag)
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, ptbinning, "Pt_pfjet1","Pt_pfjet1", "Pt_pfjet1", "p_{T} (jet_{1}) (GeV) " +xtag,znorm, ttscaler,filetag)

    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, etabinning, "Eta_HEEPele2", "Eta_muon1*(Pt_muon1<Pt_HEEPele1)+Eta_HEEPele1*(Pt_HEEPele1<Pt_muon1)","Eta_QCDele2", "#eta (e_{2}) " +xtag,  znorm, ttscaler,filetag)
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, etabinning, "Eta_HEEPele1", "Eta_muon1*(Pt_muon1>Pt_HEEPele1)+Eta_HEEPele1*(Pt_HEEPele1>Pt_muon1)","Eta_QCDele1", "#eta (e_{1}) " +xtag, znorm, ttscaler,filetag)
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, etabinning, "Eta_pfjet1", "Eta_pfjet1", "Eta_pfjet1","#eta (jet_{1}) " +xtag, znorm, ttscaler,filetag)

    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, stbinning, "ST_pf_ee_single", "ST_pf_emu_single","(Pt_QCDele1+Pt_QCDele2+Pt_pfjet1)", "S_{T} (GeV)" +xtag, znorm, ttscaler,filetag)


    
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, mbinning, "M_HEEPele1ele2", "M_muon1HEEPele1", "M_QCDele1ele2", "M_{ee}(GeV)  " +xtag  ,znorm, ttscaler,filetag)

    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, mbinning, "M_HEEPele1pfjet1", "M_HEEPele1pfjet1", "M_QCDele1pfjet1","M_{e jet} " +xtag,znorm, ttscaler,filetag)




def main():
    if PlotHistos:
        plot()
    if IntegrateOnly:
        integrate()

main()
