ukidss
===================

Galaxy Zoo-UKIDSS data reduction: in progress.

Note: this repository is public, but the database of classifications is not. Currently the raw database *and* the classifications files that results from running the code here is stored in a separate directory (../classifications/) which is not synced here.

## To run

- Step 0: Download database dump in csv format.

- Step 1: Download subject database in mongodb format

- Step 2: Collate votes for the UKIDSS galaxies

- Step 3: Match collated classifications against subject metadata in TOPCAT

```
    ./fix_raw_classifications.sh 2013-11-03_galaxy_zoo_classifications.csv
    ./extract_ukidss_ids.sh 2013-11-03_galaxy_zoo_classifications.csv
    cd python
    ukidss.py 2013-11-03_galaxy_zoo_classifications.csv
```

Required Python packages:

- numpy
- astropy *or* pyfits
