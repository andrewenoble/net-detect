import scipy as sp
import pandas as pd
import pylab as pl
import pickle as pk
import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimg
from matplotlib import animation


# Customize the matplotlib environment.
pl.rc_context(fname='../../util/custom_rc')

# Choose a projection for plotting the border of the UK.
proj = ccrs.PlateCarree()

# Import imagery from MapQuest.
imagery = cimg.MapQuestOpenAerial()

# Define plotting and animation parameters.
marker_size_max = 5000 

num_frames = 104
fps = 4
bitrate = 1600
blit = True


# Load the UK measles data.
df = pd.read_excel('../data/60measles.xls', '60measles')

# Create separate arrays for the city names, year, week, and reported cases
# associated with each record (row) in the data set.
cities = sp.asarray(df.columns[2:])
years = sp.asarray(df.values[:, 0])
weeks = sp.asarray(df.values[:, 1])
cases_array = sp.asarray(df.values[:, 2:])

# Calculate the maximum number of cases reported in any single city during any 
# single biweekly period.
max_cases = max(cases_array.flatten())

# Define a function that returns marker sizes proportional to the number of
# reported cases during the ith biweekly period.
def get_marker_sizes(i):
    
    marker_sizes = []
    
    for cases in cases_array[i]:
        
        marker_sizes.append(marker_size_max * cases / max_cases)
        
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
        
        
# Create a base figure that will be updated to create each still in the 
# animation sequence.
fig = pl.figure(figsize=(3.0, 2.7))
ax = pl.axes([0.26, 0.01, 0.70, 0.98], projection=imagery.crs)
ax.set_extent([-4.9, 2.3, 50, 55.2]) # Format is [long_W, long_E, lat_S, lat_N].

# Add a map of the UK to the background of the plot.          
ax.add_image(imagery, 7, alpha=0.3)    
    
# The base figure will be the first still (i = 0) in the animation sequence.    
i = 0

# List the year and week of each biweekly record on the left-hand-side of the 
# base figure.
ax.text(-0.19, 0.55, '19%s' % years[i], fontsize=13, 
    horizontalalignment='center', transform=ax.transAxes)	
ax.text(-0.19, 0.45, 'week %s' % weeks[i], fontsize=13, 
    horizontalalignment='center', transform=ax.transAxes)	
    
# Plot a disk at the location of each of the 60 cities.  The size of the disk
# is directly proportional to the number of reported cases.
im = ax.scatter(longitudes, latitudes, color='b', 
    s=get_marker_sizes(i), marker='o', alpha=0.6, linewidth=0.1, 
    transform=proj)
    
    
# Define a dummy function to initialize the animation.
def init(): return im,

# Define a function called to update the base figure, creating the ith still
# of the animation.
def animate(i):
                      
    im._sizes = get_marker_sizes(i)
    ax.texts[-2].set_text('19%s' % years[i])
    ax.texts[-1].set_text('week %s' % weeks[i]) 
    
    return im,

# Generate the animation.
anim = animation.FuncAnimation(fig, animate, init_func=init, 
    frames=num_frames, blit=blit)


# Save the animation.
anim.save('uk_measles.mp4', fps=fps, bitrate=bitrate,
    extra_args=['-vcodec', 'libx264'])
