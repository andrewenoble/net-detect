import sys
sys.path.append('../../util/') 
import libe
import scipy as sp
import pylab as pl
import cartopy.crs as ccrs
from cartopy.io.img_tiles import GoogleTiles


# Customize the matplotlib environment.
pl.rc_context(fname='../../util/custom_rc')

# Choose a projection for plotting station locations.
proj = ccrs.PlateCarree() 

# Import imagery from the Google Maps API.
imagery = GoogleTiles()

# Define plotting parameters.
ll_scale_factor = 12.


# Load the filtered data.
ll_matrix = sp.loadtxt('../data_filter/ll_matrix.txt')
weekday_data_matrix = sp.loadtxt('../data_filter/weekday_data_matrix.txt')

# Choose the geographic area to plot based on the latitudes and longitudes of
# all stations (as contained in 'll_matrix').   
lat_min, lat_max = min(ll_matrix.T[0]), max(ll_matrix.T[0]) 
long_min, long_max = min(ll_matrix.T[1]), max(ll_matrix.T[1]) 
lat_offset = (lat_max - lat_min) / ll_scale_factor
long_offset = (long_max - long_min) / ll_scale_factor


# Perform the PCA.  Store the leading and subleading principal components (pc's) 
# in 'v'.  Store the fractions of total variation described by each pc in 'w'.  
# In both of the two-component 'v' and 'w' arrays, the first elements correspond 
# to the subleading pc; the second elements to the leading pc.
w, v = libe.pca_2(weekday_data_matrix)

# Save the fractions of total variation described by each pc.
sp.savetxt('w.txt', w) 
    
    
# Define a function that plots each pc of variation on a map.   
def plot(color_array, title, name): 
    
    fig = pl.figure(figsize=(3.2, 4.4))
    ax = pl.axes([0.01, 0.01, 0.98, 0.98], projection=imagery.crs)
    ax.set_extent([
        long_min - long_offset, long_max + long_offset, 
        lat_min - lat_offset, lat_max + lat_offset])
                
    # Add a map of San Francisco to the background.                                  
    ax.add_image(imagery, 14, alpha=0.25)         
        
    # Mark the value of the pc at each station location using a disk, of a 
    # color specified in 'color_array', on a white square.  (Otherwise, 
    # the disks are difficult to see against the colors of the map in the 
    # background.)        
    ax.scatter(ll_matrix.T[1], ll_matrix.T[0], color='w',
        s=60., marker='s', edgecolor='none', transform=proj)
        
    ax.scatter(ll_matrix.T[1], ll_matrix.T[0], color=color_array,
        s=30., marker='o', edgecolor='k', linewidth='0.25', transform=proj)
        
    # Add a title.
    ax.text(0.5, 0.96, title, fontsize=10, horizontalalignment='center', 
        transform=ax.transAxes)        
        
    # Save the plot.    
    fig.savefig(name, dpi=300)
    
    pass
        
    
# Plot the leading ('1') pc on a map.  (We ignore the subleading pc in this 
# analysis.)  
pc_1 = v.T[1]
pc_1_color_array = libe.make_color_array(pc_1)
plot(pc_1_color_array, 'Leading Principal Component', 'pc_1.png')


# Plot a time series of the leading pc projected onto the filtered data for the 
# first two weeks of September 2015.
fig = pl.figure(figsize=(6., 4.))
ax = pl.axes([0.08, 0.09, 0.91, 0.90])

# Calculate the time series.
pc_1_ts = weekday_data_matrix.T.dot(pc_1)

# Select the first two weeks of the time series.
series = pc_1_ts[:60*10]
times = sp.arange(len(series))

for i in xrange(10):
        
    pl.plot(times[60*i:60*(i+1)], series[60*i:60*(i+1)], 'm-', lw=1., alpha=0.8)

# Label the horizontal axis with the date in 'M/DD' format.    
ax.set_xticks([60, 120, 180, 240, 300, 360, 420, 480, 540])
ax.set_xticklabels([''])
ax.set_xticks([30, 90, 150, 210, 270, 330, 390, 450, 510, 570], minor=True)
ax.set_xticklabels(['9/01', '9/02', '9/03', '9/04', '9/05', '9/08', '9/09', 
    '9/10', '9/11', '9/12'], minor=True, y=-0.01)
ax.set_xlabel('Day', labelpad=5)
ax.xaxis.set_ticks_position('bottom')

# Label the vertical axis with a fractional measure of 'bike availability'.
ax.set_yticks([-1.0, -0.5, 0.0, 0.5, 1.0])
ax.set_ylabel('Morning commute data projected onto the leading PC', labelpad=5) 
ax.yaxis.set_ticks_position('left')   
ax.set_ylim(-1.05, 1.05)
    
# Save plot.
fig.savefig('pc_1_ts.png', dpi=300) 
