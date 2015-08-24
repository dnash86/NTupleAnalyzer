#!/usr/bin/python
from ROOT import *
import array
import math
tRand = TRandom3()
from random import randint
import os


### This contains all the variable computations that are used in the main NTupleAnalyzer file
#   This is both simple computations such as ST, and complex mass combination concepts for choosing lj masses for single and pair prod.
#   Also, in addition to the basic math, there is some use of root, for vertex counting

### Basic math
def TransMass(p1,p2):
	# Purpose: Simple calculation of transverse mass between two TLorentzVectors
	return math.sqrt( 2*p1.Pt()*p2.Pt()*(1-math.cos(p1.DeltaPhi(p2))) )

def InvMass(particles):
	# Purpose: Simple calculation of invariant mass between two TLorentzVectors	
	output=particles
	return (p1+p2).M()

def ST(particles):
	# Purpose: Calculation of the scalar sum of PT of a set of TLorentzVectors	
	st = 0.0
	for p in particles:
		st += p.Pt()
	return st
####



####Pair production LQ concepts
def GetLLJJMasses(l1,l2,j1,j2):
	# Purpose: For LLJJ channels, this function returns two L-J Masses, corresponding to the
	#         pair of L-Js which minimizes the difference between LQ masses in the event

	# These are the invariant mass combinations 
	m11 = (l1+j1).M()
	m12 = (l1+j2).M()
	m21 = (l2+j1).M()
	m22 = (l2+j2).M()
	mh = 0.0 # This will be the invariant mass of the lepton and leading jet

	# Difference in Mass for the two matching scenarios
	diff1 = abs(m21-m12)
	diff2 = abs(m11-m22)

	# The ideal match minimizes the Mass difference above
	# Based on the the diffs, store the appropriate pairs	
	if diff1 < diff2:
		pair =  [m21,m12] # The invariant mass pair
		mh = m21          # invariant mass corresponding to leading jet
	else:
		pair = [m11,m22]  # The invariant mass pair
		mh = m11          # invariant mass corresponding to leading jet
	least = min(diff1,diff2)
	#print '2Jet min:',least,'masses: ',pair[0],pair[1]
	pair.sort()
	pair.reverse()
	pair.append(mh)
	return pair



def GetLLJJMassesRelative(l1,l2,j1,j2):
	# Purpose: For LLJJ channels, this function returns two L-J Masses, corresponding to the
	#         pair of L-Js which minimizes the difference between LQ masses in the event

	# These are the invariant mass combinations 
	m11 = (l1+j1).M()
	m12 = (l1+j2).M()
	m21 = (l2+j1).M()
	m22 = (l2+j2).M()
	mh = 0.0 # This will be the invariant mass of the lepton and leading jet

	# Difference in Mass for the two matching scenarios
	if m12>0:
		diff1 = abs(m21-m12)/m12
	else:
		diff1 = 9999
	if m11>0:
		diff2 = abs(m11-m22)/m11
	else:
		diff2 = 10000

	# The ideal match minimizes the Mass difference above
	# Based on the the diffs, store the appropriate pairs	
	if diff1 < diff2:
		pair =  [m21,m12] # The invariant mass pair
		mh = m21          # invariant mass corresponding to leading jet
	else:
		pair = [m11,m22]  # The invariant mass pair
		mh = m11          # invariant mass corresponding to leading jet
	least = min(diff1,diff2)
	#print '2Jet min:',least,'masses: ',pair[0],pair[1]
	pair.sort()
	pair.reverse()
	pair.append(mh)
	return pair




