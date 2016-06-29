#!/bin/zsh

NJOBS=500
CRABTEMPLATE=crabConfig_MCgeneration_RECO76X_step2.py
DATE=`date +'%F'`

for DATASETIN in `cat datasets_DIGI.txt`; do
  echo "DATASETIN: $DATASETIN"
  a=("${(@s/-/)DATASETIN}")
  CRABCONFIG=crabConfig_$a[2]-$a[3].py
  echo "CRABCONFIG $CRABCONFIG"
  DATASETOUT=$a[2]-$a[3]_RECO76X
  echo "DATASETOUT: $DATASETOUT"
  cp $CRABTEMPLATE $CRABCONFIG
  sed -i -e "s|DATASETIN|$DATASETIN|g" $CRABCONFIG
  sed -i -e "s/DATASETOUT/$DATASETOUT/g" $CRABCONFIG
  sed -i -e "s/DATE/$DATE/g" $CRABCONFIG
  sed -i -e "s/NJOBS/$NJOBS/g" $CRABCONFIG
  echo crab submit -c $CRABCONFIG
  break
done
