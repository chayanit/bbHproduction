# bbHproduction
scripts for MSSM bbH private MC production with crab3

## setup

Clone the repository into a new directory (more directories will show up in parallel):
```
mkdir signalProduction
cd signalProduction
git clone git@github.com:clelange/bbHproduction.git
```

### at DESY

To get a CMS software environment:

```
export X509_USER_PROXY=$HOME/k5-ca-proxy.pem
module use -a /afs/desy.de/group/cms/modulefiles/
module load cmssw
```

## GEN-SIM step

This step needs a working CMS software environment (see above). Need to be in ```signalProduction``` directory.

```
cmsrel CMSSW_7_1_24
cd CMSSW_7_1_24/src
cmsenv
source /cvmfs/cms.cern.ch/crab3/crab_light.sh
for i in `ls ../../bbHproduction/GEN-SIM`; do ln -s ../../bbHproduction/GEN-SIM/$i; done
```

Need to adjust ```crabConfig_MCgeneration.py``` to point to a storage site that you have write access to:
```
config.Site.storageSite = 'T2_DE_DESY'
```

Then submit:
```
./submitCrab.sh
```

### job sitting

To check the status of your jobs and to resubmit the failed ones:
```
./resubmit.sh
```

## DIGI step

Start again in the ```signalProduction``` directory, probably best from a clean shell (set up CMS software environment again).


```
cmsrel CMSSW_7_6_1
cd CMSSW_7_6_1/src
cmsenv
source /cvmfs/cms.cern.ch/crab3/crab_light.sh
for i in `ls ../../bbHproduction/DIGI-RECO`; do ln -s ../../bbHproduction/DIGI-RECO/$i; done
ln -s ../../bbHproduction/GEN-SIM/resubmit.sh
```

Put your GEN-SIM dataset names into ```datasets_GENSIM.txt```, one per line.

Need to adjust ```crabConfig_MCgeneration_DIGI76X_step1.py``` to point to a storage site that you have write access to:
```
config.Site.storageSite = 'T2_DE_DESY'
```

Then you can submit:
```
submitCrab_DIGI.sh
```

## RECO step

This step needs the same setup as the DIGI one, so you can just setup CMSSW and crab again, or reuse the same shell:

```
cd CMSSW_7_6_1/src
cmsenv
source /cvmfs/cms.cern.ch/crab3/crab_light.sh
```

Put your DIGI dataset names into ```datasets_DIGI.txt```, one per line.

Need to adjust ```crabConfig_MCgeneration_RECO76X_step2.py``` to point to a storage site that you have write access to:
```
config.Site.storageSite = 'T2_DE_DESY'
```

Then you can submit:
```
submitCrab_RECO.sh
```

### job sitting

To check the status of your jobs and to resubmit the failed ones:
```
./resubmit.sh
```

Mind that this would also resubmit failed DIGI jobs when you're already running RECO jobs (but this won't hurt).
