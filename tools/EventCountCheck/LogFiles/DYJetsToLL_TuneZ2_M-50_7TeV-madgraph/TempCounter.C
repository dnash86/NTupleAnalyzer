{
  gROOT->Reset();
  TFile *f = TFile::Open(root://eoscms//eos/cms/"/store/group/phys_exotica/leptonsPlusJets/leptoquarks/NTuples_V00_02_06/RootNtuple-V00-02-06-Summer11MC_ZJets_MG_20110909_183645/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola__Summer11-PU_S4_START42_V11-v1__AODSIM_386_1_xHT.root");
  TH1F* h =(TH1F*)f.Get("/LJFilter/EventCount/EventCounter");
  std::cout<<h->GetBinContent(1)<<std::endl;
  gROOT->ProcessLine(".q");
}
