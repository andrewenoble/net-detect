import scipy as sp
import pylab as pl


# Customize the matplotlib environment.
pl.rc_context(fname='../../util/custom_rc')


# Load filtered data.
sf_stations = sp.loadtxt('../data_filter/sf_stations.txt')
weekday_data_matrix = sp.loadtxt('../data_filter/weekday_data_matrix.txt')


# Plot 'bike availability' in the filtered data at stations 73 and 82 during the 
# first two weeks of September 2015.
station_index_list = [-6, -1]

# Plot station mean availability.
fig = pl.figure(figsize=(6., 4.))
ax = pl.axes([0.08, 0.09, 0.91, 0.90])

# Plot each morning's filtered data as an independent line segment.
series_0 = weekday_data_matrix[station_index_list[0], :60*10]
series_1 = weekday_data_matrix[station_index_list[1], :60*10]
times = sp.arange(len(series_0))

for i in xrange(10):
    
    label = 'station ' + str(int(sf_stations[-6])) if i is 0 else None
    
    pl.plot(times[60*i:60*(i+1)], series_0[60*i:60*(i+1)], 'g-', lw=0.5, 
        label=label, alpha=0.8)
        
    label = 'station ' + str(int(sf_stations[-1])) if i is 0 else None
                
    pl.plot(times[60*i:60*(i+1)], series_1[60*i:60*(i+1)], 'g-', lw=1., 
        label=label, alpha=0.8)
    
# Label the horizontal axis with the date in 'M/DD' format.    
ax.set_xticks([60, 120, 180, 240, 300, 360, 420, 480, 540])
ax.set_xticklabels([''])
ax.set_xticks([30, 90, 150, 210, 270, 330, 390, 450, 510, 570], minor=True)
ax.set_xticklabels(['9/01', '9/02', '9/03', '9/04', '9/05', '9/08', '9/09', 
    '9/10', '9/11', '9/12'], minor=True, y=-0.01)
ax.set_xlabel('Day', labelpad=5)
ax.xaxis.set_ticks_position('bottom')

# Label the vertical axis with a fractional measure of 'bike availability'.
ax.set_yticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
ax.set_ylabel('# bikes / # bike docks (\"bike availability\")', labelpad=5)    
ax.set_ylim(-0.025, 1.025)  
ax.yaxis.set_ticks_position('left')

# Add a legend.  
ax.legend(numpoints = 1, loc = 0, markerscale=0.5, handlelength=1.5,
    borderpad=0.2, labelspacing=0.3) 
    
# Save plot.
fig.savefig('station_ts.png', dpi=300)         
