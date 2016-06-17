import scipy as sp
import pandas as pd
import pylab as pl


# Customize the matplotlib environment.
pl.rc_context(fname='../../util/custom_rc')

# Define plotting parameters.
scale_of_reported_cases = 1e4


# Load the UK measles data.
df = pd.read_excel('../data/60measles.xls', '60measles')

# Create separate arrays for the year, week, and reported cases
# associated with each record (row) in the data set.
years = sp.asarray(df.values[:,0])
weeks = sp.asarray(df.values[:,1])
data_matrix = sp.asarray(df.values[:,2:])

# Create array recording each time point as a fraction of a year.
times = sp.linspace(years[0] + 1900 + 0./26, years[-1] + 1900 + 25./26, 
    len(years))

# Create arrays for the London (the 26th column of the data_matrix) and 
# Birmingham (the 25th column of the data_matrix) time series.
london_ts = data_matrix.T[26] 
birm_ts = data_matrix.T[2] 


# Plot time series.
fig = pl.figure(figsize=(6., 4.))
ax = pl.axes([0.08, 0.09, 0.91, 0.90])

# Plot the London time series as a black line.
pl.plot(times, london_ts / scale_of_reported_cases, 'k-', lw=1.00, 
    label='London', alpha=0.8)
                    
# Plot the Birmingham time series as a red line.                    
pl.plot(times, birm_ts / scale_of_reported_cases, 'r-', lw=0.75, 
    label='Birmingham', alpha=0.8)
    
# Label the horizontal axis with the year.   
ax.set_xlabel('Year', labelpad=5) 
ax.set_xlim(1943.75, 1967.25)
ax.xaxis.set_ticks_position('bottom')

# Label the vertical axis with the fractional number of reported cases.
ax.set_ylabel('# reported cases / 10,000', labelpad=5)    
ax.set_ylim(-0.02, 0.75) 
ax.yaxis.set_ticks_position('left')

# Add a legend.  
ax.legend(numpoints = 1, loc = 0, markerscale=0.5, handlelength=1.5,
    borderpad=0.2, labelspacing=0.3) 
    
# Save plot.
fig.savefig('london_birm_ts.png', dpi=300)         
