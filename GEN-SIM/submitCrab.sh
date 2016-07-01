#!/bin/zsh

EVENTSJOB=200
NJOBS=550
TEMPLATE=crabConfig_MCgeneration.py
DATE=`date +'%F'`

for CONFIG in `ls configs/*.py`; do
  #echo $CONFIG
  DATASET=`print $CONFIG(:t:r)`_GEN-SIM
  CONFIGNAME=crabConfig_${DATASET}.py
  cp $TEMPLATE $CONFIGNAME
  sed -i -e "s/DATASET/$DATASET/g" $CONFIGNAME
  sed -i -e "s/DATE/$DATE/g" $CONFIGNAME
  sed -i -e "s/EVENTSJOB/$EVENTSJOB/g" $CONFIGNAME
  sed -i -e "s/NJOBS/$NJOBS/g" $CONFIGNAME
  echo crab submit -c $CONFIGNAME
  # break
done
