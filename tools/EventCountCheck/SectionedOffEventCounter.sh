############################################################################
# This script counts the number of events in a given folder of MC
# It makes use of FileList.txt
# In a text file, make a list of each folder you want to count, one per line
# Then run by typing "sh EventCounter.sh {Text file name}"
#############################################################################

cut -f1 -d',' $1 > SigType.txt
cut -f8 -d',' $1 > Folders.txt
# ^ Here I make text files out of the 1st and 8th columns of the input csv file

N=`wc SigType.txt | gawk '(NR==1){print $1}'`
echo $N

mkdir LogFiles

for ((i = 2; i <=N; i++))
do
    CurrentFolder=`gawk '(NR=='$i'){print $1}' Folders.txt`
    CurrentSig=`gawk '(NR=='$i'){print $1}' SigType.txt`

    cmsLs $CurrentFolder  | gawk '{print $5}' > TotalFolderContents.txt
    grep $CurrentSig TotalFolderContents.txt > CurrentFiles.txt
    # ^ Here I take only files matching the current Signature and put them in a text file
    M=`wc CurrentFiles.txt | gawk '(NR==1){print $1}'`

    mkdir LogFiles/$CurrentSig

    for ((j = 1; j <=M; j++))
    do
	CurrentFile=`gawk '(NR=='$j'){print $1}' CurrentFiles.txt`

	cat BlankScript.sh | sed -e 's,File=PLACEHOLDER,File='$CurrentFile',g
s,PLACE_TWO,/afs/cern.ch/user/d/dnash/CMSSW_4_2_8/src/NTupleAnalyzer/tools/EventCountCheck/LogFiles/'$CurrentSig'/Log_'$j'.txt,g' > /afs/cern.ch/user/d/dnash/CMSSW_4_2_8/src/NTupleAnalyzer/tools/EventCountCheck/LogFiles/$CurrentSig/Script_$j.sh


    done
done
