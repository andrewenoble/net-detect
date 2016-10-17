# Network Anomaly Detection and PCA

By [Andrew Noble](http://andrewenoble.com)

## About

This repo contains the Python files used to demonstrate the utility of a Principal Component Analysis (PCA) as a simple and scalable first step in searching for anomalous behavior in large spatiotemporal data sets.  Two such data sets, one on the San Francisco bike share program and the other on UK measles outbreaks following World War II, are analyzed here.  Code in the ```bikeshare``` directory reproduces the results discussed on [this webpage](http://andrewenoble.com/bikeshare.html).  Code in the ```measles``` directory reproduces the results discussed on [this webpage](http://andrewenoble.com/measles.html).  Code in the ```util``` directory is used by both ```bikeshare``` and ```measles```.

## Requirements

* Python (numpy, scipy, pandas, pickle, cartopy, matplotlib, pylab)

## Usage

Clone the repo.
```
git clone https://github.com/andrewenoble/net-detect.git
cd net-detect
```
From the ```net-detect``` directory,  decend into either the ```measles``` or ```bikeshare``` directory.  Further usage instructions can be found there in another README.md file.

## Acknowledgements

This work is support by an [NSF
INSPIRE award](http://www.nsf.gov/awardsearch/showAward?AWD_ID=1344187&amp;HistoricalAwards=false) from the National Science Foundation.  
