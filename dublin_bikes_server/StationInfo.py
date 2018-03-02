from link_to_mysql import *
import pymysql
import numpy as np
import pandas as pd
import json

class StationInfo(object):
    def __init__(self, staticStation, dynamicStation_d, dynamicStation_h):
        self.staticStation = staticStation
        self.dynamicStation_d = dynamicStation_d
        self.dynamicStation_h = dynamicStation_h

def fetch_station_info():

    # get connection of MySQL server
    engine = connect_to_sql()

    # query static data
    stm = "SELECT distinct s.*, rs.banking, rs.bonus, rs.status, rs.bike_stands \
          FROM dublinbikes.stations as s, dublinbikes.stations_real_time as rs where s.number = rs.number"

    df_static = pd.read_sql_query(stm, engine)
    static_string = df_static.to_json()
    #print(static_string)
    # number of station (bad.....)
    number_of_station = df_static['number'].max()

    #----------------dynamtic data by station by days and hours----------------#
    # query dynamtic data by time
    stm = "SELECT number, banking, bonus, bike_stands, available_bike_stands, available_bikes, last_update_date FROM dublinbikes.stations_real_time \
          where last_update_date between '2017-03-26 00:00' and '2017-04-02 00:00'"
    df_realtime = pd.read_sql_query(stm, engine)

    # add new column for time to hour
    df_realtime['date_by_hour'] = df_realtime['last_update_date'].apply(lambda x:x.strftime('%D %H'))

    # store by station number -- 3hrs
    realtime_string = "{"
    for i in range(number_of_station):
        df = df_realtime.loc[ df_realtime[(df_realtime['number'] == i+1 )].index ]
        res = df.groupby(df['date_by_hour']).mean()
        res['available_bikes'] = res['available_bikes'].round()
        res = res.T
        realtime_string += '"' + str(i+1) + '":' + res.to_json() + ','
    realtime_string = realtime_string[:-1] + '}'
    
    #----------------dynamtic data by station by hours (average)----------------#

    df_realtime['by_hour'] = df_realtime['last_update_date'].apply(lambda x: x.strftime('%H'))

    # store by station number -- by hour average
    realtime_hour_string = "{"
    for i in range(number_of_station):
        df = df_realtime.loc[df_realtime[(df_realtime['number'] == i + 1)].index]
        res = df.groupby(df['by_hour']).mean()
        res['available_bikes'] = res['available_bikes'].round()
        res = res.T
        realtime_hour_string += '"' + str(i + 1) + '":' + res.to_json() + ','

    realtime_hour_string = realtime_hour_string[:-1] + '}'
    
    stations = StationInfo(static_string, realtime_string, realtime_hour_string)
    return stations


if __name__ == '__main__':
    fetch_station_info()