def GetLLJJMasses3Jets(l1,l2,j1,j2,j3):

	m11 = (l1+j1).M()
	m12 = (l1+j2).M()
	m13 = (l1+j3).M()
	m21 = (l2+j1).M()
	m22 = (l2+j2).M()
	m23 = (l2+j3).M()

	diff1 = abs(m11-m22)
	diff2 = abs(m11-m23)
	diff3 = abs(m12-m21)
	diff4 = abs(m12-m23)
	diff5 = abs(m13-m21)
	diff6 = abs(m13-m22)

	least = min(diff1,diff2,diff3,diff4,diff5,diff6)
	
	if least == diff1 :
		pair = [m11,m22] # The invariant mass pair
		mh = m11 # invariant mass corresponding to leading jet
	elif least == diff2:
		pair = [m11,m23] # The invariant mass pair
		mh = m11 # invariant mass corresponding to leading jet
	elif least == diff3:
		pair = [m12,m21] # The invariant mass pair
		mh = m21 # invariant mass corresponding to leading jet
	elif least == diff4:
		pair = [m12,m23] # The invariant mass pair
		mh = m12 # invariant mass corresponding to leading jet
	elif least == diff5:
		pair = [m13,m21] # The invariant mass pair
		mh = m21 # invariant mass corresponding to leading jet
	elif least == diff6:
		pair = [m13,m22] # The invariant mass pair
		mh = m22 # invariant mass corresponding to leading jet
        else:
		pair = [0,0]
		mh=0
	#print '3Jet min:',least,'masses: ',pair[0],pair[1]
	pair.sort()
	pair.reverse()
	pair.append(mh)
	return pair

def GetLLJJMasses3JetsRelative(l1,l2,j1,j2,j3):

	m11 = (l1+j1).M()
	m12 = (l1+j2).M()
	m13 = (l1+j3).M()
	m21 = (l2+j1).M()
	m22 = (l2+j2).M()
	m23 = (l2+j3).M()

	j1pt = j1.Pt()
	j2pt = j2.Pt()

	if j1pt > 0:
		diff1 = abs(m11-m22)/j1pt
		diff2 = abs(m11-m23)/j1pt
		diff3 = abs(m12-m21)/j1pt
		diff5 = abs(m13-m21)/j1pt
	else:
		diff1 = 9999
		diff2 = 10000
		diff3 = 10000
		diff5 = 10000
	if j2pt > 0:
		diff4 = abs(m12-m23)/j2pt
		diff6 = abs(m13-m22)/j2pt
	else:
		diff4 = 9999
		diff6 = 10000

	least = min(diff1,diff2,diff3,diff4,diff5,diff6)
	
	if least == diff1 :
		pair = [m11,m22] # The invariant mass pair
		mh = m11 # invariant mass corresponding to leading jet
	elif least == diff2:
		pair = [m11,m23] # The invariant mass pair
		mh = m11 # invariant mass corresponding to leading jet
	elif least == diff3:
		pair = [m12,m21] # The invariant mass pair
		mh = m21 # invariant mass corresponding to leading jet
	elif least == diff4:
		pair = [m12,m23] # The invariant mass pair
		mh = m12 # invariant mass corresponding to leading jet
	elif least == diff5:
		pair = [m13,m21] # The invariant mass pair
		mh = m21 # invariant mass corresponding to leading jet
	elif least == diff6:
		pair = [m13,m22] # The invariant mass pair
		mh = m22 # invariant mass corresponding to leading jet
        else:
		pair = [0,0]
		mh=0
	#print '3Jet min:',least,'masses: ',pair[0],pair[1]
	pair.sort()
	pair.reverse()
	pair.append(mh)
	return pair

