#!/usr/bin/python
from ROOT import *
import array
import math
tRand = TRandom3()
from random import randint
import os

### This python file contains the set of functions that are used to apply objection identification criteria
#   It also contains functions needed by those functions, such as propagation of pT to MET, and the JERModifiedPt function
#   NOTE: These functions should likely remain identical between like analyses (LQ analyses), as object criteria and variations will be the same
#   Edit this only to change object criteria and object pT scale and resolution schemes
#   NOTE: The PassTrigger and CheckRunLumiCert function is in this file as well (they are essentially bool filters, as are the ID functions

newntupleswitch = True#'V00-03-18' in name
if newntupleswitch == True:
	print 'Detected V00-03-18 ntuple - making small tweaks to handle this!'


### The TightHighPtIdMuons function, moved here from NTupleAnalyzer.py
def TightHighPtIDMuons(T,_met,variation,isdata,alignementcorrswitch,nonisoswitch):
	# Purpose: Gets the collection of muons passing tight muon ID. 
	#         Returns muons as TLorentzVectors, and indices corrresponding
	#         to the surviving muons of the muon collection. 
	#         Also returns modified MET for systematic variations.
	muons = []
	muoninds = []
	if variation=='MESup':	
		#_MuonCocktailPt = [(pt + pt*(0.05*pt/1000.0)) for pt in T.MuonCocktailPt]
		_MuonCocktailPt = [(pt + pt*(0.05*pt/1000.0)) for pt in T.MuonPt]
	elif variation=='MESdown':	
		#_MuonCocktailPt = [(pt - pt*(0.05*pt/1000.0)) for pt in T.MuonCocktailPt]
		_MuonCocktailPt = [(pt - pt*(0.05*pt/1000.0)) for pt in T.MuonPt]
	elif variation=='MER':	
		#_MuonCocktailPt = [pt+pt*tRand.Gaus(0.0,  0.01*(pt<=200.0) + (0.04)*(pt>200.0) ) for pt in T.MuonCocktailPt]
		_MuonCocktailPt = [pt+pt*tRand.Gaus(0.0,  0.01*(pt<=200.0) + (0.04)*(pt>200.0) ) for pt in T.MuonPt]
	else:	
		#_MuonCocktailPt = [pt for pt in T.MuonPt]	
		_MuonCocktailPt = [pt for pt in T.MuonPt]	

	if (isdata):
		#_MuonCocktailPt = [pt for pt in T.MuonCocktailPt]	
		_MuonCocktailPt = [pt for pt in T.MuonPt]	

	trk_isos = []
	charges = []
	deltainvpts = []

	chi2 = []
	pfid = []
	layers = []

	nequiv = []
	for n in range(len(T.MuonPt)):
            if T.MuonIsGlobal[n] or newntupleswitch==True:
                nequiv.append(n)

	# Loop over muons using the pT array from above
	for n in range(len(_MuonCocktailPt)):

		# Some muon alignment studies use the inverse diff of the high pT and Trk pT values
		deltainvpt = -1.0	
		if ( T.MuonTrkPt[nequiv[n]] > 0.0 ) and (_MuonCocktailPt[n]>0.0):
			deltainvpt = ( 1.0/T.MuonTrkPt[nequiv[n]] - 1.0/_MuonCocktailPt[n])
	
		# For alignment correction studies in MC, the pT is modified according to
		# parameterizations of the position
		if alignementcorrswitch == True and isdata==False:
			if abs(deltainvpt) > 0.0000001:
				__Pt_mu = _MuonCocktailPt[n]
				#__Eta_mu = T.MuonCocktailEta[n]
				__Eta_mu = T.MuonEta[n]
				#__Phi_mu = T.MuonCocktailPhi[n]
				__Phi_mu = T.MuonPhi[n]
				__Charge_mu = T.MuonCharge[nequiv[n]]
				#if (__Pt_mu >200)*(abs(__Eta_mu) < 0.9)      : 
					#_MuonCocktailPt[n] =  ( (1.0) / ( -5e-05*__Charge_mu*sin(-1.4514813+__Phi_mu ) + 1.0/__Pt_mu ) ) 
				deltainvpt = ( 1.0/T.MuonTrkPt[nequiv[n]] - 1.0/_MuonCocktailPt[n])


		# For the ID, begin by assuming it passes. Veto if it fails any condition
		# High PT conditions from https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMuonId
		# NTuple definitions in https://raw.githubusercontent.com/CMSLQ/RootTupleMakerV2/master/src/RootTupleMakerV2_Muons.cc
		Pass = True
		# A preliminary pT cut. This also encompasses the GlobalMuon conditions, since
		# all non-global muosn have cocktail pT of -1 in the ntuples.
		Pass *= (_MuonCocktailPt[n] > 35)      
		# Eta requirement matches trigger.
		Pass *= abs(T.MuonEta[n])<2.1    

		# Number of valid hits
		Pass *= T.MuonGlobalTrkValidHits[nequiv[n]]>=1

		# Number of station matches
		Pass *= T.MuonStationMatches[nequiv[n]]>1 

		# Impact parameters
		# Pass *= abs(T.MuonCocktailTrkVtxDXY[n]) < 0.2     
		# Pass *= abs(T.MuonCocktailTrkVtxDZ[n]) < 0.5      
		Pass *= abs(T.MuonBestTrackVtxDistXY[nequiv[n]]) < 0.2     # Fixed
		Pass *= abs(T.MuonBestTrackVtxDistZ[nequiv[n]]) < 0.5      #Fixed 
		# Pixel hits
		Pass *= T.MuonTrkPixelHits[nequiv[n]]>=1  

		# Layers with measurement (high PT ID cut is 5, used to be tight id cut at 8)
		Pass *= T.MuonTrackLayersWithMeasurement[nequiv[n]] > 5 
		#Pass *= T.MuonCocktailPtError[n]/T.MuonCocktailPt[n]  < 0.3

		# Isolation condition using tracker-only isolation
		if nonisoswitch != True:
			Pass *= (T.MuonTrackerIsoSumPT[nequiv[n]]/_MuonCocktailPt[n])<0.1

		# Propagate MET changes if undergoing systematic variation
		if (Pass):
			NewMu = TLorentzVector()
			OldMu = TLorentzVector()
			#NewMu.SetPtEtaPhiM(_MuonCocktailPt[n],T.MuonCocktailEta[n],T.MuonCocktailPhi[n],0)
			NewMu.SetPtEtaPhiM(_MuonCocktailPt[n],T.MuonEta[n],T.MuonPhi[n],0)
			#OldMu.SetPtEtaPhiM(T.MuonCocktailPt[n],T.MuonCocktailEta[n],T.MuonCocktailPhi[n],0)
			OldMu.SetPtEtaPhiM(T.MuonPt[n],T.MuonEta[n],T.MuonPhi[n],0)
			_met = PropagatePTChangeToMET(_met,OldMu,NewMu)

			# Append items to retun if the muon is good

			muons.append(NewMu)
			trk_isos.append((T.MuonTrackerIsoSumPT[nequiv[n]]/_MuonCocktailPt[n]))
			chi2.append(T.MuonGlobalChi2[nequiv[n]])
			pfid.append(T.MuonIsPF[nequiv[n]])
			layers.append(T.MuonTrackLayersWithMeasurement[nequiv[n]])
			charges.append(T.MuonCharge[n])
			muoninds.append(n)
			deltainvpts.append(deltainvpt)

	return [muons,muoninds,_met,trk_isos,charges,deltainvpts,chi2,pfid,layers]




