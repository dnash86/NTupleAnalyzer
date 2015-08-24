#!/usr/bin/python
from ROOT import *
import array
import math
tRand = TRandom3()
from random import randint
import os

### This contains the fucntions that return various objects used in the NTupleAnalyzer
#   There are more complicated functions that return muons/jets from LQ decays 
#   There are also simple functions, such as one that returns an MET-vector, creates a PDF weight list
#   The function for vertex counting is here too, it may need work from 2012 to adapt for 2015



def MuonsFromLQ(T):
	# Purpose: Testing. Get the muons from LQ decays and find the matching reco muons. 
	#         Return TLorentzVectors of the gen and reco muons, and the indices for
	#         the recomuons as well.
	muons = []
	genmuons=[]
	recomuoninds = []
	for n in range(len(T.MuonPt)):	
		m = TLorentzVector()
		m.SetPtEtaPhiM(T.MuonPt[n],T.MuonEta[n],T.MuonPhi[n],0)
		muons.append(m)
	for n in range(len(T.GenParticlePdgId)):
		pdg = T.GenParticlePdgId[n]
		if pdg not in [13,-13]:
			continue
		motherIndex = T.GenParticleMotherIndex[n]
		
		motherid = 0
		if motherIndex>-1:
			motherid = T.GenParticlePdgId[motherIndex]
			#print 'pdgId:',pdg,'index:',T.GenParticleMotherIndex[n],'mother pdgId:',T.GenParticlePdgId[motherIndex]
		if motherid not in [42,-42]:
			continue	
		m = TLorentzVector()
		m.SetPtEtaPhiM(T.GenParticlePt[n],T.GenParticleEta[n],T.GenParticlePhi[n],0.0)
		genmuons.append(m)
	
	matchedrecomuons=[]
	emptyvector = TLorentzVector()
	emptyvector.SetPtEtaPhiM(0,0,0,0)
	#print 'number of genmuons:',len(genmuons)
	for g in genmuons:
		bestrecomuonind=-1
		mindr = 99999
		ind=-1
		for m in muons:
			ind+=1
			dr = abs(m.DeltaR(g))
			if dr<mindr:
				mindr =dr
				bestrecomuonind=ind
		if mindr<0.4:
			matchedrecomuons.append(muons[bestrecomuonind])
			recomuoninds.append(bestrecomuonind)
		else:
			matchedrecomuons.append(emptyvector)
			recomuoninds.append(-99)
		#print mindr, muons[bestrecomuonind].Pt(), g.Pt()
	while len(recomuoninds)<2 :
		recomuoninds.append(-99)
	return([genmuons,matchedrecomuons,recomuoninds])
	#return(recomuoninds)

def JetsFromLQ(T):
	# Purpose: Testing. Get the quarks from LQ decays and find the matching reco pfJets. 
	#         Return TLorentzVectors of the gen and reco jets, and the indices for
	#         the recojets as well.
	jets = []
	genjets=[]
	recojetinds = []
	for n in range(len(T.PFJetPt)):	
		if  T.PFJetPassLooseID[n]==1 and T.PFJetPt[n]>30 and abs(T.PFJetEta[n])<2.4 : #morse only use jets that pass id
			m = TLorentzVector()
			m.SetPtEtaPhiM(T.PFJetPt[n],T.PFJetEta[n],T.PFJetPhi[n],0)
			jets.append(m)
	for n in range(len(T.GenParticlePdgId)):
		pdg = T.GenParticlePdgId[n]
		if pdg not in [4,-4]: #Get charm quarks
			continue
		motherIndex = T.GenParticleMotherIndex[n]
		motherid = 0
		if motherIndex>-1:
			motherid = T.GenParticlePdgId[motherIndex]
		if motherid not in [42,-42]:
			continue	
		m = TLorentzVector()
		m.SetPtEtaPhiM(T.GenParticlePt[n],T.GenParticleEta[n],T.GenParticlePhi[n],0.0)
		genjets.append(m)
	
	matchedrecojets=[]
	emptyvector = TLorentzVector()
	emptyvector.SetPtEtaPhiM(0,0,0,0)
	for g in genjets:
		bestrecojetind=-1
		mindr = 99999
		ind=-1
		for m in jets:
			ind+=1
			dr = abs(m.DeltaR(g))
			if dr<mindr:
				mindr =dr
				bestrecojetind=ind
		if mindr<0.6:
			matchedrecojets.append(jets[bestrecojetind])
			recojetinds.append(bestrecojetind)
		else:
			matchedrecojets.append(emptyvector)
			recojetinds.append(-99)
		#print mindr, jets[bestrecojetind].Pt(), g.Pt()
	while len(recojetinds)<2 :
		recojetinds.append(-99)
	return([genjets,matchedrecojets,recojetinds])
	#return(recojetinds)