def GetLLJJMasses4Jets(l1,l2,j1,j2,j3,j4):

	m11 = (l1+j1).M()
	m12 = (l1+j2).M()
	m13 = (l1+j3).M()
	m14 = (l1+j4).M()
	m21 = (l2+j1).M()
	m22 = (l2+j2).M()
	m23 = (l2+j3).M()
	m24 = (l2+j4).M()

	diff1  = abs(m11-m22)
	diff2  = abs(m11-m23)
	diff3  = abs(m11-m24)
	diff4  = abs(m12-m21)
	diff5  = abs(m12-m23)
	diff6  = abs(m12-m24)
	diff7  = abs(m13-m21)
	diff8  = abs(m13-m22)
	diff9  = abs(m13-m24)
	diff10 = abs(m14-m21)
	diff11 = abs(m14-m22)
	diff12 = abs(m14-m23)

	least = min(diff1,diff2,diff3,diff4,diff5,diff6,diff7,diff8,diff9,diff10,diff11,diff12)
	if least == diff1 :
		pair = [m11,m22] # The invariant mass pair
		mh = m11 # invariant mass corresponding to leading jet
	elif least == diff2:
		pair = [m11,m23] # The invariant mass pair
		mh = m11 # invariant mass corresponding to leading jet
	elif least == diff3:
		pair = [m12,m21] # The invariant mass pair
		mh = m21 # invariant mass corresponding to leading jet
	elif least == diff4:
		pair = [m12,m23] # The invariant mass pair
		mh = m12 # invariant mass corresponding to leading jet
	elif least == diff5:
		pair = [m13,m21] # The invariant mass pair
		mh = m21 # invariant mass corresponding to leading jet
	elif least == diff6:
		pair = [m13,m22] # The invariant mass pair
		mh = m22 # invariant mass corresponding to leading jet
	elif least == diff7 :
		pair = [m13,m21] # The invariant mass pair
		mh = m21 # invariant mass corresponding to leading jet
	elif least == diff8:
		pair = [m13,m22] # The invariant mass pair
		mh = m22 # invariant mass corresponding to leading jet
	elif least == diff9:
		pair = [m13,m24] # The invariant mass pair
		mh = m13 # invariant mass corresponding to leading jet
	elif least == diff10:
		pair = [m14,m21] # The invariant mass pair
		mh = m21 # invariant mass corresponding to leading jet
	elif least == diff11:
		pair = [m14,m22] # The invariant mass pair
		mh = m22 # invariant mass corresponding to leading jet
	elif least == diff12:
		pair = [m14,m23] # The invariant mass pair
		mh = m23 # invariant mass corresponding to leading jet
        else:
		pair = [0,0]
		mh=0

	#print '4Jet min:',least,'masses: ',pair[0],pair[1]
	pair.sort()
	pair.reverse()
	pair.append(mh)
	return pair


def GetLVJJMasses(l1,met,j1,j2):
	# Purpose: For LVJJ channels, this function returns two L-J Masses, and an LJ mass and mT, 
	#         Quantities corresponding to the pair of L-Js which minimizes the difference 
	#         between LQ masses in the event

	# These are the lepton-jet masses
	m11 = (l1+j1).M()
	m12 = (l1+j2).M()
	# These are the lepton-jet transverse masses
	mt11 = TransMass(l1,j1)
	mt12 = TransMass(l1,j2)
	# These are the met-jet transverse masses
	mte1 = TransMass(met,j1)
	mte2 = TransMass(met,j2)
	mh = 0.0	
	# Difference in MT for the two matching scenarios
	diff1 = abs(mte1-mt12)  # MET matched to jet1, lepton matched to jet2
	diff2 = abs(mt11-mte2)  # MET matched to jet2, lepton matched to jet1
	# The ideal match minimizes the MT difference above
	# Based on the the diffs, store the appropriate pairs
	if diff1 < diff2:
		pair =  [mte1,mt12]      # These are the two trans-mass values
		pairwithinv = [m12,mte1] # Instead we could store one invariant mass and one trans mass
	# This is the other matching possibility
	else:
		pair = [mt11,mte2]
		invmass = m11
		mh = m11 # The invariant mass pair with the leading jet
		pairwithinv = [m11,mte2]
	# Let put the pair of trans-masses in pT order
	pair.sort()
	pair.reverse()
	
	return [pair,pairwithinv,mh]

###############  Single LQ mass concepts


def GetLLJMass(l1,l2,j1):
	m11 = (l1+j1).M()
	m12 = (l2+j1).M()
        if m11> m12:
            return m11
        else:
            return m12
