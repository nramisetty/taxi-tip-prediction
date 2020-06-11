#File to store functions for preprocessing pandas dataframe and h2o dataframes
import pandas as pd
import numpy as np
import h2o

def preprocess(data):
    #filtering out for just credit card values
    data = data[data['payment_type']==1] # only credit cards
    data = data[data['trip_distance'] != 0.0] # don't want any trips that didn't go anywhere
    data=data.drop(['store_and_fwd_flag','ehail_fee','payment_type','VendorID'],axis=1)
    
    #cleaning some of the data, negative values of taxes and extra charges set to NaN
    data.loc[data['improvement_surcharge'] < 0, 'improvement_surcharge'] = np.NaN
    data.loc[data['extra'] < 0, 'extra'] = np.NaN
    data.loc[data['mta_tax'] < 0, 'mta_tax'] = np.NaN
    data.reset_index(drop=True,inplace=True)
    
    #changing the DateTime to Unix timestamp to have interval data
    #We subtract the timestamp of new years of the given year because we want a predictor to work regardless of year
    #But we assume month of the year to be important
    def dt2Unix(row,idx):
        #print(row[idx])
        dt = pd.to_datetime(row[idx], format='%Y-%m-%d %H:%M:%S').tz_localize('EST')
        year = pd.Timestamp(year = dt.year, month = 1, day = 1).tz_localize('EST')
        date=dt.timestamp()
        return int(date - year.timestamp())
    
    #changing out the datetime for unix stamps with function above
    data.insert(0,'unix_pickup',data.apply(dt2Unix,idx=0,axis=1))
    data.insert(1,'unix_dropoff',data.apply(dt2Unix,idx=2,axis=1))
    data=data.drop(['lpep_pickup_datetime','lpep_dropoff_datetime'],axis=1)
    data = data[data['unix_pickup'] >= 0]
    
    #Trip duration by itself might help
    data.insert(2,'trip_duration',data['unix_dropoff'] - data['unix_pickup'])
    #Filter out any trips that wereimmediately cancelled
    data = data[data['trip_duration'] > 0]
    
    #moving tip amount to the end
    col_names = data.columns.tolist()
    col_names.remove('tip_amount')
    col_names.append('tip_amount')
    data = data[col_names]
    data.insert(data.shape[1], 'did_tip',(data['tip_amount'] != 0).astype(int))
    
    return data

def process_df(df):
    #setting these columns to categorical for h2o dataframe
    cat_columns = ['RatecodeID','PULocationID','DOLocationID','trip_type','did_tip']
    for category in cat_columns:
        df[:,category] = df[:,category].asfactor()
    
    return df

