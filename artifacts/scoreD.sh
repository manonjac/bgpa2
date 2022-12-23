#!/bin/bash

dataFile=updates.20221130.2240

while getopts 'd:' OPTION; do
  case "$OPTION" in
  d)
      dataFile="$OPTARG"
      echo "The File provided is $OPTARG"
      ;;

  ?)
        exit 1
      ;;
  esac
done
shift "$(($OPTIND -1))"

if [ $# -eq 0 ]
    then
    ./bgpdump -M $dataFile | awk -F '|' '{print $7}' | awk -F ' ' '{print $1 " " $NF} ' | sort -u >allAsPair.txt

else

./bgpdump -M $dataFile |grep "|$1"| grep "$2|" | awk -F '|' '{print $7}' | sort -u >output.txt

fi 

echo "File created"


if [ $# -eq 2 ]
    then
    echo "The score d of the pair $1 - $2 is "

    ./scoreD.py

fi