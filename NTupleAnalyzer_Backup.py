#!/usr/bin/python
from datetime import datetime
import sys
sys.argv.append( '-b True' )
from ROOT import *
import array
import math
#from optparse import OptionParser
import argparse
tRand = TRandom3()
from random import randint
import os



#### Import of important functions
from objectID import *
from variableComputation import *
from getComplexObjects import *

##########################################################################################
#################      SETUP OPTIONS - File, Normalization, etc    #######################
##########################################################################################

# Input Options - file, cross-section, number of vevents

def getArguments():
	parser = argparse.ArgumentParser(description='Analyzer for LQ root files')

	parser.add_option("-f", "--file", dest="filename", help="input root file", metavar="FILE")
	parser.add_option("-b", "--batch", dest="dobatch", help="run in batch mode", metavar="BATCH")
	parser.add_option("-s", "--sigma", dest="crosssection", help="specify the process cross-section", metavar="SIGMA")
	parser.add_option("-n", "--ntotal", dest="ntotal", help="total number of MC events for the sample", metavar="NTOTAL")
	parser.add_option("-l", "--lumi", dest="lumi", help="integrated luminosity for data taking", metavar="LUMI")
	parser.add_option("-j", "--json", dest="json", help="json file for certified run:lumis", metavar="JSON")
	parser.add_option("-d", "--dir", dest="dir", help="output directory", metavar="DIR")
	parser.add_option("-p", "--pdf", dest="pdf", help="option to produce pdf uncertainties", metavar="PDF")

	args_ = parser.parse_args()
	return args_


args=getArguments()
dopdf = int(args.pdf)==1

# Here we get the file name, and adjust it accordingly for EOS, castor, or local directory
name = args.filename
if '/store' in name:
	name = 'root://eoscms//eos/cms'+name
if '/castor/cern.ch' in name:
	name = 'rfio://'+name

# These are switches based on the tag name. 
# First is whether to change out a muon with an electron ( for e-mu ttbar samples)
emuswitch=False
if "EMuSwitch" in args.dir:
	emuswitch=True
# Turn of the isolation condition for QCD studies
nonisoswitch=False
if "NonIso" in args.dir:
	nonisoswitch = True
# Quick test means no systematics
quicktestswitch = False
if "QuickTest" in args.dir:
	quicktestswitch = True
# Modifications of muon pT due to muon aligment mismodelling.
alignementcorrswitch = False
if "AlignmentCorr" in args.dir:
	alignementcorrswitch = True

print 'EMu Switch = ', emuswitch
print 'NonIso Switch = ', nonisoswitch
print 'Quick Switch (No Sys) = ', quicktestswitch
print 'AlignmentCorr Switch = ', alignementcorrswitch


# Typical event weight, sigma*lumi/Ngenerated
startingweight = float(args.crosssection)*float(args.lumi)/float(args.ntotal)

# Get the file, tree, and number of entries
print name
newntupleswitch = True#'V00-03-18' in name
if newntupleswitch == True:
	print 'Detected V00-03-18 ntuple - making small tweaks to handle this!'

fin = TFile.Open(name,"READ")
to = fin.Get("rootTupleTree/tree")
No = to.GetEntries()

# Here we are going to pre-skim the file to reduce running time.
indicator = ((name.split('_'))[-1]).replace('.root','')

junkfile1 = str(randint(100000000,1000000000))+indicator+'junk.root'

# At least one 100 GeV PFJet
fj1 = TFile.Open(junkfile1,'RECREATE')
t1 = to.CopyTree('PFJetPt[]>110')
# t1 = to.CopyTree('(1)')
Nj1 = t1.GetEntries()

junkfile2 = str(randint(100000000,1000000000))+indicator+'junk.root'

# At least one 40 GeV muon
fj2 = TFile.Open(junkfile2,'RECREATE')
t = t1.CopyTree('MuonPt[]>42')
N = t.GetEntries()