### The HEEPElectrons function, moved here from NTupleAnalyzer.py
def HEEPElectrons(T,_met,variation):
	# Purpose: Gets the collection of electrons passing HEEP ID. 
	#         Returns electrons as TLorentzVectors, and indices corrresponding
	#         to the surviving electrons of the electron collection. 
	#         Also returns modified MET for systematic variations.	
	electrons = []
	electroninds = []
	if variation=='EESup':	
		_ElectronPt = [pt*1.01 for pt in T.ElectronPtHeep]
	elif variation=='EESdown':	
		_ElectronPt = [pt*0.99 for pt in T.ElectronPtHeep]
	elif variation=='EER':	
		_ElectronPt = [pt+pt*tRand.Gaus(0.0,0.04) for pt in T.ElectronPtHeep]
	else:	
		_ElectronPt = [pt for pt in T.ElectronPtHeep]	

	for n in range(len(_ElectronPt)):
		Pass = True
		Pass *= (T.ElectronPtHeep[n] > 35)
		Pass *= abs(T.ElectronEta[n])<2.1

		barrel = (abs(T.ElectronSCEta[n]))<1.442
		endcap = (abs(T.ElectronSCEta[n]))>1.56 
		Pass *= (barrel+endcap)

		if barrel:
			Pass *= T.ElectronHasEcalDrivenSeed[n]
			Pass *= T.ElectronDeltaEtaTrkSC[n] < 0.005
			Pass *= T.ElectronDeltaPhiTrkSC[n] < 0.06
			Pass *= T.ElectronHoE[n] < 0.05
			Pass *= ((T.ElectronE2x5OverE5x5[n] > 0.94) or (T.ElectronE1x5OverE5x5[n] > 0.83) )
			#Pass *= (T.ElectronHcalIsoD1DR03[n] + T.ElectronEcalIsoDR03[n]) <  (2.0 + 0.03*_ElectronPt[n] + 0.28*T.rhoForHEEP)
			Pass *= T.ElectronTrkIsoDR03[n] < 5.0
			Pass *= T.ElectronMissingHits[n] <=1
			Pass *= T.ElectronLeadVtxDistXY[n]<0.02

		if endcap:
			Pass *= T.ElectronHasEcalDrivenSeed[n]
			Pass *= T.ElectronDeltaEtaTrkSC[n] < 0.007
			Pass *= T.ElectronDeltaPhiTrkSC[n] < 0.06
			Pass *= T.ElectronHoE[n] < 0.05
			Pass *= T.ElectronSigmaIEtaIEta[n] < 0.03
			#if _ElectronPt[n]<50:
				#Pass *= ((T.ElectronHcalIsoD1DR03[n] + T.ElectronEcalIsoDR03[n]) < (2.5 + 0.28*T.rhoForHEEP))
			#else:
				#Pass *= ((T.ElectronHcalIsoD1DR03[n] + T.ElectronEcalIsoDR03[n]) < (2.5 + 0.03*(_ElectronPt[n]-50.0) + 0.28*T.rhoForHEEP))
			Pass *= T.ElectronTrkIsoDR03[n] < 5.0
			Pass *= T.ElectronMissingHits[n] <=1
			Pass *= T.ElectronLeadVtxDistXY[n]<0.05

		if (Pass):
			NewEl = TLorentzVector()
			OldEl = TLorentzVector()
			NewEl.SetPtEtaPhiM(_ElectronPt[n],T.ElectronEta[n],T.ElectronPhi[n],0)
			OldEl.SetPtEtaPhiM(T.ElectronPtHeep[n],T.ElectronEta[n],T.ElectronPhi[n],0)
			met = PropagatePTChangeToMET(_met,OldEl,NewEl)

		Pass *= (_ElectronPt[n] > 35)
		if (Pass):
			electrons.append(NewEl)
			electroninds.append(n)
	return [electrons,electroninds,_met]




