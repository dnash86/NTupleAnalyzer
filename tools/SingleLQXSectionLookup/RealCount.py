from ROOT import *
import os
import sys
import math

Files = os.popen("cmsLs /store/group/phys_exotica/leptonsPlusJets/RootNtuple/dnash/RootNtuple-V00-03-09_SingleLQ_20130117_103725 | gawk '{print $5}' ").readlines()


def QuickIntegral(tree,selection):
    h = TH1D('h','h',1,-1,3)
    #h.Sumw2()
    #print selection
    tree.Project('h','1.0',selection)
    #print "done"
    I = h.GetBinContent(1)
    #I = h.GetEntries()
    #E = h.GetBinError(1)
    h.Delete()
    return I
                                
for x in range(len(Files)):
    Files[x] = Files[x].replace('\n','')
    print Files[x]
    exec('CurrentTree'+" = TFile.Open(\"root://eoscms//eos/cms/"+Files[x]+"\")"+".Get(\"PhysicalVariables\")")
    #print QuickIntegral(CurrentTree,"LQTag==
    print QuickIntegral(CurrentTree,"1.0")