# PRint the reduction status
print 'Original events:          ',No
print 'After demand 1 pT110 jet: ',Nj1
print 'After demand 1 pt42 muon: ',N

##########################################################################################
#################      PREPARE THE VARIABLES FOR THE OUTPUT TREE   #######################
##########################################################################################

# Branches will be created as follows: One branch for each kinematic variable for each 
# systematic variation determined in _variations. One branch for each weight and flag.
# So branch names will include weight_central, run_number, Pt_muon1, Pt_muon1MESUP, etc.

_kinematicvariables = ['Pt_muon1','Pt_muon2','Pt_ele1','Pt_ele2','Pt_jet1','Pt_jet2','Pt_miss']
_kinematicvariables += ['Eta_muon1','Eta_muon2','Eta_ele1','Eta_ele2','Eta_jet1','Eta_jet2','Eta_miss']
_kinematicvariables += ['Phi_muon1','Phi_muon2','Phi_ele1','Phi_ele2','Phi_jet1','Phi_jet2','Phi_miss']
_kinematicvariables += ['X_miss','Y_miss']
_kinematicvariables += ['TrkIso_muon1','TrkIso_muon2']
_kinematicvariables += ['Chi2_muon1','Chi2_muon2']
_kinematicvariables += ['PFID_muon1','PFID_muon2']
_kinematicvariables += ['TrkMeasLayers_muon1','TrkMeasLayers_muon2']
_kinematicvariables += ['Charge_muon1','Charge_muon2']
_kinematicvariables += ['TrkGlbDpt_muon1','TrkGlbDpt_muon2']
_kinematicvariables += ['NHEF_jet1','NHEF_jet2','NEMEF_jet1','NEMEF_jet2']
_kinematicvariables += ['St_uujj','St_uvjj']
_kinematicvariables += ['St_eejj','St_evjj']
_kinematicvariables += ['M_uu','MT_uv']
_kinematicvariables += ['DR_muon1muon2','DPhi_muon1met','DPhi_jet1met','DPhi_jet2met']
_kinematicvariables += ['DR_muon1jet1','DR_muon1jet2','DR_muon2jet1','DR_muon2jet2']
_kinematicvariables += ['DPhi_muon1jet1','DPhi_muon1jet2','DPhi_muon2jet1','DPhi_muon2jet2']
_kinematicvariables += ['M_uujj1_gen','M_uujj2_gen','M_uujjavg_gen']
_kinematicvariables += ['M_uujj1_genMatched','M_uujj2_genMatched','M_uujjavg_genMatched']
_kinematicvariables += ['M_uujj1_3jet','M_uujj2_3jet','M_uujjavg_3jet']
_kinematicvariables += ['M_uujj1_3jet_rel','M_uujj2_3jet_rel','M_uujjavg_3jet_rel']
_kinematicvariables += ['M_uujj1','M_uujj2','M_uujjavg']
_kinematicvariables += ['M_uujj1_rel','M_uujj2_rel','M_uujjavg_rel']
_kinematicvariables += ['MT_uvjj1','MT_uvjj2','M_uvjj','MT_uvjj']
_kinematicvariables += ['MH_uujj','MH_uvjj']
_kinematicvariables += ['M_eejj1','M_eejj2','MT_evjj1','MT_evjj2','M_evjj','MT_evjj']
_kinematicvariables += ['JetCount','MuonCount','ElectronCount','GenJetCount']
_kinematicvariables += ['IsMuon_muon1','IsMuon_muon2']
_kinematicvariables += ['muonIndex1','muonIndex2']
_kinematicvariables += ['jetIndex1','jetIndex2']
_weights = ['weight_nopu','weight_central', 'weight_pu_up', 'weight_pu_down','weight_central_2012D']
_flags = ['run_number','event_number','lumi_number','pass_HLTMu40_eta2p1','GoodVertexCount']
_flags += ['passPrimaryVertex','passBeamScraping','passHBHENoiseFilter','passBPTX0','passBeamHalo','passTrackingFailure','passTriggerObjectMatching','passDataCert']
_flags += ['passBadEESuperCrystal','passEcalDeadCellBE','passEcalDeadCellTP','passEcalLaserCorr','passHcalLaserEvent','passPhysDeclared']
_variations = ['','JESup','JESdown','MESup','MESdown','JERup','JERdown','MER']
# _variations = ['','JESup','JESdown','MESup','MESdown','EESup','EESdown','JER','MER','EER']
if nonisoswitch==True or emuswitch==True or quicktestswitch==True:
	print 'NOT performing systematics...'
	_variations = ['']  # For quicker tests
