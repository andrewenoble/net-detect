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
left = 0.01
bottom = 0.01
width = 0.98
height = 0.98

ll_scale_factor = 12.

    
# Load filtered data.
sf_stations = sp.loadtxt('../data_filter/sf_stations.txt')
ll_matrix = sp.loadtxt('../data_filter/ll_matrix.txt')
weekday_data_matrix = sp.loadtxt('../data_filter/weekday_data_matrix.txt')

# Choose the geographic area to plot based on the latitudes and longitudes of
# all stations (as contained in 'll_matrix').   
lat_min, lat_max = min(ll_matrix.T[0]), max(ll_matrix.T[0]) 
long_min, long_max = min(ll_matrix.T[1]), max(ll_matrix.T[1]) 
lat_offset = (lat_max - lat_min) / ll_scale_factor
long_offset = (long_max - long_min) / ll_scale_factor


# Plot all station locations.
fig = pl.figure(figsize=(3.2, 4.4))
ax = pl.axes([left, bottom, width, height], projection=imagery.crs)
ax.set_extent([long_min - long_offset, long_max + long_offset, 
    lat_min - lat_offset, lat_max + lat_offset])
            
# Add a map of San Francisco to the background of the plot.          
ax.add_image(imagery, 14, alpha=0.25)        
    
# Mark station locations using a black disk on a white square.  (Otherwise, 
# the disks are difficult to see against the colors of the map in the 
# background.)
ax.scatter(ll_matrix.T[1], ll_matrix.T[0], color='w',
    s=60., marker='s', edgecolor='none', transform=proj)
    
ax.scatter(ll_matrix.T[1], ll_matrix.T[0], color='k',
    s=30., marker='o', edgecolor='k', linewidth='0.25', transform=proj)
        
# Save plot.        
fig.savefig('map.png', dpi=300)   


# Plot the locations of stations 73 and 82.
station_index_list = [-6, -1]

fig = pl.figure(figsize=(3.2, 4.4))
ax = pl.axes([left, bottom, width, height], projection=imagery.crs)
ax.set_extent([long_min - long_offset, long_max + long_offset, 
    lat_min - lat_offset, lat_max + lat_offset])

# Add a map of San Francisco to the background of the plot.                                  
ax.add_image(imagery, 14, alpha=0.25)   
    
# Mark the two station locations with the station number in black letters on a
# white square.
for i in station_index_list: 
       
    ax.scatter(ll_matrix.T[1][i], ll_matrix.T[0][i], color='w',
        s=90., marker='s', edgecolor='none', transform=proj) 
           
    ax.scatter(ll_matrix.T[1][i], ll_matrix.T[0][i], color='k',
        s=60., marker=r'$ {} $'.format(str(int(sf_stations[i]))), edgecolor='k', 
        linewidth='0.25', transform=proj)
    
# Save plot.            
fig.savefig('map_two.png', dpi=300)          
