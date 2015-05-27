import sys
import os

# PU Twiki Example Distribution
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/PileupReweighting
genvaluesFlat10 = [0.0698146584, #0
0.0698146584, #1
0.0698146584, #2
0.0698146584, #3
0.0698146584, #4
0.0698146584, #5
0.0698146584, #6
0.0698146584, #7
0.0698146584, #8
0.0698146584, #9
0.0698146584, #10
0.0630151648, #11
0.0526654164, #12
0.0402754482, #13
0.0292988928, #14
0.0194384503, #15
0.0122016783, #16
0.007207042, #17						
0.004003637, #18
0.0020278322, #19
0.0010739954, #21
0.0004595759, #21
0.0002229748, #22
0.0001028162, #23
4.58337152809607E-05] #24


# PileUpInformation Twik Distribution
# Contact: Mike Hildreth
# Stated as useable for Spring11 and Summer11 MC samples
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/PileupInformation
genvaluesFlat10PlusTail = [ 0.069286816, #0
0.069286816, #1
0.069286816, #2
0.069286816, #3
0.069286816, #4
0.069286816, #5
0.069286816, #6
0.069286816, #7
0.069286816, #8
0.069286816, #9
0.069286816, #10
0.06518604 , #11
0.053861878, #12
0.040782032, #13
0.030135062, #14
0.019550796, #15
0.012264707, #16
0.007449117, #17
0.004502075, #18
0.002194605, #19
0.001166276, #20
0.000476543, #21
0.000188109, #22
7.52436E-05, #23
1.25406E-05  #24  
]

genvaluesFlat10PlusTailBugFix = [0.158209  , # 0
0.0918829  , # 1
0.0993907  , # 2
0.0987426  , # 3
0.0960109  , # 4
0.0911  , # 5
0.0835376  , # 6
0.0733272  , # 7
0.060944  , # 8
0.0478402  , # 9
0.035403  , # 10
0.0247308  , # 11
0.0162462  , # 12
0.0101034  , # 13
0.0059091  , # 14
0.0032846  , # 15
0.0017269  , # 16
0.0008738  , # 17
0.0004101  , # 18
0.0001874  , # 19
8.52e-05  , # 20
3.4e-05  , # 21
1.29e-05  , # 22
4.6e-06  , # 23
2e-06  , # 24
6e-07  , # 25
1e-07  , # 26
2e-07   # 27
]

genvaluesFlat10PlusTailMCDriven = [0.06111756549114,
0.06236929880448,
0.06198633024772,
0.07602171794776,
0.07126236742495,
0.07288371809767,
0.06948853202414,
0.07658293670127,
0.07787261552299,
0.07978183674999,
0.07194257579732,
0.0610149720796,
0.05221512760934,
0.03979500056216,
0.02561883971068,
0.01717481636248,
0.01029625604317,
0.00639585597571,
0.00312659277443,
0.00204959852715,
0.00044292011768,
0.00037790915564]

genvaluesSummmer11MCDriven = [
0.09665301589505,
0.05554598459082,
0.06286201152218,
0.06347122926355,
0.06396043589922,
0.06648962309988,
0.0676207399181,
0.06617623377525,
0.06433025612549,
0.06118643714861,
0.05614576247657,
0.05150364406191,
0.04656833483723,
0.04030686471854,
0.03210744776845,
0.02622530714236,
0.02101242451586,
0.0157206913306,
0.01210654542931,
0.00861567293677,
0.00705705559797,
0.0051418060665,
0.00322022627889,
0.00229183730131,
0.00122568890123,
0.00104950371347,
0.00073970292219,
0.0003276407302,
0.00019143194281,
0.00014610744777]

# Use Mike Hildreth's provided numbers by default:
genvalues = genvaluesFlat10PlusTail
genvalues = genvaluesSummmer11MCDriven

a = sys.argv
rootfile = ''
newgenvalues = []
distfile = ''
for x in range(len(a)):
	if a[x] == '-r':
		rootfile = a[x+1]

	if a[x] == '-f':
		distfile = a[x+1]
		os.system('wget '+distfile)
		distfile = distfile.split('/')[-1]
		info = os.popen('cat '+distfile).readlines()
		print info
		for y in info:
			if 'probValue' in y:
				genvalues2 = y
		genvalues2 = genvalues2.split('(')[-1]
		genvalues2 = genvalues2.split(')')[0]
		genvalues2 = genvalues2.split(',')
		for y in genvalues2:
			newgenvalues.append[float(y)]
		os.system('rm '+distfile)
		genvalues = newgenvalues
		
if rootfile == '':
	print 'No root file specified. Specify root file (from estimatePileUpD.py) with "-r rootfile.root".'
	sys.exit()
	
if distfile == '':
	print 'No generator distribution specified. Using default gen values for Spring11 MC'
	os.system('sleep 0')
	
#print rootfile
#print newgenvalues
#print distfile
	

f = open('GetDataValues.C','w')
f.write('{\n\n')

f.write('TFile f("'+rootfile+'");\n\n')
f.write('TH1D *h = (TH1D*)f->Get("pileup");\n\n')
#f.write('h->Draw();\n\n')

f.write('int nbinsx = h->GetXaxis()->GetNbins();\n\n')
f.write('Double_t ndat = -1.0;\n\nDouble_t ncenter = -1.0;')
f.write('for (int ibin=0;ibin<nbinsx;ibin++)\n	{\n	 ndat = 1.0*(h->GetBinContent(ibin));\n	 ncenter = 1.0*(h->GetBinCenter(ibin));\n	std::cout<<ncenter<<"	"<<ndat<<std::endl;\n\n	}\n\n')

f.write('	gROOT->Reset(); gROOT->ProcessLine(".q;");')
f.write('\n\n}\n\n')
f.close()

fileinfo = os.popen('root -l GetDataValues.C').readlines()

print 'Data Distribution Summary:\n'
print 'Bin     Contents'
for x in fileinfo:
	if 'Processing' not in x:
		print x.replace('\n','')
shortfileinfo = []

for x in	fileinfo:
	shortfileinfo.append(x.replace('\n',''))

print '\n\n'

datavalues = []

save = 0

for x in shortfileinfo:
	if save:
		center =	x.split()[0]
		if float(center) >=0:
			datavalues.append(float(x.split()[1]))
	if 'Processing GetDataValues.C' in x:
		save = 1
		

total = 0.0
for x in datavalues:
	total += x

normvalues = []

n = 0
for x in datavalues:

	if n<len(genvalues):
		normvalues.append(x/total)
	n = n + 1;

print '------------ Rescaling Factor Summary ------------\n'
print 'N_PU Bin    Rescale Factor\n'
n = 0
for x in range(len(normvalues)):
	print str(n) + '           ' + str(normvalues[x]/genvalues[x])
	n = n+1


print '\n\n'
print '------------         Rescaling Routine Code           ------------\n'
print '------------ NTupleAnalyzerV2 PlotMacros Compatible   ------------\n'

print 'cut_mc += "*(";';
makeplus = 1
n = 0
for x in range(len(normvalues)):
	n = n + 1
	factor =	normvalues[x]/genvalues[x]
	print 'cut_mc += "((N_PileUpInteractions > '+str(x-.5)+')*(N_PileUpInteractions < '+str(x+.5)+')*('+str(factor)+'))'+makeplus*'+'+'";'
	if n == (len(normvalues))-1:
		makeplus = 0
print 'cut_mc += ")";\n\n'