# _variations = ['']  # For quicker tests


# Get the appropriate numbers of PDF weights from the tree
_pdfweightsnames = GetPDFWeightVars(t)



##########################################################################################
#################         Prepare the Output Tree                  #######################
##########################################################################################

# First create the output file. 
tmpfout = str(randint(100000000,1000000000))+indicator+'.root'
if '/store' in name:
	finalfout = args.dir+'/'+(name.split('/')[-2]+'__'+name.split('/')[-1].replace('.root','_tree.root'))
else:
	finalfout = args.dir+'/'+name.replace('.root','_tree.root')

# Create the output file and tree "PhysicalVariables"
fout = TFile.Open(tmpfout,"RECREATE")
tout=TTree("PhysicalVariables","PhysicalVariables")


# Below all the branches are created, everything is a double except for flags
# for b in _kinematicvariables:
# 	for v in _variations:
# 		exec(b+v+' = array.array("f",[0])')
# 		exec('tout.Branch("'+b+v+'",'+b+v+',"'+b+v+'/F")' )
# for b in _weights:
# 	exec(b+' = array.array("f",[0])')
# 	exec('tout.Branch("'+b+'",'+b+',"'+b+'/F")' )
# if dopdf:
# 	for b in _pdfweights:
# 		exec(b+' = array.array("f",[0])')
# 		print (b+' = array.array("f",[0])')
# 		exec('tout.Branch("'+b+'",'+b+',"'+b+'/F")' )
# for b in _flags:
# 	exec(b+' = array.array("L",[0])')
# 	exec('tout.Branch("'+b+'",'+b+',"'+b+'/i")' )

Branches = {}
for b in _kinematicvariables:
	for v in _variations:
		Branches[b+v] = array.array("f",[0])
		tout.Branch(b+v,Branches[b+v],b+v+"/F")
for b in _weights:
	Branches[b] = array.array("f",[0])
	tout.Branch(b,Branches[b],b+"/F")
if dopdf:
	for b in _pdfweightsnames:
		Branches[b] = array.array("f",[0])
		tout.Branch(b,Branches[b],b+"/F")
for b in _flags:
	Branches[b] = array.array("L",[0])
	tout.Branch(b,Branches[b],b+"/i")




##########################################################################################
#################           SPECIAL FUNCTIONS FOR ANALYSIS         #######################
##########################################################################################

def PrintBranchesAndExit(T):
	# Purpose: Just list the branches on the input file and bail out. 
	#         For coding and debugging
	x = T.GetListOfBranches()
	for n in x:
		print n
	sys.exit()

# PrintBranchesAndExit(t)

##########################################################################################
###########      FULL CALCULATION OF ALL VARIABLES, REPEATED FOR EACH SYS   ##############
##########################################################################################

