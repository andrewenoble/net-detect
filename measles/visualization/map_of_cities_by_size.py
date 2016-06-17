import scipy as sp
import pandas as pd
import pylab as pl
import pickle as pk
import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimg


# Customize the matplotlib environment.
pl.rc_context(fname='../../util/custom_rc')

# Choose a projection for plotting cities.
proj = ccrs.PlateCarree()

# Import imagery from MapQuest.
imagery = cimg.MapQuestOpenAerial()

# Define plotting parameters.
marker_size_max = 500 


# Load the UK measles data.
df = pd.read_excel('../data/60measles.xls', '60cities')

# Create separate arrays for city names and population sizes.
cities = sp.asarray(df.values[:, 0])
sizes = sp.asarray(df.values[:, 1])

# Calculate the maximum number of cases reported in any single city during any 
# single biweekly period.
max_sizes = max(sizes)

# Define a function that returns marker sizes proportional to city sizes.
def get_marker_sizes():
    
    marker_sizes = []
    
    for size in sizes:
        
        marker_sizes.append(marker_size_max * size / max_sizes)
        
    return marker_sizes
    
# Load a dictionary containing the latitude and longitude coordinates for each 
# city.  (The keys are city names; the values are 2-elements arrays containing
# latitude and longitude coordinates.)
ll_dict = pk.load(open('../data/60latlong.p', 'rb'))

# Create lists of latitude and longitude corresponding to each city name in 
# cities.
latitudes = []
longitudes = []

for city in cities:
    
    latitude, longitude = ll_dict[city]
    
    latitudes.append(latitude)
    longitudes.append(longitude)
    
        
# Create figure.
fig = pl.figure(figsize=(2.52, 3.00))
ax = pl.axes([0., 0., 1., 1.], projection=imagery.crs)
ax.set_extent([-4.9, 2.3, 50.0, 55.2])#Format is [long_W, long_E, lat_S, lat_N].

# Add a map of the UK to the background of the plot.          
ax.add_image(imagery, 7, alpha=0.25)    

# Plot a disk at the location of each of the 60 cities.  The size of the disk
# is directly proportional to the size of the city.
ax.scatter(longitudes, latitudes, color='k', s=get_marker_sizes(), marker='o', 
    alpha=0.5, linewidth=0.1, transform=proj)
     

# Save figure.
fig.savefig('map_of_cities_by_size.png', dpi=300)
