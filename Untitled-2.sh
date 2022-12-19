#!/bin/bash
#!/bin/bash

dataFile=data 

while getopts 'd:' OPTION; do
  case "$OPTION" in
  d)
      dataFile="$OPTARG"
      echo "The value provided is $OPTARG"
      ;;

  ?)
        exit 1
      ;;
  esac
done
shift "$(($OPTIND -1))"

echo "$1 "" $2"

if [ $# -eq 0 ]
    then
     echo "0"
     echo "$dataFile"
    ./bgpdump -M $dataFile | awk -F '|' '{print $7}' | awk -F ' ' '{print $1 " " $NF} ' | sort -u >allAsPair.txt

else
./bgpdump -M $dataFile |grep "|$1"| grep "$2|" | awk -F '|' '{print $7}' | sort -u >output.txt
fi 