def FullKinematicCalculation(T,variation):
	# Purpose: This is the magic function which calculates all kinmatic quantities using
	#         the previous functions. It returns them as a simple list of doubles. 
	#         It will be used in the loop over events. The 'variation' argument is passed
	#         along when getting the sets of leptons and jets, so the kinematics will vary.
	#         This function is repeated for all the sytematic variations inside the event
	#         loop. The return arguments ABSOLUELY MUST be in the same order they are 
	#         listed in the branch declarations. Modify with caution.  

	# MET as a vector
	met = MetVector(T)
	# ID Muons,Electrons
	[muons,goodmuoninds,met,trkisos,charges,dpts,chi2,pfid,layers] = TightHighPtIDMuons(T,met,variation,T.isData,alignementcorrswitch,nonisoswitch)
	# muons_forjetsep = MuonsForJetSeparation(T)
	# taus_forjetsep = TausForJetSeparation(T)
	[electrons,electroninds,met] = HEEPElectrons(T,met,variation)
	# ID Jets and filter from muons
	[jets,jetinds,met,failthreshold,neutralhadronEF,neutralemEF] = LooseIDJets(T,met,variation,T.isData)
	# jets = GeomFilterCollection(jets,muons_forjetsep,0.5)
	jets = GeomFilterCollection(jets,muons,0.5)
	jets = GeomFilterCollection(jets,electrons,0.5)
	# jets = GeomFilterCollection(jets,taus_forjetsep,0.5)
	# Empty lorenz vector for bookkeeping
	EmptyLorentz = TLorentzVector()
	EmptyLorentz.SetPtEtaPhiM(.01,0,0,0)

	# Muon and Jet Counts
	_mucount = len(muons)
	_elcount = len(electrons)
	_jetcount = len(jets)

	# Make sure there are two of every object, even if zero
	if len(muons) < 1 : 
		muons.append(EmptyLorentz)
		trkisos.append(0.0)
		charges.append(0.0)
		dpts.append(-1.0)
		chi2.append(-1.0)
		pfid.append(-1.0)
		layers.append(-1.0)

	if len(muons) < 2 : 
		muons.append(EmptyLorentz)
		trkisos.append(0.0)
		charges.append(0.0)		
		dpts.append(-1.0)
		chi2.append(-1.0)
		pfid.append(-1.0)
		layers.append(-1.0)

	if len(electrons) < 1 : electrons.append(EmptyLorentz)
	if len(electrons) < 2 : electrons.append(EmptyLorentz)	
	if len(jets) < 1 : 
		jets.append(EmptyLorentz)
		neutralhadronEF.append(0.0)
		neutralemEF.append(0.0)
	if len(jets) < 2 : 
		jets.append(EmptyLorentz)
		neutralhadronEF.append(0.0)
		neutralemEF.append(0.0)		

	_ismuon_muon1 = 1.0
	_ismuon_muon2 = 1.0

	if emuswitch == True:
		if muons[0].Pt() > electrons[0].Pt():
			muons[1] = electrons[0]
			_ismuon_muon2 = 0.0
		else:
			muons[1] = muons[0]
			muons[0] = electrons[0]
			_ismuon_muon1=0.0

	[_genMuons,_matchedRecoMuons,muonInd] = MuonsFromLQ(T)
	[_genJets,_matchedRecoJets,jetInd] = JetsFromLQ(T)
	#print 'muon index:',muonInd,'  jet index:',jetInd
	_muonInd1=muonInd[0]
	_muonInd2=muonInd[1]
	_jetInd1=jetInd[0]
	_jetInd2=jetInd[1]

	#[_Muujj1_gen,_Muujj2_gen]=GetLLJJMassesGen(muonInd,jetInd);


	# Get kinmetic quantities
	[_ptmu1,_etamu1,_phimu1,_isomu1,_qmu1,_dptmu1] = [muons[0].Pt(),muons[0].Eta(),muons[0].Phi(),trkisos[0],charges[0],dpts[0]]
	[_ptmu2,_etamu2,_phimu2,_isomu2,_qmu2,_dptmu2] = [muons[1].Pt(),muons[1].Eta(),muons[1].Phi(),trkisos[1],charges[1],dpts[1]]

	[_chimu1,_chimu2] = [chi2[0],chi2[1]]
	[_ispfmu1,ispfmu2] = [pfid[0],pfid[1]]
	[_layersmu1,_layersmu2] = [layers[0],layers[1]]

	[_ptel1,_etael1,_phiel1] = [electrons[0].Pt(),electrons[0].Eta(),electrons[0].Phi()]
	[_ptel2,_etael2,_phiel2] = [electrons[1].Pt(),electrons[1].Eta(),electrons[1].Phi()]
	[_ptj1,_etaj1,_phij1]    = [jets[0].Pt(),jets[0].Eta(),jets[0].Phi()]
	[_ptj2,_etaj2,_phij2]    = [jets[1].Pt(),jets[1].Eta(),jets[1].Phi()]
	[_nhefj1,_nhefj2,_nemefj1,_nemefj2] = [neutralhadronEF[0],neutralhadronEF[1],neutralemEF[0],neutralemEF [1]]
	[_ptmet,_etamet,_phimet] = [met.Pt(),0,met.Phi()]
	[_xmiss,_ymiss] = [met.Px(),met.Py()]

	_stuujj = ST([muons[0],muons[1],jets[0],jets[1]])
	_stuvjj = ST([muons[0],met,jets[0],jets[1]])

	_steejj = ST([electrons[0],electrons[1],jets[0],jets[1]])
	_stevjj = ST([electrons[0],met,jets[0],jets[1]])


	_Muu = (muons[0]+muons[1]).M()
	_MTuv = TransMass(muons[0],met)
	_DRuu = (muons[0]).DeltaR(muons[1])
	_DPHIuv = abs((muons[0]).DeltaPhi(met))
	_DPHIj1v = abs((jets[0]).DeltaPhi(met))
	_DPHIj2v = abs((jets[1]).DeltaPhi(met))

	_DRu1j1 = abs(muons[0].DeltaR(jets[0]))
	_DRu1j2 = abs(muons[0].DeltaR(jets[1]))
	_DRu2j1 = abs(muons[1].DeltaR(jets[0]))
	_DRu2j2 = abs(muons[1].DeltaR(jets[1]))

	_DPhiu1j1 = abs(muons[0].DeltaPhi(jets[0]))
	_DPhiu1j2 = abs(muons[0].DeltaPhi(jets[1]))
	_DPhiu2j1 = abs(muons[1].DeltaPhi(jets[0]))
	_DPhiu2j2 = abs(muons[1].DeltaPhi(jets[1]))

	_Muujj1_gen=0
	_Muujj2_gen=0
	_MHuujj_gen=0
	_Muujjavg_gen=0
	#if(_jetInd1 != -99 and _jetInd2 != -99 and len(jets) > _jetInd2 and len(jets) > _jetInd1): 
	#	print _muonInd1,_muonInd2,_jetInd1,_jetInd2
	#	print '#jets: ',len(jets)
	if (len(_genMuons)>1 and len(_genJets)>1) :
		[_Muujj1_gen,_Muujj2_gen,_MHuujj_gen] = GetLLJJMasses(_genMuons[0],_genMuons[1],_genJets[0],_genJets[1])
		_Muujjavg_gen = 0.5*(_Muujj1_gen + _Muujj1_gen)
	else :
		[_Muujj1_gen,_Muujj2_gen,_MHuujj_gen] = [0,0,0]
		_Muujjavg_gen = 0

	if len(_matchedRecoMuons)>1 and len(_matchedRecoJets)>1 :
		[_Muujj1_genMatched,_Muujj2_genMatched,_MHuujj_genMatched] = GetLLJJMasses(_matchedRecoMuons[0],_matchedRecoMuons[1],_matchedRecoJets[0],_matchedRecoJets[1])
		_Muujjavg_genMatched = 0.5*(_Muujj1_genMatched + _Muujj1_genMatched)
	else :
		
		[_Muujj1_genMatched,_Muujj2_genMatched,_MHuujj_genMatched] = [0,0,0]
		_Muujjavg_genMatched = 0



	_Muujj1_3jet=0
	_Muujj2_3jet=0
	_MHuujj_3jet=0	
	_Muujj1_3jet_rel=0
	_Muujj2_3jet_rel=0
	_MHuujj_3jet_rel=0
	#if len(jets)>= 4:
	#	[_Muujj1_3jet, _Muujj2_3jet,_MHuujj_3jet] = GetLLJJMasses4Jets(muons[0],muons[1],jets[0],jets[1],jets[2],jets[3])
	if len(jets)>= 3 and jets[1].Pt()>130 and jets[2].Pt()>45 :
		[_Muujj1_3jet, _Muujj2_3jet,_MHuujj_3jet] = GetLLJJMasses3Jets(muons[0],muons[1],jets[0],jets[1],jets[2])
	else:
		[_Muujj1_3jet, _Muujj2_3jet,_MHuujj_3jet] = GetLLJJMasses(muons[0],muons[1],jets[0],jets[1])
	_Muujjavg_3jet = 0.5*(_Muujj1_3jet+_Muujj2_3jet)

	if len(jets)>= 3 and jets[1].Pt()>130 and jets[2].Pt()>45 :
		[_Muujj1_3jet_rel, _Muujj2_3jet_rel,_MHuujj_3jet_rel] = GetLLJJMasses3JetsRelative(muons[0],muons[1],jets[0],jets[1],jets[2])
	else:
		[_Muujj1_3jet_rel, _Muujj2_3jet_rel,_MHuujj_3jet_rel] = GetLLJJMassesRelative(muons[0],muons[1],jets[0],jets[1])
	_Muujjavg_3jet_rel = 0.5*(_Muujj1_3jet_rel+_Muujj2_3jet_rel)



	[_Muujj1, _Muujj2,_MHuujj] = GetLLJJMasses(muons[0],muons[1],jets[0],jets[1])
	[[_MTuvjj1, _MTuvjj2], [_Muvjj, _MTuvjj],_MHuvjj] = GetLVJJMasses(muons[0],met,jets[0],jets[1])

	[_Meejj1, _Meejj2,_MHeejj] = GetLLJJMasses(electrons[0],electrons[1],jets[0],jets[1])
	[[_MTevjj1, _MTevjj2], [_Mevjj, _MTevjj],_MHevjj] = GetLVJJMasses(electrons[0],met,jets[0],jets[1])

	_Muujjavg = 0.5*(_Muujj1+_Muujj2)

	[_Muujj1_rel, _Muujj2_rel,_MHuujj_rel] = GetLLJJMassesRelative(muons[0],muons[1],jets[0],jets[1])
	_Muujjavg_rel = 0.5*(_Muujj1_rel+_Muujj2_rel)



	if _ptmu1>42 and  _ptmu2>42 and _ptmet>35 and _ptj1>110 and _ptj2>40 and _stuujj>250 and _stuvjj>250:
		#print ' Here we go:'
		if len(jets)>= 4: GetLLJJMasses4Jets(muons[0],muons[1],jets[0],jets[1],jets[2],jets[3])
		if len(jets)>= 3: GetLLJJMasses3Jets(muons[0],muons[1],jets[0],jets[1],jets[2])
		GetLLJJMasses(muons[0],muons[1],jets[0],jets[1])

	_genjetcount = 0
	if T.isData==0:
		_genjetcount = len(T.GenJetPt)

	# This MUST have the same structure as _kinematic variables!
	toreturn = [_ptmu1,_ptmu2,_ptel1,_ptel2,_ptj1,_ptj2,_ptmet]
	toreturn += [_etamu1,_etamu2,_etael1,_etael2,_etaj1,_etaj2,_etamet]
	toreturn += [_phimu1,_phimu2,_phiel1,_phiel2,_phij1,_phij2,_phimet]
	toreturn += [_xmiss,_ymiss]
	toreturn += [_isomu1,_isomu2]
	
	toreturn += [_chimu1,_chimu2]
	toreturn += [_ispfmu1,ispfmu2]
	toreturn += [_layersmu1,_layersmu2]

	toreturn += [_qmu1,_qmu2]
	toreturn += [_dptmu1,_dptmu2]
	toreturn += [_nhefj1,_nhefj2,_nemefj1,_nemefj2]
	toreturn += [_stuujj,_stuvjj]
	toreturn += [_steejj,_stevjj]
	toreturn += [_Muu,_MTuv]
	toreturn += [_DRuu,_DPHIuv,_DPHIj1v,_DPHIj2v]
	toreturn += [_DRu1j1,_DRu1j2,_DRu2j1,_DRu2j2]
	toreturn += [_DPhiu1j1,_DPhiu1j2,_DPhiu2j1,_DPhiu2j2]
	toreturn += [_Muujj1_gen, _Muujj2_gen,_Muujjavg_gen]
	toreturn += [_Muujj1_genMatched, _Muujj2_genMatched,_Muujjavg_genMatched]
	toreturn += [_Muujj1_3jet, _Muujj2_3jet,_Muujjavg_3jet]
	toreturn += [_Muujj1_3jet_rel, _Muujj2_3jet_rel,_Muujjavg_3jet_rel]
	toreturn += [_Muujj1, _Muujj2,_Muujjavg]
	toreturn += [_Muujj1_rel, _Muujj2_rel,_Muujjavg_rel]
	toreturn += [_MTuvjj1, _MTuvjj2,_Muvjj, _MTuvjj]
	toreturn += [_MHuujj,_MHuvjj]
	toreturn += [_Meejj1, _Meejj2]
	toreturn += [_MTevjj1, _MTevjj2,_Mevjj, _MTevjj]	
	toreturn += [_jetcount,_mucount,_elcount,_genjetcount]
	toreturn += [_ismuon_muon1,_ismuon_muon2]
	toreturn += [_muonInd1,_muonInd2]
	toreturn += [_jetInd1,_jetInd2]
	return toreturn



