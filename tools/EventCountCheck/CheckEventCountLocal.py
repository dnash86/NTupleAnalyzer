import os

files = os.popen('ls *root').readlines()
files2 = []
for x in files:
	files2.append(x.replace('\n',''))
files2 = files

sets = []
setindex = []
totals = []
thisindex = 0

allfiles = len(files)

for x in range(1000):
	totals.append(0)

for x in range(len(files)):

	thistype = files[x].split('AODSIM')[0]

	if thistype not in sets:
		sets.append(thistype)
		setindex.append(thisindex)
		thisindex +=1

	f = open('temp.C','w')
	f.write('{\n\ngROOT->ProcessLine(\"gROOT->Reset()\");\nTFile *f = TFile::Open("'+files[x].replace('\n','')+'");\nTH1F* h = (TH1F*)f.Get("/LJFilter/EventCount/EventCounter");\nstd::cout<<h->GetBinContent(1)<<std::endl;\n\ngROOT->ProcessLine(".q");}\n\n')
	f.close()
	thisentry = os.popen('root -l temp.C ').readlines()[-1].replace('\n','')
	totals[thisindex] += float(thisentry)

	print str(x) +' / '+ str(allfiles) + ' files completed.'


for y in range(len(sets)):
	print sets[y] + ' , ' + str(totals[y+1])
