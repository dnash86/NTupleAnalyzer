from ROOT import *
import os
import sys
import math
from time import strftime


#from ProcessHistos import *

from CMSStyle import *
from HistoCreation import *
from WeightsAndFilters import *
from tdrstyle import *
from CMS_lumi import *

#################################
#   Loading trees...



#Files_emu = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_Foremu_EMu_ReRun_2014_04_30_22_04_51/SummaryFiles'

#Files_emu='/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_Foremu_ForEMuFixedElectronEta_2014_07_01_16_02_33/SummaryFiles'

#Files_emu = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_Foremu_EMuLowerSkimCorrectMuIDLowerJetSepPt_SmearingInsurance_2014_07_27_02_01_47/SummaryFiles'
#Files_mumu = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_MuonsReRunNewStoreFile_2013_10_29_18_44_01/SummaryFiles'
Files_emu = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_Foremu_EMuLowerFixMuonKinematics_2014_07_30_14_17_53/SummaryFiles'

Files_mumu = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_MuonFixID_2014_07_30_14_18_20/SummaryFiles'



TreeName = 'PhysicalVariables'

Trigger = '*(HLTMu40TriggerPass>0.5)'
Trigger_emu = '*(HLTMu40TriggerPass>0.5)'


#################################
# Parsing arguments

a=sys.argv
InputCuts=False
UseOutputDir=False

for n in range(len(a)):
    if a[n]=='-i' or a[n]=='--input_cutcard':
        InputCuts=True
        ifile=a[n+1]
        print "Will use the input cut card for selection"
    if a[n]=='-o' or a[n]=='--output_dir':
        OutputDir=a[n+1]
        UseOutputDir=True


if not InputCuts:
    print "No input cut card, will use standard selection"