### The LooseIDJets function, moved here from NTupleAnalyzer.py
def LooseIDJets(T,met,variation,isdata):
	# Pupose: Gets the collection of jets passing loose PFJet ID. 
	#         Returns jets as TLorentzVectors, and indices corrresponding
	#         to the surviving jetss of the jet collection. 
	#         Also returns modified MET for systematic variations.	

	if variation!='JERup' and variation!='JERdown':
		# _PFJetPt = [JERModifiedPt(T.PFJetPt[n],T.PFJetEta[n],T.PFJetPhi[n],T,'') for n in range(len(T.PFJetPt))] 	
		 _PFJetPt = [pt for pt in T.PFJetPt]				
	if variation=='JERup':	
		_PFJetPt = [JERModifiedPt(T.PFJetPt[n],T.PFJetEta[n],T.PFJetPhi[n],T,'up') for n in range(len(T.PFJetPt))] 
	if variation=='JERdown':	
		_PFJetPt = [JERModifiedPt(T.PFJetPt[n],T.PFJetEta[n],T.PFJetPhi[n],T,'down') for n in range(len(T.PFJetPt))] 		

	if variation=='JESup':	
		_PFJetPt = [ _PFJetPt[n]*(1.0+T.PFJetJECUnc[n]) for n in range(len(_PFJetPt))]
	if variation=='JESdown':	
		_PFJetPt = [ _PFJetPt[n]*(1.0-T.PFJetJECUnc[n]) for n in range(len(_PFJetPt))]

	if (isdata):
		_PFJetPt = [pt for pt in T.PFJetPt]	

	# print met.Pt(),


	JetFailThreshold=0.0

	jets=[]
	jetinds = []
	NHF = []
	NEMF = []
	for n in range(len(_PFJetPt)):
		if _PFJetPt[n]>30 and abs(T.PFJetEta[n])<2.4 :
			if T.PFJetPassLooseID[n]==1:
				j = TLorentzVector()
				j.SetPtEtaPhiM(_PFJetPt[n],T.PFJetEta[n],T.PFJetPhi[n],0)
				oldjet = TLorentzVector()
				oldjet.SetPtEtaPhiM(T.PFJetPt[n],T.PFJetEta[n],T.PFJetPhi[n],0)				
				met = PropagatePTChangeToMET(met,oldjet,j)
				jets.append(j)
				jetinds.append(n)
				NHF.append(T.PFJetNeutralHadronEnergyFraction[n])
				NEMF.append(T.PFJetNeutralEmEnergyFraction[n])
			else:
				if _PFJetPt[n] > JetFailThreshold:
					JetFailThreshold = _PFJetPt[n]

	# print met.Pt()

	return [jets,jetinds,met,JetFailThreshold,NHF,NEMF]


