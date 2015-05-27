

cut -f1 -d',' $1 > SigTypes.txt
cut -f8 -d',' $1 > CastorFolders.txt

nsls `gawk '(NR==2){print $1}' CastorFolders.txt` > CurrentFiles.txt
CurrentSig=`gawk '(NR==2){print $1}' SigType.txt`

grep $CurrentSig CurrentFiles.txt
Home=`pwd`
NewFolder=Something
echo $Home/$NewFolder