print "Loading..."
print Files_mumu
for f in os.popen('cmsLs '+Files_mumu+'| grep ".root" | gawk \'{print $NF}\' | gawk -F "/" \'{print $NF}\'').readlines():
    exec(f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_mumu+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")

for f in os.popen('cmsLs '+Files_emu+'| grep ".root" | grep -v LQTo | gawk \'{print $NF}\' | gawk -F "/" \'{print $NF}\'').readlines():
    exec('emu_'+f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_emu+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")

print "...done loading"


###############################################



def FindNormalization(selection, emuselection):

    TTStackStyle=[3005,21,.00001,2,4]
    binning= [10,0,5000]
    h_TTBar=MakeHisto('h_TTBar','t#bar{t}',TTBarDBin,"Pt_muon1",binning,selection+LumiAndPU+Filters,TTStackStyle,"label")
    h_TTBar_emusel=MakeHisto('h_TTBar','t#bar{t}',emu_TTBarDBin,"Pt_muon1",binning,emuselection+LumiAndPU+Filters,TTStackStyle,"label")
    
    #print h_TTBar.Integral()
    #print h_TTBar_emusel.Integral()
    Scalefac  = h_TTBar.Integral()/h_TTBar_emusel.Integral()
    print "Scale fac = " + str(Scalefac)

    htt=TH1D('htt','htt',1,-1,3)
    httemu=TH1D('httemu','httemu',1,-1,3)
    htt.Sumw2()
    httemu.Sumw2()
    TTBarDBin.Project('htt','1.0',selection+LumiAndPU+Filters)
    emu_TTBarDBin.Project('httemu','1.0',emuselection+LumiAndPU+Filters)
    htt.Divide(httemu)

    print str(h_TTBar.Integral())+"/"+str(h_TTBar_emusel.Integral())
    print str(round(htt.GetBinContent(1),3)) +"+/-" +str(round(htt.GetBinError(1),3))
    
    return (Scalefac)


    
    
def Plot(selection, emuselection,  drawSub, binning, variable, variable_emu, xlabel,zscale,ttscaler,tag):
    #SetStyle()
    setTDRStyle()
    Luminosity = "19.6"
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
    if False:
        Label=[xlabel,"Number of events"]
    
        
        TTStackStyle=[3005,21,.00001,2,4]
        DataRecoStyle=[0,21,0.0,2,1]
        
        h_Data=MakeHisto('h_Data','t#bar{t} data, e#mu sel',emu_SingleMuData,variable_emu,binning,emuselection+Trigger+Filters,DataRecoStyle,Label)
        
        h_emu_WJets=MakeHisto('h_emu_WJets','W+Jets',emu_WJetsJBin,variable_emu,binning,emuselection+LumiAndPU+SingleMuNonEmulatedTrigger+Filters,DataRecoStyle,Label)
        h_emu_DiBoson=MakeHisto('h_emu_DiBoson','DiBoson',emu_DiBoson,variable_emu,binning,emuselection+LumiAndPU+SingleMuNonEmulatedTrigger+Filters,DataRecoStyle,Label)
        h_emu_ZJets=MakeHisto('h_emu_ZJets','Z+Jets',emu_ZJetsJBin,variable_emu,binning,emuselection+LumiAndPU+SingleMuNonEmulatedTrigger+Filters,DataRecoStyle,Label)
        h_emu_SingleTop=MakeHisto('h_emu_SingleTop','SingleTop',emu_SingleTop,variable_emu,binning,emuselection+LumiAndPU+SingleMuNonEmulatedTrigger+Filters,DataRecoStyle,Label)
        h_emu_QCD=MakeHisto('h_emu_QCD','h_emu_QCD',emu_QCDMu,variable_emu,binning,emuselection+LumiAndPU+SingleMuNonEmulatedTrigger+Filters,DataRecoStyle,Label)
        print h_Data.Integral()
        h_Data.Add(h_emu_WJets,-1)
        print h_Data.Integral()
        h_Data.Add(h_emu_DiBoson,-1)
        print h_Data.Integral()
        h_Data.Add(h_emu_ZJets,-1)
        print h_Data.Integral()
        h_Data.Add(h_emu_SingleTop,-1)
        print h_Data.Integral()
        h_Data.Add(h_emu_QCD,-1)
        print ttscaler

        DataIntegral_Prescale = h_Data.Integral()
        
        h_Data.Scale(ttscaler)

    #Set the style for each dataset   Format:  FillStyle,MarkerStyle,MarkerSize,LineWidth,Colors

    Label=[xlabel,"Number of events"]

    DataRecoStyle=[0,21,0.0,2,1]
    WStackStyle=[3007,21,.00001,2,9]
    TTStackStyle=[3005,21,.00001,2,4]
    ZStackStyle=[3004,21,.00001,2,2]
    DiBosonStackStyle=[3006,21,.00001,2,9]
    StopStackStyle=[3006,21,.00001,2,3]
    QCDStackStyle=[3006,21,.00001,2,3]


    h_Data=MakeHisto('h_Data','Data',emu_SingleMuData,variable_emu,binning,emuselection+Trigger+Filters,DataRecoStyle,Label)

    h_WJets=MakeHisto('h_WJets','W+Jets',emu_WJetsJBin,variable_emu,binning,emuselection+LumiAndPU+SingleMuNonEmulatedTrigger+Filters,WStackStyle,Label)
    h_DiBoson=MakeHisto('h_DiBoson','DiBoson',emu_DiBoson,variable_emu,binning,emuselection+LumiAndPU+SingleMuNonEmulatedTrigger+Filters,DiBosonStackStyle,Label)
    h_SingleTop=MakeHisto('h_SingleTop','SingleTop',emu_SingleTop,variable_emu,binning,emuselection+LumiAndPU+SingleMuNonEmulatedTrigger+Filters,StopStackStyle,Label)    
    #h_QCD=MakeHisto('h_QCD','h_QCD',emu_QCDMu,variable_emu,binning,emuselection+LumiAndPU+SingleMuNonEmulatedTrigger+Filters,QCDStackStyle,Label)

    h_ZJets=MakeHisto('h_ZJets','Z+Jets',emu_ZJetsJBin,variable_emu,binning,emuselection+'*('+str(zscale)+')'+LumiAndPU+SingleMuNonEmulatedTrigger+Filters,ZStackStyle,Label)

    h_TTBar=MakeHisto('h_TTBar','t#bar{t}',emu_TTBarDBin,variable_emu,binning,emuselection+LumiAndPU+SingleMuNonEmulatedTrigger+Filters,TTStackStyle,Label)



    print "Made the ttbar plots"

    DataIntegral_Prescale = h_Data.Integral()

    #Adding up backgrounds...
    print "h_WJets = " + str(h_WJets.Integral())
    print "h_Diboson = " + str(h_DiBoson.Integral())
    print "h_SingleTop = " + str(h_SingleTop.Integral())
    print "h_TTBar = " + str(h_TTBar.Integral())
    print "h_ZJets = " + str(h_ZJets.Integral())


    h_WJets.SetTitle("Other Backgrounds")
    h_WJets.Add(h_DiBoson)
    h_WJets.Add(h_SingleTop)
    #h_WJets.Add(h_QCD)
    h_TTBar.Scale(0.897)    
    Backgrounds=[h_WJets,h_TTBar,h_ZJets]

    #h_WJets.Scale(.915)
    #h_ZJets.Scale(.915)

    MCStack = THStack ("MCStack","")
    BackgroundIntegral = sum(k.Integral() for k in Backgrounds)
    DataIntegral = h_Data.Integral()
    ZIntegral = h_ZJets.Integral()

    SigmaData = math.sqrt(DataIntegral)
    SigmaNonZ = 0
    if (zscale !=1.00):
        NonZSigmaBackgrounds=[h_WJets,h_QCD,h_TTBar]
    else:
        NonZSigmaBackgrounds=[h_WJets,h_TTBar]
    for bg in Backgrounds:
        if bg.GetEntries() > 0:
            SigmaNonZ += bg.Integral() * math.pow(bg.GetEntries(),-0.5)
    SigmaZ = h_ZJets.Integral()*math.pow(h_ZJets.GetEntries(),-0.5)

    print "Data = " + str(DataIntegral)
    print "Background = " + str(BackgroundIntegral)
    print "tt : " + str(h_TTBar.Integral()) + "+/-" +str( h_TTBar.Integral()* math.pow(h_TTBar.GetEntries(),-0.5) )
    print "z : " + str(ZIntegral) + "+/-" +str( h_ZJets.Integral()* math.pow(h_ZJets.GetEntries(),-0.5) )
    #if (zscale !=1.00):
    #    print "qcd : " + str(h_QCD.Integral())




                                   
    print 'Stacking...  '	
    for histo in Backgrounds:
        MCStack.Add(histo)
        histo.SetMaximum(10000.*h_Data.GetMaximum())


    testbinning= [10,0,5000]
    h_TTBar_emusel=MakeHisto('h_TTBar','t#bar{t}',emu_TTBarDBin,"Pt_muon1",testbinning,emuselection+LumiAndPU+SingleMuNonEmulatedTrigger+Filters,TTStackStyle,"label")



    h=TH1D('h','h',1,-1,3)
    htotal=TH1D('htotal','htotal',1,-1,3)


    httemu=TH1D('httemu','httemu',1,-1,3)
    httemu.Sumw2()
    emu_TTBarDBin.Project('httemu','1.0',emuselection+LumiAndPU+SingleMuNonEmulatedTrigger+Filters)

    h.Sumw2()
    htotal.Sumw2()


    trees=[emu_SingleMuData,emu_WJetsJBin,emu_DiBoson,emu_ZJetsJBin,emu_SingleTop]#,emu_QCDMu]
    weights=[1,-1,-1,-1,-1]#,-1]
    selections=[emuselection+Trigger+Filters,emuselection+LumiAndPU+SingleMuNonEmulatedTrigger+Filters,emuselection+LumiAndPU+SingleMuNonEmulatedTrigger+Filters,emuselection+LumiAndPU+SingleMuNonEmulatedTrigger+Filters,emuselection+LumiAndPU+SingleMuNonEmulatedTrigger+Filters]#,emuselection+LumiAndPU+SingleMuNonEmulatedTrigger+Filters]

    for i in range(len(trees)):
        trees[i].Project('h','1.0',selections[i])
        htotal.Add(h,weights[i])
        print htotal.GetBinContent(1)

        #emu_TTBarDBin.Project('httemu','1.0',emuselection+LumiAndPU+SingleMuNonEmulatedTrigger+Filters)
    emu_TTBarDBin.Project('httemu','1.0',emuselection+LumiAndPU+SingleMuNonEmulatedTrigger+Filters)
    print "Total = " + str(htotal.GetBinContent(1))

    htotal.Divide(httemu)
    print "Other integral = "+str(h_TTBar_emusel.Integral())
    print "httemu = "+str(httemu.GetBinContent(1))
    print "Total = " + str(htotal.GetBinContent(1))
    I = htotal.GetBinContent(1)
    E = htotal.GetBinError(1)


    File = open('TTBar_mumu.tex','w')
    File.write('\\begin{tabular}{|c|c|}\n')

    File.write('{Data}  & {'+str(round(DataIntegral_Prescale,2))+'} \\\\\n')    
    File.write('\\hline\n')

    File.write('{$t\\bar{t}$}  & {'+str(round(h_TTBar.Integral(),2))+'} \\\\\n')
    File.write('{Z}  & {'+str(round(h_ZJets.Integral(),2))+'} \\\\\n')
    File.write('{Single Top}  & {'+str(round(h_SingleTop.Integral(),2))+'} \\\\\n')
    File.write('{DiBoson}  & {'+str(round(h_DiBoson.Integral(),2))+'} \\\\\n')
    File.write('{W}  & {'+str(round(h_WJets.Integral(),2))+'} \\\\\n')
    File.write('\\hline\n')
    File.write('\\hline\n')
    File.write('{$R_{t\\bar{t}}$} & {'+str(round(I,3))+'$\\pm$'+str(round(E,3))+'}\\\\\n')
    File.write('\\end{tabular}\n')
    File.close()
                                   
    MCStack.Draw("HIST")
    c1.cd(1).SetLogy()

    MCStack.SetMinimum(.1)
    MCStack.SetMaximum(10000.*h_Data.GetMaximum())                              
    MCStack=BeautifyStack(MCStack,Label)
    h_Data.Draw("HISTEPSAME")

    leg=TLegend(0.4,0.55,0.85,0.89,"","brNDC")
    leg.SetTextFont(42)
    leg.SetFillColor(0)
    leg.SetBorderSize(0)

    #h_DataDummy.SetMarkerSize(1.)
    leg.AddEntry(h_Data,"Data 2012, "+Luminosity+" fb^{-1}, 8 TeV")
    #leg.AddEntry(h_DataDummy,"Data")
    leg.AddEntry(h_ZJets,"Z/#gamma* + jets")
    leg.AddEntry(h_TTBar,"t#bar{t}")
    leg.AddEntry(h_WJets,"Other backgrounds")
	
    leg.Draw("SAME")

    h_Data.SetMinimum(.1)
    h_Data.SetMaximum(10000.*(h_Data.GetMaximum()))

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
            if (ndat>0):
                chi2 += pow((ndat -nbg),2.0)/pow(ndat,0.5)
            
            h_comp.SetBinContent(ibin,0.0 )
            h_compr.SetBinContent(ibin,0.0 )
            if (ndat>0 and nbg > 0):
                h_comp.SetBinContent(ibin, (ndat - nbg)/err_total )
            if (ndat>0 and nbg > 0):
                h_compr.SetBinContent(ibin, (ndat - nbg)/nbg )
            if (ndat>0 and nbg > 0):
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
        c1.Print("PlotsSingleSub_mumu2012/"+variable+"_"+tag+".png");


    
def DrawHisto(selection, emuselection,  drawSub, binning, variable, variable_emu, xlabel,zscale,ttscaler,tag):
    #SetStyle()
    #setTDRStyle()


    MaxRescaler=10.

    if False:
        MaxRescaler=100.
   
    if "N_Vertices" in variable:
        MaxRescaler = 1000.
    if "delta" in variable:
        MaxRescaler=10000.
    if "Eta" in variable:
        MaxRescaler = 1000000


    Luminosity = "19600"
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
    #Label=[xlabel,"Number of events"]
    Label=[xlabel,"Events / "+str((binning[2]-binning[1])/binning[0])+" GeV"]
    
   
    TTStackStyle=[3005,21,.00001,2,4]
    DataRecoStyle=[0,21,0.0,2,1]

    h_Data=MakeHisto('h_Data','t#bar{t} data, e#mu sel',emu_SingleMuData,variable_emu,binning,emuselection+Filters+Trigger_emu,DataRecoStyle,Label)
    h_DataDummy=MakeHisto('h_DataDummy','t#bar{t} data, e#mu sel',emu_SingleMuData,variable_emu,binning,emuselection+Filters+Trigger_emu,DataRecoStyle,Label)


    h_emu_WJets=MakeHisto('h_emu_WJets','W+Jets',emu_WJetsJBin,variable_emu,binning,emuselection+LumiAndPU+SingleMuNonEmulatedTrigger+Filters,DataRecoStyle,Label)
    h_emu_DiBoson=MakeHisto('h_emu_DiBoson','DiBoson',emu_DiBoson,variable_emu,binning,emuselection+LumiAndPU+SingleMuNonEmulatedTrigger+Filters,DataRecoStyle,Label)
    h_emu_ZJets=MakeHisto('h_emu_ZJets','Z+Jets',emu_ZJetsJBin,variable_emu,binning,emuselection+LumiAndPU+SingleMuNonEmulatedTrigger+Filters,DataRecoStyle,Label)
    h_emu_SingleTop=MakeHisto('h_emu_SingleTop','SingleTop',emu_SingleTop,variable_emu,binning,emuselection+LumiAndPU+SingleMuNonEmulatedTrigger+Filters,DataRecoStyle,Label)
    h_emu_QCD=MakeHisto('h_emu_QCD','h_emu_QCD',emu_QCDMu,variable_emu,binning,emuselection+LumiAndPU+SingleMuNonEmulatedTrigger+Filters,DataRecoStyle,Label)
    print h_Data.Integral()
    h_Data.Add(h_emu_WJets,-1)
    print h_Data.Integral()
    h_Data.Add(h_emu_DiBoson,-1)
    print h_Data.Integral()
    h_Data.Add(h_emu_ZJets,-1)
    print h_Data.Integral()
    h_Data.Add(h_emu_SingleTop,-1)
    print h_Data.Integral()
    h_Data.Add(h_emu_QCD,-1)
    print ttscaler
    h_Data.Scale(ttscaler)

    
    for i in range(h_Data.GetNbinsX()):
        if  h_Data.GetBinContent(i+1) < 0.0:
            h_Data.SetBinContent(i+1,0.0)



    h_TTBar=MakeHisto('h_TTBar','t#bar{t}',TTBarDBin,variable,binning,selection+LumiAndPU+DoubleMuNonEmulatedTrigger+Filters,TTStackStyle,Label)
        

    h_TTBar.Scale(0.897)
    #Adding up backgrounds...
    Backgrounds=[h_TTBar]

    MCStack = THStack ("MCStack","")
    BackgroundIntegral = sum(k.Integral() for k in Backgrounds)
    DataIntegral = h_Data.Integral()

    print "Data = " + str(DataIntegral)
    print "Background = " + str(BackgroundIntegral)
                                   
    print 'Stacking...  '	
    for histo in Backgrounds:
        MCStack.Add(histo)
        histo.SetMaximum(MaxRescaler*h_Data.GetMaximum())
                                   
    MCStack.Draw("HIST")
    c1.cd(1).SetLogy()

    MCStack.SetMinimum(.1)
    MCStack.SetMaximum(MaxRescaler*h_Data.GetMaximum())                              
    MCStack=BeautifyStack(MCStack,Label)
    h_Data.Draw("HISTEPSAME")

    leg=TLegend(0.4,0.55,0.89,.89,"","brNDC")
    leg.SetTextFont(132)
    leg.SetFillColor(0)
    leg.SetBorderSize(0)
    #leg.AddEntry(h_Data,"Data 2012, "+Luminosity+" pb^{-1}")

    h_DataDummy.SetMarkerSize(1.)
    #leg.AddEntry(h_DataDummy,"Data 2012, "+Luminosity+" fb^{-1}, 8 TeV")
    leg.AddEntry(h_DataDummy,"Data - Non-t#bar{t} MC, e#mu sel")
    leg.AddEntry(h_TTBar,"t#bar{t} MC, #mu#mu sel")
	
    leg.Draw("SAME")

    h_Data.SetMinimum(.1)
    h_Data.SetMaximum(MaxRescaler*(h_Data.GetMaximum()))

    #txt = TLatex((binning[2]-binning[1])*.02+binning[1],.3*5.0*h_Data.GetMaximum(), "Work in Progress")
    #txt = TLatex((binning[2]-binning[1])*.02+binning[1],.15*5.0*h_Data.GetMaximum(), "CMS Preliminary")
    #txt.SetTextFont(132)
    #txt.SetTextSize(0.06)
    #txt.Draw()

                       
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
            if ndat < 0.0:
                ndat=0.0
            nbg = 1.0*(h_bg.GetBinContent(ibin))
            datmean += 1.0*(h_Data.GetBinContent(ibin))*h_Data.GetBinCenter(ibin)
            err_nbg = 1.0*(h_bg.GetBinError(ibin))
            err_total = sqrt(  pow(err_nbg,2.0) + ndat )
            
            mcmean += 1.0*(h_bg.GetBinContent(ibin))*h_bg.GetBinCenter(ibin)
            if (ndat>0):
                chi2 += pow((ndat -nbg),2.0)/pow(ndat,0.5)
            
            h_comp.SetBinContent(ibin,0.0 )
            h_compr.SetBinContent(ibin,0.0 )
            if (ndat>0 and nbg > 0):
                h_comp.SetBinContent(ibin, (ndat - nbg)/err_total )
            if (ndat>0 and nbg > 0):
                h_compr.SetBinContent(ibin, (ndat - nbg)/nbg )
            if (ndat>0 and nbg > 0):
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

    CMS_lumi(pad1,2,0)
    if UseOutputDir:
        c1.Print(OutputDir+"/"+variable+"_"+tag+".png");
        c1.Print(OutputDir+"/"+variable+"_"+tag+".pdf");
    else:
        c1.Print("PlotsSingleSub_mumu2012/"+variable+"_"+tag+".png");
        c1.Print("PlotsSingleSub_mumu2012/"+variable+"_"+tag+".pdf");



def DrawHistoActualClosure(selection, emuselection,  drawSub, binning, variable, variable_emu, xlabel,zscale,ttscaler,tag):
    #SetStyle()
    #setTDRStyle()


    MaxRescaler=10.

    if False:
        MaxRescaler=100.
   
    if "N_Vertices" in variable:
        MaxRescaler = 1000.
    if "delta" in variable:
        MaxRescaler=10000.
    if "Eta" in variable:
        MaxRescaler = 1000000


    Luminosity = "19600"
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
    #Label=[xlabel,"Number of events"]
    Label=[xlabel,"Events / "+str((binning[2]-binning[1])/binning[0])+" GeV"]
    
   
    TTStackStyle=[3005,21,.00001,2,4]
    DataRecoStyle=[0,21,0.0,2,1]


    h_Data=MakeHisto('h_Data','t#bar{t}',emu_TTBarDBin,variable_emu,binning,emuselection+LumiAndPU+SingleMuNonEmulatedTrigger+Filters,TTStackStyle,Label)
    h_DataDummy=MakeHisto('h_DataDummy','t#bar{t}',emu_TTBarDBin,variable_emu,binning,emuselection+LumiAndPU+SingleMuNonEmulatedTrigger+Filters,TTStackStyle,Label)


    h_Data.Scale(ttscaler)

    
    for i in range(h_Data.GetNbinsX()):
        if  h_Data.GetBinContent(i+1) < 0.0:
            h_Data.SetBinContent(i+1,0.0)




    h_TTBar=MakeHisto('h_TTBar','t#bar{t}',TTBarDBin,variable,binning,selection+LumiAndPU+DoubleMuNonEmulatedTrigger+Filters,TTStackStyle,Label)
        

    h_TTBar.Scale(0.897)
    #Adding up backgrounds...
    Backgrounds=[h_TTBar]

    MCStack = THStack ("MCStack","")
    BackgroundIntegral = sum(k.Integral() for k in Backgrounds)
    DataIntegral = h_Data.Integral()

    print "Data = " + str(DataIntegral)
    print "Background = " + str(BackgroundIntegral)
                                   
    print 'Stacking...  '	
    for histo in Backgrounds:
        MCStack.Add(histo)
        histo.SetMaximum(MaxRescaler*h_Data.GetMaximum())
                                   
    MCStack.Draw("HIST")
    c1.cd(1).SetLogy()

    MCStack.SetMinimum(.1)
    MCStack.SetMaximum(MaxRescaler*h_Data.GetMaximum())                              
    MCStack=BeautifyStack(MCStack,Label)
    h_Data.Draw("HISTEPSAME")

    leg=TLegend(0.4,0.55,0.89,.89,"","brNDC")
    leg.SetTextFont(132)
    leg.SetFillColor(0)
    leg.SetBorderSize(0)
    #leg.AddEntry(h_Data,"Data 2012, "+Luminosity+" pb^{-1}")


    h_Data.SetMarkerColor(1)
    h_DataDummy.SetMarkerColor(1)
    h_Data.SetLineColor(1)
    h_DataDummy.SetLineColor(1)

    h_Data.SetFillColor(1)
    h_DataDummy.SetFillColor(1)

    h_DataDummy.SetMarkerSize(1.)
    #leg.AddEntry(h_DataDummy,"Data 2012, "+Luminosity+" fb^{-1}, 8 TeV")
    leg.AddEntry(h_DataDummy,"t#bar{t} MC, e#mu sel, rescaled")
    leg.AddEntry(h_TTBar,"t#bar{t} MC, #mu#mu sel")
	
    leg.Draw("SAME")

    h_Data.SetMinimum(.1)
    h_Data.SetMaximum(MaxRescaler*(h_Data.GetMaximum()))

    #txt = TLatex((binning[2]-binning[1])*.02+binning[1],.3*5.0*h_Data.GetMaximum(), "Work in Progress")
    #txt = TLatex((binning[2]-binning[1])*.02+binning[1],.15*5.0*h_Data.GetMaximum(), "CMS Preliminary")
    #txt.SetTextFont(132)
    #txt.SetTextSize(0.06)
    #txt.Draw()

                       
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
            if ndat < 0.0:
                ndat=0.0
            nbg = 1.0*(h_bg.GetBinContent(ibin))
            datmean += 1.0*(h_Data.GetBinContent(ibin))*h_Data.GetBinCenter(ibin)
            err_nbg = 1.0*(h_bg.GetBinError(ibin))
            err_total = sqrt(  pow(err_nbg,2.0) + ndat )
            
            mcmean += 1.0*(h_bg.GetBinContent(ibin))*h_bg.GetBinCenter(ibin)
            if (ndat>0):
                chi2 += pow((ndat -nbg),2.0)/pow(ndat,0.5)
            
            h_comp.SetBinContent(ibin,0.0 )
            h_compr.SetBinContent(ibin,0.0 )
            if (ndat>0 and nbg > 0):
                h_comp.SetBinContent(ibin, (ndat - nbg)/err_total )
            if (ndat>0 and nbg > 0):
                h_compr.SetBinContent(ibin, (ndat - nbg)/nbg )
            if (ndat>0 and nbg > 0):
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

    CMS_lumi(pad1,2,0)
    if UseOutputDir:
        c1.Print(OutputDir+"/"+variable+"_"+tag+".png");
        c1.Print(OutputDir+"/"+variable+"_"+tag+".pdf");
    else:
        c1.Print("PlotsSingleSub_mumu2012/"+variable+"_"+tag+".png");
        c1.Print("PlotsSingleSub_mumu2012/"+variable+"_"+tag+".pdf");




def GetSelections(ifile):
    import csv
    csvfile=open(ifile,'r')
    WriteToSelection=False
    WriteToSelection_emu=False
    Selections=['','']
    for row in csv.reader(csvfile):
        print row
        if row[0] == "#Selection":
            WriteToSelection=True
            WriteToSelection_emu=False
        if row[0] == "#Selection_emu":
            WriteToSelection_emu=True
            WriteToSelection=False
        if (row[0][0]!='#') and (len(row)==3):
            if WriteToSelection:
                if Selections[0]!='': Selections[0] += '*'
                Selections[0] += '('+row[0]+row[1]+row[2]+')'
            if WriteToSelection_emu:
                if Selections[1]!='': Selections[1] += '*'
                Selections[1] += '('+row[0]+row[1]+row[2]+')'
    print Selections
    return Selections



def MakePlots():

    znorm=1.0
    drawSub = True
    if InputCuts:
        Selections = GetSelections(ifile)
        Selection = Selections[0]
        Selection_emu = Selections[1]
    else:
        Selection = '((Pt_muon1>45)*(Pt_muon2>45)*(Pt_pfjet1>45)*(deltaR_muon1muon2>0.3)*((abs(Eta_muon1)<2.1)*(abs(Eta_muon2)<2.1))*(M_muon1muon2>110))*(ST_pf_ee_single> 250)'

        Selection_emu = '((Pt_muon1>45)*(Pt_HEEPele1>45)*(Pt_pfjet1>45)*(deltaR_muon1HEEPele1>0.3)*((abs(Eta_muon1)<2.1)*(abs(Eta_HEEPele1)<2.1))*(M_muon1HEEPele1>110))*(ST_pf_emu_single> 250)'


    #Trigger = '*(HLTMu40TriggerPass>0.5)'
    #Trigger_emu = '*(HLTMu40TriggerPass>0.5)'
    #Selection +=Trigger
    #Selection_emu +=Trigger_emu

    filetag = "TTBarStudy"
    xtag = " ["+filetag+"]"

    
    ptbinning = [50,0,1000]
    etabinning = [48,-2.4,2.4]
    mbinning = [50,0,2000]
    stbinning = [50,0,2000]
    vertexbinning = [45,-0.5,44.5]
    deltarbinning = [50,0,5]
    deltaphibinning = [80,-4,4]
    isobinning = [100,0,10]
    relisobinning=[100,0,0.5]
    hcalisobinning=[100,0,5]
    jetcountbinning=[9,0,8]

    chargebinning=[11,-5,5]

    ttscaler = FindNormalization(Selection,Selection_emu)


    #Plot(Selection, Selection_emu, drawSub, stbinning, "ST_pf_mumu_single", "ST_pf_emu_single", "S_{T} (GeV)" +xtag, znorm, ttscaler,filetag)

    #Plot(Selection, Selection_emu, drawSub, mbinning, "M_singleLQ_mupfjet_Masshigh", "M_singleLQ_emusel_Masshigh", "M_{#ell jet} " +xtag, znorm, ttscaler,filetag)

    #Plot(Selection, Selection_emu, drawSub, mbinning, "M_muon1muon2", "M_muon1HEEPele1",  "M_{#mu#mu}(GeV)  " +xtag  ,znorm, ttscaler,filetag)


    #Plot(Selection, Selection_emu, drawSub, ptbinning, "Pt_muon1", "max(Pt_HEEPele1,Pt_muon1)", "p_{T} (#mu_{1}) (GeV) " +xtag,znorm, ttscaler,filetag)
    #Plot(Selection, Selection_emu, drawSub, ptbinning,  "Pt_muon2", "min(Pt_HEEPele1,Pt_muon1)","p_{T} (#mu_{2}) (GeV) " +xtag,znorm, ttscaler,filetag)
    #Plot(Selection, Selection_emu, drawSub, ptbinning, "Pt_pfjet1","Pt_pfjet1", "p_{T} (jet_{1}) (GeV) " +xtag,znorm, ttscaler,filetag)

    #Plot(Selection, Selection_emu, drawSub, etabinning, "Eta_muon2", "Eta_muon1*(Pt_muon1<Pt_HEEPele1)+Eta_HEEPele1*(Pt_HEEPele1<Pt_muon1)", "#eta (#mu_{2}) " +xtag,  znorm, ttscaler,filetag)
    
    #Plot(Selection, Selection_emu, drawSub, etabinning, "Eta_muon1", "Eta_muon1*(Pt_muon1>Pt_HEEPele1)+Eta_HEEPele1*(Pt_HEEPele1>Pt_muon1)", "#eta (#mu_{1}) " +xtag,  znorm, ttscaler,filetag)

    #Plot(Selection, Selection_emu,drawSub, jetcountbinning, "PFJetCount", "PFJetCount", "PFJetCount" +xtag, znorm, ttscaler,filetag)





    filetag = "TTBarStudyClosureTestWithMC"
    #xtag = " ["+filetag+"]"
    xtag = ""


    #DrawHistoActualClosure(Selection, Selection_emu, drawSub, mbinning, "M_singleLQ_mupfjet_Masshigh", "M_singleLQ_emusel_Masshigh", "M_{#mu jet} " +xtag, znorm, ttscaler,filetag)
    #return


    3DrawHistoActualClosure(Selection, Selection_emu, drawSub, stbinning, "ST_pf_mumu_single", "ST_pf_emu_single", "S_{T} (GeV)" +xtag, znorm, ttscaler,filetag)
    #return




    filetag = "TTBarStudyClosure"
    #xtag = " ["+filetag+"]"
    xtag = ""

    
    DrawHisto(Selection, Selection_emu, drawSub, stbinning, "ST_pf_mumu_single", "ST_pf_emu_single", "S_{T} (GeV)" +xtag, znorm, ttscaler,filetag)
    return

    DrawHisto(Selection, Selection_emu, drawSub, mbinning, "M_singleLQ_mupfjet_Masshigh", "M_singleLQ_emusel_Masshigh", "M_{#mu jet} " +xtag, znorm, ttscaler,filetag)
    return





    DrawHisto(Selection, Selection_emu, drawSub, mbinning, "M_muon1muon2", "M_muon1HEEPele1",  "M_{#mu#mu}(GeV)  " +xtag  ,znorm, ttscaler,filetag)

    #return
    DrawHisto(Selection, Selection_emu, drawSub, ptbinning, "Pt_muon1", "max(Pt_HEEPele1,Pt_muon1)", "p_{T} (#mu_{1}) (GeV) " +xtag,znorm, ttscaler,filetag)
    DrawHisto(Selection, Selection_emu, drawSub, ptbinning,  "Pt_muon2", "min(Pt_HEEPele1,Pt_muon1)","p_{T} (#mu_{2}) (GeV) " +xtag,znorm, ttscaler,filetag)
    DrawHisto(Selection, Selection_emu, drawSub, ptbinning, "Pt_pfjet1","Pt_pfjet1", "p_{T} (jet_{1}) (GeV) " +xtag,znorm, ttscaler,filetag)

    DrawHisto(Selection, Selection_emu, drawSub, etabinning, "Eta_muon2", "Eta_muon1*(Pt_muon1<Pt_HEEPele1)+Eta_HEEPele1*(Pt_HEEPele1<Pt_muon1)", "#eta (#mu_{2}) " +xtag,  znorm, ttscaler,filetag)
    
    DrawHisto(Selection, Selection_emu, drawSub, etabinning, "Eta_muon1", "Eta_muon1*(Pt_muon1>Pt_HEEPele1)+Eta_HEEPele1*(Pt_HEEPele1>Pt_muon1)", "#eta (#mu_{1}) " +xtag,  znorm, ttscaler,filetag)

    DrawHisto(Selection, Selection_emu,drawSub, jetcountbinning, "PFJetCount", "PFJetCount", "PFJetCount" +xtag, znorm, ttscaler,filetag)


def main():
    #ScaleFac = getvalues()
    MakePlots()
    
main()