# def MuonsForJetSeparation(T):

# 	# Attempting to be the same as process.analysisPatMuons.finalCut = cms.string("isGlobalMuon & muonID('GlobalMuonPromptTight') & pt > 20")
# 	# GlobalTightPrompt is muon.isGlobalMuon() && muon.globalTrack()->normalizedChi2() < 10. && muon.globalTrack()->hitPattern().numberOfValidMuonHits() > 0
# 	muons = []
# 	for n in range(len(T.MuonPt)):
# 		Pass = True
# 		Pass *= T.MuonIsGlobal[n]
# 		Pass *= T.MuonGlobalChi2[n]<10.
# 		Pass *= T.MuonGlobalTrkValidHits[n]>=1
# 		Pass *= T.MuonPt[n] > 20.
# 		if Pass == True:
# 			ThisMu = TLorentzVector()
# 			ThisMu.SetPtEtaPhiM(T.MuonPt[n],T.MuonEta[n],T.MuonPhi[n],0)
# 			muons.append(ThisMu)
# 	return muons

# def TausForJetSeparation(T):
# 	# process.analysisPatTaus.preselection = cms.string(
# 	#     'tauID("decayModeFinding") > 0.5 &'
# 	#     ' tauID("byLooseCombinedIsolationDeltaBetaCorr3Hits") > 0.5 &'
# 	#     ' tauID("againstMuonLoose3") > 0.5 &'
# 	#     ' tauID("againstElectronLooseMVA3") > 0.5'
# 	# )
# 	# process.analysisPatTaus.finalCut = cms.string('pt > 20. & abs(eta) < 2.3')
# 	taus = []
# 	for n in range(len(T.HPSTauPt)):
# 		Pass = True
# 		Pass *= T.HPSTauDecayModeFindingDiscr[n] > 0.5
# 		Pass *= T.HPSTauLooseCombinedIsolationDeltaBetaCorr3HitsDiscr[n] > 0.5
# 		Pass *= T.HPSTauAgainstMuonLoose3Discr[n]>0.5
# 		Pass *= T.HPSTauAgainstElectronLooseMVA3Discr[n] > 0.5
# 		Pass *= (T.HPSTauEta[n] > -2.3)*(T.HPSTauEta[n] < 2.3)
# 		Pass *= T.HPSTauPt[n] > 20.
# 		if Pass == True:
# 			ThisTau = TLorentzVector()
# 			ThisTau.SetPtEtaPhiM(T.HPSTauPt[n],T.HPSTauEta[n],T.HPSTauPhi[n],0)
# 			taus.append(ThisTau)
# 	return taus


def MetVector(T):
	# Purpose: Creates a TLorentzVector represting the MET. No pseudorapidity, obviously.
	met = TLorentzVector()
	met.SetPtEtaPhiM(T.PFMETType01XYCor[0],0,T.PFMETPhiType01XYCor[0],0)
	return met



def GeomFilterCollection(collection_to_clean,good_collection,dRcut):
	# Purpose: Take a collection of TLorentzVectors that you want to clean (arg 1)
	#         by removing all objects within dR of dRcut (arg 3) of any element in
	#         the collection of other particles (arg 2)
	#         e.g.  argumments (jets,muons,0.3) gets rid of jets within 0.3 of muons. 
	output_collection = []
	for c in collection_to_clean:
		isgood = True
		for g in good_collection:
			if (c.DeltaR(g))<dRcut:
				isgood = False
		if isgood==True:
			output_collection.append(c)
	return output_collection


##########################################################################################
#################     Everything needed for PDF Weight variation   #######################
##########################################################################################