##########################################################################################
#################    BELOW IS THE ACTUAL LOOP OVER ENTRIES         #######################
##########################################################################################
startTime = datetime.now()

# Please don't edit here. It is static. The kinematic calulations are the only thing to edit!
lumisection = array.array("L",[0])
t.SetBranchAddress("ls",lumisection)
for n in range(N):

	# This is the loop over events. Due to the heavy use of functions and automation of 
	# systematic variations, this loop is very small. It should not really be editted, 
	# except possibly to add a new flag or weight variable. 
	# All editable contents concerning kinematics are in the function defs.

	# Get the entry
	t.GetEntry(n)
	# if n > 1000:  # Testing....
	# 	break
	if n%100==0:
		print 'Procesing event',n, 'of', N # where we are in the loop...

	## ===========================  BASIC SETUP  ============================= ##
	# print '-----'
	# Assign Weights
	Branches['weight_central'][0] = startingweight*GetPUWeight(t,'Central','Basic')
	Branches['weight_pu_down'][0] = startingweight*GetPUWeight(t,'SysDown','Basic')
	Branches['weight_pu_up'][0] = startingweight*GetPUWeight(t,'SysUp','Basic')
	Branches['weight_central_2012D'][0] = startingweight*GetPUWeight(t,'Central','2012D')
	Branches['weight_nopu'][0] = startingweight
	if dopdf:
		pdfweights = GetPDFWeights(t)
		for p in range(len(pdfweights)):
			Branches[_pdfweightsnames[p]][0] = pdfweights[p]
	
	# Event Flags
	Branches['run_number'][0]   = t.run
	# event_number[0] = int(t.event)
	Branches['event_number'][0] = t.event
	Branches['lumi_number'][0]  = lumisection[0]
	Branches['GoodVertexCount'][0] = CountVertices(t)




	if t.isData == True:
		Branches['pass_HLTMu40_eta2p1'][0] = PassTrigger(t,["HLT_Mu45_eta2p1_v"],1)         # Data Only
		Branches['passTriggerObjectMatching'][0]  = 1*(True in t.MuonHLTSingleMuonMatched)  # Data Only
		Branches['passBPTX0'][0]                  = 1*(t.isBPTX0)          # Unused, Data only: MC = 0
		Branches['passBeamScraping'][0]           = 1*(1-t.isBeamScraping) # Used, Data only
		Branches['passTrackingFailure'][0]        = 1*(1-t.isTrackingFailure) # Used, Data only
		Branches['passBadEESuperCrystal'][0]      = 1*(1-t.passBadEESupercrystalFilter) # Used, Data only
		Branches['passEcalLaserCorr'][0]          = 1*(t.passEcalLaserCorrFilter) # Used, Data only
		# Branches['passHcalLaserEvent'][0]         = 1*(1-t.passHcalLaserEventFilter) # Used, Data only
		Branches['passHcalLaserEvent'][0]         = 1 # Ooops, where did it go?
		Branches['passPhysDeclared'][0]           = 1*(t.isPhysDeclared)

	else:
		Branches['pass_HLTMu40_eta2p1'][0] = PassTrigger(t,["HLT_Mu45_eta2p1_v"],1)        
		Branches['passTriggerObjectMatching'][0]  = 1
		Branches['passBPTX0'][0]                  = 1
		Branches['passBeamScraping'][0]           = 1
		Branches['passTrackingFailure'][0]        = 1
		Branches['passBadEESuperCrystal'][0]      = 1
		Branches['passEcalLaserCorr'][0]          = 1
		Branches['passHcalLaserEvent'][0]         = 1
		Branches['passPhysDeclared'][0]           = 1
	
	Branches['passPrimaryVertex'][0]          = 1*(t.isPrimaryVertex)     # checked, data+MC
	Branches['passHBHENoiseFilter'][0]        = 1*(t.passHBHENoiseFilter) # checked, data+MC
	Branches['passBeamHalo'][0]               = 1*(t.passBeamHaloFilterTight) # checked, data+MC
	Branches['passEcalDeadCellBE'][0]         = 1#*(1-t.passEcalDeadCellBoundaryEnergyFilter) # Checked, data + MC
	Branches['passEcalDeadCellTP'][0]         = 1*(1-t.passEcalDeadCellTriggerPrimitiveFilter) # Checked, data + MC

	Branches['passDataCert'][0] = 1
	if ( (t.isData==True) and (CheckRunLumiCert(t.run,lumisection[0]) == False) ) : 	
		Branches['passDataCert'][0] = 0



	## ===========================  Calculate everything!  ============================= ##

	# Looping over systematic variations
	for v in _variations:
		# All calucations are done here
		calculations = FullKinematicCalculation(t,v)
		# Now cleverly cast the variables
		for b in range(len(_kinematicvariables)):
			Branches[_kinematicvariables[b]+v][0] = calculations[b]

	## ===========================     Skim out events     ============================= ##

	# Feel like skimming? Do it here. The syntax is just Branches[branchname] > blah, or whatever condition
	# you want to impose. This Branches[blah] mapping was needed because branches must be linked to arrays of length [0]
	# BE MINDFUL: Just because the central (non-systematic) quantity meets the skim, does not mean 
	# that the systematic varied quantity will, and that will throw off systematics calculations later.
	# Make sure your skim is looser than any selection you will need afterward!

	if (Branches['Pt_muon1'][0] < 42): continue
	if nonisoswitch != True:
		if (Branches['Pt_muon2'][0] < 42) and (Branches['Pt_miss'][0] < 35): continue
	if (Branches['Pt_jet1'][0] < 110): continue
	if (Branches['Pt_jet2'][0] < 40): continue
	if (Branches['St_uujj'][0] < 250) and (Branches['St_uvjj'][0] < 250): continue
	# Fill output tree with event
	tout.Fill()

# All done. Write and close file.
tout.Write()
fout.Close()

# Timing, for debugging and optimization
print(datetime.now()-startTime)

print ('mv '+tmpfout+' '+finalfout)
os.system('mv '+tmpfout+' '+finalfout)
os.system('rm '+junkfile1)
os.system('rm '+junkfile2)
