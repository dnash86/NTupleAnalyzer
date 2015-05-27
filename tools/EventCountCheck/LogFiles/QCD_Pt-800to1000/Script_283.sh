###############################################################
#Note: Do not modify this script, it is used by EventCounter.sh
###############################################################


File=/store/group/phys_exotica/leptonsPlusJets/RootNtuple/hsaka/RootNtuple-V00-03-11-Summer12MC_QCD_MuEnriched_PYTHIA_20130215_205103/QCD_Pt-800to1000_MuEnrichedPt5_TuneZ2star_8TeV_pythia6__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_355_1_hv8.root
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

cp number.txt /afs/cern.ch/user/d/dnash/CMSSW_5_0_0/src/NTupleAnalyzer/tools/EventCountCheck/LogFiles/QCD_Pt-800to1000/Log_283.txt
# ^ Another placeholder that will be changed by a sed comand