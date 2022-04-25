'''
This file is used to clean, preprocess and transform the data.csv using pandas Data Frame.
'''

import pandas as pd
import numpy as np
import json

def get_data():
    '''
    This function is used to load, clean, and transform the data in data.csv into a Dataframe and 
    extract city names with their respective MSA_ID.

    Returns:
        df (pd.DataFrame) : Cleaned Dataframe containing data from data.csv with changed column names
        area_codes (dict) : dictionary containing city_name as keys and values as MSA_ID.
    '''
    df = pd.read_csv('../data.csv') # Reading the data into pandas DafaFrame
    df.rename(columns={'Metro Area': 'M_Areas', 'Job Group': 'Job_Groups', 
                    'Total Employment': 'Total_Emp'}, inplace=True) # Renaming the column names 

     # Replacing missing values with 0 and then converting the Total Employment values to integer.
    df['Total_Emp'] = df['Total_Emp'].replace(np.nan, 0).astype(int)

    
    area_codes = {} # Dictionary to store cities with their respective MSA_ID.
    for area in df['M_Areas'].unique():
        for city in area.split(',')[0].split('-'):
            area_codes[city.lower()] = (df[df['M_Areas'] == area]['MSA_ID']).unique()[0]

    return df, area_codes
    
def get_employment_data(df, city_code):
    '''
    This function is used to get job groups with their corresponding employment data for a given city.

    Inputs:
        df (pd.DataFrame): This dataframe object contains the job groups and employment data.
        city_code (str) : Name of the city whose employment data is requested.
    
    Outputs:
        (JSON) : Job groups are the keys with their correspoding employment data as their values.
    '''
    # Extracting data for the given city_code only
    ndf = df[df['MSA_ID'] == city_code]
    # Extracting the columns of interest.
    ndf = ndf[['Job_Groups', 'Total_Emp']]

    # Formatting the data as per requirements. 
    # NOTE: Thier are multiple ways to format the below extracted data.
    ndf.set_index('Job_Groups', inplace=True)
    ndf = ndf.T
    json_data = json.dumps(ndf.to_dict(orient='index')['Total_Emp'])
    return json.loads(json_data)