def GetPDFWeightVars(T):
	# Purpose: Determine all the branch names needed to store the PDFWeights 
	#         for CTEQ, MSTW, and NNPDF in flat (non vector) form. 
	if T.isData:
		return []
	else:
		T.GetEntry(1)
		pdfweights=[]
		for x in range(len(T.PDFCTEQWeights)):
			pdfweights.append('factor_cteq_'+str(x+1))
		for x in range(len(T.PDFMSTWWeights)):
			pdfweights.append('factor_mstw_'+str(x+1))		
		for x in range(len(T.PDFNNPDFWeights)):
			pdfweights.append('factor_nnpdf_'+str(x+1))			
		return pdfweights




def GetPDFWeights(T):
	# Purpose: Gather the pdf weights into a single list. 	
	_allweights = []
	_allweights += T.PDFCTEQWeights
	_allweights += T.PDFNNPDFWeights
	_allweights += T.PDFMSTWWeights
	return _allweights



##########################################################################################
#################     Everything needed for Pileup reweighting     #######################
##########################################################################################



def GetPURescalingFactors(puversion):
	# Purpose: To get the pileup reweight factors from the PU_Central.root, PU_Up.root, and PU_Down.root files.
	#         The MC Truth distribution is taken from https://twiki.cern.ch/twiki/bin/view/CMS/PileupMCReweightingUtilities

	MCDistSummer12 = [2.560E-06, 5.239E-06, 1.420E-05, 5.005E-05, 1.001E-04, 2.705E-04, 1.999E-03, 6.097E-03, 1.046E-02, 1.383E-02, 
                      1.685E-02, 2.055E-02, 2.572E-02, 3.262E-02, 4.121E-02, 4.977E-02, 5.539E-02, 5.725E-02, 5.607E-02, 5.312E-02, 5.008E-02, 4.763E-02, 
                      4.558E-02, 4.363E-02, 4.159E-02, 3.933E-02, 3.681E-02, 3.406E-02, 3.116E-02, 2.818E-02, 2.519E-02, 2.226E-02, 1.946E-02, 1.682E-02, 
                      1.437E-02, 1.215E-02, 1.016E-02, 8.400E-03, 6.873E-03, 5.564E-03, 4.457E-03, 3.533E-03, 2.772E-03, 2.154E-03, 1.656E-03, 1.261E-03, 
                      9.513E-04, 7.107E-04, 5.259E-04, 3.856E-04, 2.801E-04, 2.017E-04, 1.439E-04, 1.017E-04, 7.126E-05, 4.948E-05, 3.405E-05, 2.322E-05, 
                      1.570E-05, 5.005E-06]

    # This is the standard (all of 2012) pileup scenario
	if puversion =='Basic':
		f_pu_up = TFile("PU_Up.root","read")
		h_pu_up = f_pu_up.Get('pileup')
		f_pu_down = TFile("PU_Down.root","read")
		h_pu_down = f_pu_down.Get('pileup')
		f_pu_central = TFile("PU_Central.root","read")
		h_pu_central = f_pu_central.Get('pileup')
		#h_pu_up = TFile.Open("PU_Up.root",'read').Get('pileup')
		#h_pu_down = TFile.Open("PU_Down.root",'read').Get('pileup')
		#h_pu_central = TFile("PU_Central.root",'read').Get('pileup')

	# This is just for 2012D. It was used for some studies. Not that important.
	if puversion =='2012D':
		f_pu_up = TFile("PU_Up_2012D.root","read")
		h_pu_up = f_pu_up.Get('pileup')
		f_pu_down = TFile("PU_Down_2012D.root","read")
		h_pu_down = f_pu_down.Get('pileup')
		f_pu_central = TFile("PU_Central_2012D.root","read")
		h_pu_central = f_pu_central.Get('pileup')
		#h_pu_up = TFile.Open("PU_Up_2012D.root").Get('pileup')
		#h_pu_down = TFile.Open("PU_Down_2012D.root",'read').Get('pileup')
		#h_pu_central = TFile.Open("PU_Central_2012D.root",'read').Get('pileup')

	# Arrays for the central and up/down variation weights.
	bins_pu_central = []
	bins_pu_up = []
	bins_pu_down = []

	# Loop over bins and put content in arrays
	for x in range(h_pu_up.GetNbinsX()):
		bin = x +1
		bins_pu_central.append(h_pu_central.GetBinContent(bin))
		bins_pu_up.append(h_pu_up.GetBinContent(bin))
		bins_pu_down.append(h_pu_down.GetBinContent(bin))

	# Sum bins for proper normalizations
	total_pu_central = sum(bins_pu_central)
	total_pu_up = sum(bins_pu_up)
	total_pu_down = sum(bins_pu_down)
	total_mc = sum(MCDistSummer12)

	# Get normalized bins
	bins_pu_central_norm = [x/total_pu_central for x in bins_pu_central]
	bins_pu_up_norm = [x/total_pu_up for x in bins_pu_up]
	bins_pu_down_norm = [x/total_pu_down for x in bins_pu_down]
	bins_mc_norm  = [x/total_mc for x in MCDistSummer12]

	# Arrays for scale factors (central and systematic varied)
	scale_pu_central = []
	scale_pu_up = []
	scale_pu_down = []

	# Fill arrays of scale factors
	for x in range(len(bins_mc_norm)):
		scale_pu_central.append(bins_pu_central_norm[x]/bins_mc_norm[x])
		scale_pu_up.append(bins_pu_up_norm[x]/bins_mc_norm[x])
		scale_pu_down.append(bins_pu_down_norm[x]/bins_mc_norm[x])

	# Return arrays of scale factors
	return [scale_pu_central, scale_pu_up, scale_pu_down]

