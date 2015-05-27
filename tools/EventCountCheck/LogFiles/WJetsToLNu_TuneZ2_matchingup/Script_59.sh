###############################################################
#Note: Do not modify this script, it is used by EventCounter.sh
###############################################################


File=/store/group/phys_exotica/leptonsPlusJets/leptoquarks/NTuples_V00_02_06/RootNtuple-V00-02-06-Summer11MC_ShapeSys_MG_20111208_222140/WJetsToLNu_TuneZ2_matchingup_7TeV-madgraph-tauola__Summer11-PU_S4_START42_V11-v1__AODSIM_153_1_Qs4.root
# ^ This is a placeholder that will be changed by a sed command

cd /afs/cern.ch/user/d/dnash/CMSSW_4_2_8/src/NTupleAnalyzer/tools/EventCountCheck/
eval `scramv1 runtime -sh`
cd -

echo "{" >> TempCounter.C
echo "  gROOT->Reset();" >> TempCounter.C
echo -n '  TFile *f = TFile::Open("root://eoscms//eos/cms/' >> TempCounter.C
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

cp number.txt /afs/cern.ch/user/d/dnash/CMSSW_5_0_0/src/NTupleAnalyzer/tools/EventCountCheck/LogFiles/WJetsToLNu_TuneZ2_matchingup/Log_59.txt
# ^ Another placeholder that will be changed by a sed comand