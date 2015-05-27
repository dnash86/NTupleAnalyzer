from ROOT import *
import os
import sys
import math

def MakeHisto(name,legendname,tree,variable,binning,selection,style,label):
    #binset=ConvertBinning(binning)
    #n = len(binset)-1
    histo= TH1D(name,legendname,binning[0],binning[1],binning[2])
    histo.Sumw2()
    tree.Project(name,variable,selection)
    #Adding overflow bin to last bin
    print "Last Bin = " +str(histo.GetBinContent(binning[0]))
    histo.SetBinContent(binning[0],histo.GetBinContent(binning[0])+histo.GetBinContent(binning[0]+1))
    print "Last Bin = " +str(histo.GetBinContent(binning[0]))
    histo.SetFillStyle(style[0])
    histo.SetMarkerStyle(style[1])
    histo.SetMarkerSize(style[2])
    histo.SetLineWidth(style[3])
    histo.SetMarkerColor(style[4])
    if style[4] != 1:
        histo.SetLineColor(style[4])
        histo.SetFillColor(style[4])
        histo.SetFillColor(style[4])
    else:
        histo.SetLineColor(style[4])
        histo.SetFillColor(0)
        histo.SetFillColor(0)
    histo.GetXaxis().SetTitle(label[0])
    histo.GetYaxis().SetTitle(label[1])
    histo.GetXaxis().SetTitleFont(42)
    histo.GetYaxis().SetTitleFont(42)
    histo.GetXaxis().SetLabelFont(42)
    histo.GetYaxis().SetLabelFont(42)
    return histo

def IntegralAndError(trees,weights,selections):
    h=TH1D('h','h',1,-1,3)
    #htest=TH1('h','h',1,-1,3)
    htotal=TH1D('htotal','htotal',1,-1,3)
    h.Sumw2()
    htotal.Sumw2()
    Entries=0
    for i in range(len(trees)):
        trees[i].Project('h','1.0',selections[i])
        Entries+=h.GetEntries()
        htotal.Add(h,weights[i])
        #htest.Add(h,weights[i])
    I = htotal.GetBinContent(1)
    E = htotal.GetBinError(1)

    #htotal.SetBinErrorOption(htotal.kPoisson)

    #err_low = htotal.GetBinErrorLow(1)
    #err_up = htotal.GetBinErrorUp(1)

    #print "Normal error = " +str(E)
    #print "Poisson error = "+str(err_low) +", "+str(err_up)
    #print "I = " +str(I)
    #print "E = " +str(E)
    #print "htotal.Integral() = " +str(htotal.Integral())
    #print "h.Integral() = " +str(h.Integral())
    #print "htotal.GetEntries() = " +str(htotal.GetEntries())
    #print "h.GetEntries() = " +str(h.GetEntries())
    return [I,E,Entries]



def BeautifyStack(stack,label):
    stack.GetHistogram().GetXaxis().SetTitleFont(42)
    stack.GetHistogram().GetYaxis().SetTitleFont(42)

    stack.GetHistogram().GetXaxis().SetTitleSize(0.05)
    stack.GetHistogram().GetYaxis().SetTitleSize(0.05)
    stack.GetHistogram().GetXaxis().SetTitleOffset(0.9)
    stack.GetHistogram().GetYaxis().SetTitleOffset(0.75)
    stack.GetHistogram().GetXaxis().SetLabelFont(42)
    stack.GetHistogram().GetYaxis().SetLabelFont(42)
    stack.GetHistogram().GetXaxis().SetTitle(label[0])
    stack.GetHistogram().GetYaxis().SetTitle(label[1])
    
    return stack


