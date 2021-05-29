traffic = traffic.rename(columns={'road_km':'camera_closest_idx_km'})
traffic_mean = traffic.groupby(['datetime', 'camera_closest_idx_km']).agg({'volume': [np.mean, np.max, np.min],
                                                                           'occupancy': [np.mean, np.max, np.min],
                                                                           'speed': [np.mean, np.max, np.min]}
                                                                         ).reset_index()
traffic_mean

# Perform merge  of traffic with df
df_traffic = df.merge(traffic_mean, on=['datetime', 'camera_closest_idx_km'],
                      how = 'left', suffixes=('_traffic', '_mean'))
df_traffic

traffic_mean.columns = ['datetime', 'camera_closest_idx_km', 'volume_mean', 'volume_max', 'volume_min',
                        'occupancy_mean','occupancy_max', 'occupancy_min', 'speed_mean', 'speed_max',
                        'speed_min']
traffic_mean