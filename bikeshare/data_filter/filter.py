import numpy as np
import pandas as pd

    
# Load bike share station data.
df_sd = pd.read_csv('../data/201508_station_data.csv')

# Filter on the San Francisco (SF) stations.
df_sd_sf = df_sd[df_sd['landmark']=='San Francisco']

# Store and save a list of the SF station numbers.
sf_stations = df_sd_sf['station_id'].values
np.savetxt('sf_stations.txt', sf_stations)

# Store and save the latitude and longitude values of each SF station.
ll_matrix = df_sd_sf[['lat', 'long']].values
np.savetxt('ll_matrix.txt', ll_matrix)

# Store the maximum number of bikes at each SF station.
dock_count = df_sd_sf['dockcount'].values.astype('float')


# Load the SF station status data.
df_status = pd.read_csv('../data/201508_status_data.csv')

# Filter on the SF stations.
df_status_sf = df_status[df_status['station_id'].isin(sf_stations)]

# Convert 'time' values to Python's 'datetime64' type.
df_status_sf['time'] = pd.to_datetime(df_status_sf['time'])

# Add a column containing the day of the week, 
# with 0 for Monday, 6 for Sunday, etc.
weekday = lambda x: pd.Timestamp(x).weekday()
df_status_sf['day of week'] = df_status_sf['time'].apply(weekday)

# Add a column containing the hour of the day.
hour = lambda x: pd.Timestamp(x).hour
df_status_sf['hour'] = df_status_sf['time'].apply(hour)

# Create a df of weekday records ('day of week' is 0 on Mondays, 1 on Tuesdays, 
# etc.) between 8:00AM and 9:00AM.
df_weekday = df_status_sf[df_status_sf['day of week'].isin(
    np.array([0, 1, 2, 3, 4]))]
df_weekday = df_weekday[8 == df_weekday['hour']]


# Create and save an array containing the time series of the fraction of bikes 
# available at each SF station.
weekday_data_matrix = []

for station, bike_capacity in zip(sf_stations, dock_count):
    
    df_temp = df_weekday[df_weekday['station_id']==station] 
    weekday_data_matrix.append(
        df_temp['bikes_available'].values / bike_capacity)
    
np.savetxt('weekday_data_matrix.txt', weekday_data_matrix)
