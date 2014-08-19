import os
import sys

outputfile=sys.argv[1]


os.system('echo NoSystematics > '+outputfile)
os.system('cat CentralValues2.txt >> '+outputfile)
os.system('cat CentralValues2_Errors.txt >> '+outputfile)

os.system('echo PU_up >> '+outputfile)
os.system('cat PUUpValues2.txt >> '+outputfile)
os.system('cat PUUpValues2_Errors.txt >> '+outputfile)

os.system('echo PU_down >> '+outputfile)
os.system('cat PUDownValues2.txt >> '+outputfile)
os.system('cat PUDownValues2_Errors.txt >> '+outputfile)

os.system('echo JetScaleUp >> '+outputfile)
os.system('cat JetUpValues2.txt >> '+outputfile)
os.system('cat JetUpValues2_Errors.txt >> '+outputfile)

os.system('echo JetScaleDown >> '+outputfile)
os.system('cat JetDownValues2.txt >> '+outputfile)
os.system('cat JetDownValues2_Errors.txt >> '+outputfile)

os.system('echo EleScaleUp >> '+outputfile)
os.system('cat EleUpValues2.txt >> '+outputfile)
os.system('cat EleUpValues2_Errors.txt >> '+outputfile)

os.system('echo EleScaleDown >> '+outputfile)
os.system('cat EleDownValues2.txt >> '+outputfile)
os.system('cat EleDownValues2_Errors.txt >> '+outputfile)

os.system('echo JetSmear >> '+outputfile)
os.system('cat JetSmearValues2.txt >> '+outputfile)
os.system('cat JetSmearValues2_Errors.txt >> '+outputfile)

os.system('echo EleSmear >> '+outputfile)
os.system('cat EleSmearValues2.txt >> '+outputfile)
os.system('cat EleSmearValues2_Errors.txt >> '+outputfile)
