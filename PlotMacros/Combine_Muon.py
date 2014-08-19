import os
import sys

outputfile=sys.argv[1]


os.system('echo NoSystematics > '+outputfile)
os.system('cat CentralValues_Muon.txt >> '+outputfile)
os.system('cat CentralValues_Muon_Errors.txt >> '+outputfile)

os.system('echo PU_up >> '+outputfile)
os.system('cat PUUpValues_Muon.txt >> '+outputfile)
os.system('cat PUUpValues_Muon_Errors.txt >> '+outputfile)

os.system('echo PU_down >> '+outputfile)
os.system('cat PUDownValues_Muon.txt >> '+outputfile)
os.system('cat PUDownValues_Muon_Errors.txt >> '+outputfile)

os.system('echo JetScaleUp >> '+outputfile)
os.system('cat JetUpValues_Muon.txt >> '+outputfile)
os.system('cat JetUpValues_Muon_Errors.txt >> '+outputfile)

os.system('echo JetScaleDown >> '+outputfile)
os.system('cat JetDownValues_Muon.txt >> '+outputfile)
os.system('cat JetDownValues_Muon_Errors.txt >> '+outputfile)

os.system('echo MuScaleUp >> '+outputfile)
os.system('cat MuUpValues_Muon.txt >> '+outputfile)
os.system('cat MuUpValues_Muon_Errors.txt >> '+outputfile)

os.system('echo MuScaleDown >> '+outputfile)
os.system('cat MuDownValues_Muon.txt >> '+outputfile)
os.system('cat MuDownValues_Muon_Errors.txt >> '+outputfile)

os.system('echo JetSmear >> '+outputfile)
os.system('cat JetSmearValues_Muon.txt >> '+outputfile)
os.system('cat JetSmearValues_Muon_Errors.txt >> '+outputfile)

os.system('echo MuSmear >> '+outputfile)
os.system('cat MuSmearValues_Muon.txt >> '+outputfile)
os.system('cat MuSmearValues_Muon_Errors.txt >> '+outputfile)
