# Network Anomaly Detection and PCA:  UK Measles

By [Andrew Noble](http://two.ucdavis.edu/~andrewnoble)

## About

This repo contains Python files used to demonstrate the utility of a Principal Component Analysis (PCA) in the exploration of spatiotemporal data on UK measles outbreaks following World War II.  The data is [publicly available](http://ento.psu.edu/research/labs/ottar-bjornstad/ottar-lab-abstracts/tsir-analysis-of-measles-in-england-and-wales), and ```data``` contains a copy.  The Python code used to animate a portion of the outbreak data is contained in ```visualization``` along with all of the scripts used to generate the first three exploratory plots at the top of [this webpage](http://two.ucdavis.edu/~andrewnoble/measles.html).  All other plots on that webpage - the results of the PCA - were generated with the Python code in ```analysis```.

## Requirements

* Python (scipy, pandas, pickle, cartopy, matplotlib, pylab)

## Usage

Clone the repo.
```
git clone https://github.com/andrewenoble/net-detect.git
cd net-detect/measles
```
Run the python scripts in ```visualization``` and ```analysis``` to re-generate the the UK measles outbreak animation [here](http://two.ucdavis.edu/~andrewnoble/research.html) and the plots [here](http://two.ucdavis.edu/~andrewnoble/measles.html).  Running the scripts will overwrite the existing animation and plots. Note that running these scripts will overwrite existing animations and plots. and 

## Acknowledgements

This work is support by an [NSF
INSPIRE award](http://www.nsf.gov/awardsearch/showAward?AWD_ID=1344187&amp;HistoricalAwards=false) from the National Science Foundation.  
