from ROOT import *
import os
import sys
import math



TreeName = "rootTupleTree/tree"
FileDirectory= "/store/group/phys_exotica/leptonsPlusJets/RootNtuple/dnash/RootNtuple-V00-03-09_SingleLQ_20130117_103725/"



def main():
    Count(FileDirectory,TreeName)



f = open('List.txt','r')
CheckList = f.readlines()
Numbers = []

w = open('TestResults.txt','w')
def Count(FileDirectory,TreeName): 
    
    f = open('List.txt','r')
    CheckList = f.readlines()
    Numbers = []
    for i in range(len(CheckList)):
        Numbers.append(0)

    for f in os.popen('cmsLs '+FileDirectory+'| grep ".root" | gawk \'{print $NF}\' | gawk -F "/" \'{print $NF}\'').readlines():
        #print f
        exec("CurrentTree"+" = TFile.Open(\"root://eoscms//eos/cms/"+FileDirectory+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
        #print "CurrentTree"+" = TFile.Open(\"root://eoscms//eos/cms/"+FileDirectory+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")"
        N= CurrentTree.GetEntries()

        for i in range(N):
            CurrentTree.GetEntry(i)
            name=""
            for k in range(len(CurrentTree.LQTag)):
                name+=( CurrentTree.LQTag[k])
            #if i == 1:
                #print name
            for j in range(len(CheckList)):
                if CheckList[j] in name:
                    Numbers[j] = Numbers[j] + 1
        print "Finished Section "+f+", current status: "
        print Numbers
    for i in range(len(Numbers)):
        w.write(str(Numbers[i])+"\n")

        #print CurrentTree.GetEntryList()
        #Cut = '(LQTag == "SLQ_tp_single-MLQ900g1r0.4")'
        #Cut = '(LQTag.at(0) == "S")'

        #Cut = ""
        #print QuickIntegral(CurrentTree,Cut)


def QuickIntegral(tree,selection):
	h = TH1D('h','h',1,-1,3)
	#h.Sumw2()
        #print selection
	tree.Project('h','1.0',selection)
        #print "done"
	I = h.GetBinContent(1)
	#E = h.GetBinError(1)
        h.Delete()
	return I


main()


f.close()
w.close()