### Moved here from NTupleAnalyzer.py, needed by the loose jets ID function above
def JERModifiedPt(pt,eta,phi,T,modtype):
	# Pupose: Modify reco jets based on genjets. Input is pt/eta/phi of a jet. 
	#         The jet will be matched to a gen jet, and the difference
	#         between reco and gen will be modified according to appropriate
	#         pt/eta dependent scale factors. 
	#         The modified jet PT is returned.
	#         https://hypernews.cern.ch/HyperNews/CMS/get/JetMET/1336.html
	#         https://twiki.cern.ch/twiki/bin/view/CMS/JetResolution
	bestn = -1
	bestdpt = 0
	bestdR = 9999999.9
	jet = TLorentzVector()
	jet.SetPtEtaPhiM(pt,eta,phi,0.0)
	for n in range(len(T.GenJetPt)):
		gjet = TLorentzVector()
		gjet.SetPtEtaPhiM(T.GenJetPt[n],T.GenJetEta[n],T.GenJetPhi[n],0.0)
		dR = abs(jet.DeltaR(gjet))
		if dR<bestdR and  dR<0.3 :
			bestdR = dR
			bestn = n
			bestdpt = pt-gjet.Pt()

	if bestdR>0.5:
		return pt

	abseta = abs(eta)
	if abseta >= 0   : jfacs = [  0.05200 , 0.11515 , -0.00900 ]
	if abseta >= 0.5 : jfacs = [  0.05700 , 0.11427 , 0.00200  ]
	if abseta >= 1.1 : jfacs = [  0.09600 , 0.16125 , 0.03400  ]
	if abseta >= 1.7 : jfacs = [  0.13400 , 0.22778 , 0.04900  ]
	if abseta >= 2.3 : jfacs = [  0.28800 , 0.48838 , 0.13500  ]

	if modtype == '':
		adjustmentfactor = jfacs[0]
	if modtype == 'up':
		adjustmentfactor = jfacs[1]
	if modtype == 'down':
		adjustmentfactor = jfacs[2]

	ptadjustment = adjustmentfactor*bestdpt
	pt += ptadjustment
	return pt



def PropagatePTChangeToMET(met,original_object,varied_object):
	# Purpose: This takes an input TLorentzVector met representing the missing ET
	#         (no eta component), and an original object (arg 2), which has been
	#         kinmatically modified for a systematic (arg 3), and modifies the 
	#         met to compensate for the change in the object.
	return  met + varied_object - original_object


def PassTrigger(T,trigger_identifiers,prescale_threshold):
	# Purpose: Return a flag (1 or 0) to indicate whether the event passes any trigger
	#         which is syntactically matched to a set of strings trigger_identifiers,
	#         considering only triggers with a prescale <= the prescale threshold.	
	for n in range(len(T.HLTInsideDatasetTriggerNames)):
		name = T.HLTInsideDatasetTriggerNames[n]
		consider_trigger=True

		for ident in trigger_identifiers:
			if ident not in name:
				consider_trigger=False
		if (consider_trigger==False) : continue

		prescale = T.HLTInsideDatasetTriggerPrescales[n]
		if prescale > prescale_threshold:
			consider_trigger=False
		if (consider_trigger==False) : continue

		decision = T.HLTInsideDatasetTriggerDecisions[n]
		if decision==True:
			return 1
	return 0	


def CheckRunLumiCert(r,l):
	# Purpose: Use the GoodRunLumis list, to check and see if a given
	#          run and lumi (r and l) are in the list. 
	GoodRunLumis = GetRunLumiList()
	for _rl in GoodRunLumis:
		if _rl[0]==r:
			for _l in _rl[1]:
				if _l == l:
					return True
	return False




