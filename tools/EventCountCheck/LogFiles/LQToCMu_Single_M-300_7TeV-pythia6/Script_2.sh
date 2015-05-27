###############################################################
#Note: Do not modify this script, it is used by EventCounter.sh
###############################################################


File=/castor/cern.ch/user/d/dnash/LeptonsPlusJets/RootNtupleMissingTwo/MissingTwo_20120411_193300/LQToCMu_Single_M-300_7TeV-pythia6__Summer11-PU_S4_START42_V11-v1__AODSIM_11_1_Hrz.root
# ^ This is a placeholder that will be changed by a sed command

cd /afs/cern.ch/user/d/dnash/CMSSW_4_2_8/src/NTupleAnalyzer/tools/EventCountCheck/
eval `scramv1 runtime -sh`
cd -

echo "{" >> TempCounter.C
echo "  gROOT->Reset();" >> TempCounter.C
echo -n "  TFile *f = TFile::Open(" >> TempCounter.C
echo -n '"' >> TempCounter.C
echo -n "$File" >> TempCounter.C
echo -n '"' >> TempCounter.C
echo ");" >> TempCounter.C
echo -n "  TH1F* h =(TH1F*)f.Get(" >> TempCounter.C
echo -n '"/LJFilter/EventCount/EventCounter"' >> TempCounter.C
echo ");" >> TempCounter.C
echo "  std::cout<<h->GetBinContent(1)<<std::endl;" >> TempCounter.C
echo -n  "  gROOT->ProcessLine(" >> TempCounter.C
echo -n '".q"' >> TempCounter.C
echo ");" >> TempCounter.C
echo "}" >> TempCounter.C
# ^ This produces a short script that finds the number of events in the root file

root -b TempCounter.C > output.txt
rm TempCounter.C
number=`gawk '(NR==19){print $1}' output.txt`
echo $number > number.txt
# ^ This outputs the number of events to a text file

cp number.txt /afs/cern.ch/user/d/dnash/CMSSW_4_2_8/src/NTupleAnalyzer/tools/EventCountCheck/LogFiles/LQToCMu_Single_M-300_7TeV-pythia6/Log_2.txt
# ^ Another placeholder that will be changed by a sed comand