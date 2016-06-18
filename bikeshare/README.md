# Network Anomaly Detection and PCA: Bike Share

By [Andrew Noble](http://two.ucdavis.edu/~andrewnoble)

## About

This repo contains Python files used to demonstrate the utility of a Principal Component Analysis (PCA) in the exploration of spatiotemporal data on the San Francisco bike share program.  The data is [publicly available](http://www.bayareabikeshare.com/open-data).  Here, the directory ```data``` only contains some general information on each of the 35 bike stations in San Francisco.  Another file (~1GB) will need to be downloaded by the user (see below).  Once both data files are in place, the Python script in ```data_filter``` can be run to extract data on the morning weekday commute.  The two Python scripts in ```vizualization``` generate the first three exploratory plots displayed benearth the bike station photo at the top of [this webpage](http://two.ucdavis.edu/~andrewnoble/bikeshare.html).  All other plots on that webpage - the results of the PCA - were generated with the Python code in ```analysis```.

## Requirements

* Python (scipy, pandas, pickle, cartopy, matplotlib, pylab)

## Usage

Clone the repo.
```
git clone https://github.com/andrewenoble/net-detect.git
cd net-detect/bikeshare
```
Download additional data:  Open the Bay Area Bike Share [data repository](http://www.bayareabikeshare.com/open-data) and click "YEAR 2 DATA".  You will have the option to download ```babs_open_data_year_2.zip```.  Unzip and copy ```201508_status_data.csv``` (~1GB) into the ```data``` directory.  Now filter that data to extract only the status of each bike station during weekday morning commutes.
```
cd data_filter
python filter.py
```
Finally, run the python scripts in ```visualization``` and ```analysis``` to re-generate the plots on  [this webpage](http://two.ucdavis.edu/~andrewnoble/bikeshare.html).  Note that running these scripts will overwrite existing animations and plots.

## Acknowledgements

This work is support by an [NSF
INSPIRE award](http://www.nsf.gov/awardsearch/showAward?AWD_ID=1344187&amp;HistoricalAwards=false) from the National Science Foundation.  