# Use the above function to get the pu weights
[CentralWeights,UpperWeights,LowerWeights] =GetPURescalingFactors('Basic')
[CentralWeights_2012D,UpperWeights_2012D,LowerWeights_2012D] =GetPURescalingFactors('2012D')




def GetPUWeight(T,version,puversion):
	# Purpose: Get the pileup weight for an event. Version can indicate the central
	#         weight, or the Upper or Lower systematics. Needs to be updated for
	#         input PU histograms given only the generated disribution........	

	# Only necessary for MC
	if T.isData:
		return 1.0

	# Getting number of PU interactions, start with zero.	
	N_pu = 0

	# Set N_pu to number of true PU interactions in the central bunch
	for n in range(len(T.PileUpInteractionsTrue)):
		if abs(T.PileUpOriginBX[n]==0):
			N_pu = int(1.0*(T.PileUpInteractionsTrue[n]))

	puweight = 0

	# Assign the list of possible PU weights according to what is being done
	# Central systematics Up, or systematic down
	if puversion=='Basic':
		puweights = CentralWeights
		if version=='SysUp':
			puweights=UpperWeights
		if version=='SysDown':
			puweights=LowerWeights

	# Also possible to do just for 2012D, for cross-checks. 
	if puversion=='2012D':
		puweights = CentralWeights_2012D
		if version=='SysUp':
			puweights=UpperWeights_2012D
		if version=='SysDown':
			puweights=LowerWeights_2012D


	# Make sure there exists a weight for the number of interactions given, 
	# and set the puweight to the appropriate value.
	NRange = range(len(puweights))
	if N_pu in NRange:
		puweight=puweights[N_pu]
	# print puweight
	return puweight


def CountVertices(T):
	vertices = 0
	for v in range(len(T.VertexZ)):
		if ( T.VertexIsFake[v] == True ) :  continue
		if ( T.VertexNDF[v] <= 4.0 ) :  continue
		if ( abs(T.VertexZ[v]) > 24.0 ) :  continue
		if ( abs(T.VertexRho[v]) >= 2.0 ) :  continue
		vertices += 1
	return vertices	


def GetRunLumiList():
	# Purpose: Parse the json file to get a list of good runs and lumis 
	#          to call on later. For real data only.
	jfile = open(options.json,'r')	
	flatjson = ''
	for line in jfile:
		flatjson+=line.replace('\n','')
	flatjson = flatjson.replace("}","")
	flatjson = flatjson.replace("{","")
	flatjson = flatjson.replace(":","")
	flatjson = flatjson.replace(" ","")
	flatjson = flatjson.replace("\t","")

	jinfo = flatjson.split('"')
	strjson = ''
	for j in jinfo:
		strjson += j
	strjson = strjson.replace('\n[',' [')
	strjson = strjson.replace(']],',']]\n')
	strjson = strjson.replace('[[',' [[')

	pairs = []
	for line in strjson.split('\n'):
		pair = []
		line = line.split(' ')
		exec('arun = '+line[0])
		exec('alumis = '+line[1])
		verboselumis = []
		for r in alumis:
			verboselumis +=  range(r[0],r[1]+1)

		pair.append(arun)
		pair.append(verboselumis)
		pairs.append(pair)
	return pairs


