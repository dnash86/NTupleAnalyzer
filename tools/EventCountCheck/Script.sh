File=$1
rm Temp.C
echo "{" >> Temp.C
echo "  gROOT->Reset();" >> Temp.C
echo -n "  TFile *f = TFile::Open(" >> Temp.C
echo -n '"' >> Temp.C
echo -n "$File" >> Temp.C
echo -n '"' >> Temp.C
echo ");" >> Temp.C
echo -n "  TH1F* h =(TH1F*)f.Get(" >> Temp.C
echo -n '"/LJFilter/EventCount/EventCounter"' >> Temp.C
echo ");" >> Temp.C
echo "  std::cout<<h->GetBinContent(1)<<std::endl;" >> Temp.C
echo -n  "  gROOT->ProcessLine(" >> Temp.C
echo -n '".q"' >> Temp.C
echo ");" >> Temp.C
echo "}" >> Temp.C

root -l Temp.C > temp.txt
echo `gawk '(NR==3){print $1}' temp.txt`
rm temp.txt

