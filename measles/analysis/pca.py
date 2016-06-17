import sys
sys.path.append('../../util/') 
import libe
import scipy as sp
import pandas as pd
import pylab as pl
import pickle as pk
import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimg

# Customize the matplotlib environment.
pl.rc_context(fname='../../util/custom_rc')

# Choose a projection for plotting station locations.
proj = ccrs.PlateCarree() 

# Import imagery from MapQuest.
imagery = cimg.MapQuestOpenAerial()

# Define plotting parameters.
scale_of_reported_cases = 1e4


# Load the UK measles data.
df = pd.read_excel('../data/60measles.xls', '60measles')

# Create separate arrays for the city names, year, week, and reported cases
# associated with each record (row) in the data set.
cities = sp.asarray(df.columns[2:])
years = sp.asarray(df.values[:,0])
weeks = sp.asarray(df.values[:,1])
data_matrix = sp.asarray(df.values[:,2:])

# Create array recording each time point as a fraction of a year.
times = sp.linspace(years[0] + 1900 + 0./26, years[-1] + 1900 + 25./26, 
    len(years))
    
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


# Perform the PCA.  Store the leading and subleading principal components (pc's) 
# in 'v'.  Store the fractions of total variation described by each pc in 'w'.  
# In both of the two-component 'v' and 'w' arrays, the first elements correspond 
# to the subleading pc; the second elements to the leading pc.
w, v = libe.pca_2(data_matrix.T)

# Save the fractions of total variation described by each pc.
sp.savetxt('w.txt', w)  
    
    
# Define a function that plots each pc of variation on a map.   
def plot(color_array, title, name): 
    
    fig = pl.figure(figsize=(3.2, 4.4))
    ax = pl.axes([0.01, 0.01, 0.98, 0.98], projection=imagery.crs)
    ax.set_extent([-4.9, 2.3, 50.0, 55.2])#Format is [long_W, long_E, lat_S, lat_N].

    # Add a map of the UK to the background of the plot.          
    ax.add_image(imagery, 7, alpha=0.25)       
        
    # Mark the value of the pc at each station location using a disk, of a 
    # color specified in 'color_array', on a white square.  (Otherwise, 
    # the disks are difficult to see against the colors of the map in the 
    # background.)        
    ax.scatter(longitudes, latitudes, color='w',
        s=60., marker='s', edgecolor='none', transform=proj)
        
    ax.scatter(longitudes, latitudes, color=color_array,
        s=30., marker='o', edgecolor='k', linewidth='0.25', transform=proj)
        
    # Add a title.
    ax.text(0.5, 0.85, title, fontsize=10, horizontalalignment='center', 
        transform=ax.transAxes)        
        
    # Save the plot.    
    fig.savefig(name, dpi=300)
    
    pass
        
    
# Plot the leading ('1') pc on a map.  
pc_1 = v.T[1]
pc_1_color_array = libe.make_color_array(pc_1)
plot(pc_1_color_array, 'Leading Principal Component', 'pc_1.png')

# Plot the subleading ('0') pc on a map.  Choose the overall sign (which is
# arbitrary) such that the disk covering London is blue.
pc_0 = v.T[0]
pc_0_color_array = libe.make_color_array(-pc_0)
plot(pc_0_color_array, 'Subleading Principal Component', 'pc_0.png')


# The times series of case reports for each city can be decomposed into
# projections onto each of the pc's.  Here, calculate projections onto the 
# leading and subleading pc's.
london_pc_1_ts = sp.dot(data_matrix, -v.T[1]) * (-v.T[1][26])      
birm_pc_1_ts = sp.dot(data_matrix, -v.T[1]) * (-v.T[1][2]) 

london_pc_0_ts = sp.dot(data_matrix, -v.T[0]) * (-v.T[0][26])      
birm_pc_0_ts = sp.dot(data_matrix, -v.T[0]) * (-v.T[0][2]) 


# Plot a time series of the leading pc projected onto the London and Birmingham 
# data.
fig = pl.figure(figsize=(6., 4.))
ax = pl.axes([0.08, 0.09, 0.91, 0.90])

# Plot the London time series as a black line.
pl.plot(times, london_pc_1_ts / scale_of_reported_cases, 'k-', lw=1.00, 
    label='London', alpha=0.8)
    
# Plot the Birmingham time series as a red line.                        
pl.plot(times, birm_pc_1_ts / scale_of_reported_cases, 'r-', lw=0.75, 
    label='Birmingham', alpha=0.8)    

# Label the horizontal axis with the year.   
ax.set_xlabel('Year', labelpad=5) 
ax.set_xlim(1943.75, 1967.25)
ax.xaxis.set_ticks_position('bottom')

# Label the vertical axis with a description of the projection.
ax.set_ylabel('Case report data by city projected onto the leading PC', 
    labelpad=5)    
ax.set_ylim(-0.02, 0.79) 
ax.yaxis.set_ticks_position('left')

# Add a legend.  
ax.legend(numpoints = 1, loc = 0, markerscale=0.5, handlelength=1.5,
    borderpad=0.2, labelspacing=0.3) 
    
# Add title.    
ax.text(0.2, 0.95, 'Leading projection', horizontalalignment='center', 
    transform=ax.transAxes)    
        
# Save plot.
fig.savefig('london_birm_pc_1_ts.png', dpi=300) 

 
# Plot a time series of the subleading pc projected onto the London and 
# Birmingham data.
fig = pl.figure(figsize=(6., 4.))
ax = pl.axes([0.08, 0.09, 0.91, 0.90])

# Plot the London time series as a black line.
pl.plot(times, london_pc_0_ts / scale_of_reported_cases, 'k-', lw=1.00, 
    label='London', alpha=0.8)
    
# Plot the Birmingham time series as a red line.                        
pl.plot(times, birm_pc_0_ts / scale_of_reported_cases, 'r-', lw=0.75, 
    label='Birmingham', alpha=0.8)    

# Label the horizontal axis with the year.   
ax.set_xlabel('Year', labelpad=5) 
ax.set_xlim(1943.75, 1967.25)
ax.xaxis.set_ticks_position('bottom')

# Label the vertical axis with a description of the projection.
ax.set_ylabel('Case report data by city projected onto the subleading PC', 
    labelpad=5)    
ax.set_yticks([-0.1, 0.0, 0.1])
ax.set_ylim(-0.152, 0.152) 
ax.yaxis.set_ticks_position('left')

# Add a legend.  
ax.legend(numpoints = 1, loc = 0, markerscale=0.5, handlelength=1.5,
    borderpad=0.2, labelspacing=0.3) 
    
# Add title.
ax.text(0.2, 0.95, 'Subleading projection', horizontalalignment='center', 
    transform=ax.transAxes)        
    
# Save plot.
fig.savefig('london_birm_pc_0_ts.png', dpi=300)    
