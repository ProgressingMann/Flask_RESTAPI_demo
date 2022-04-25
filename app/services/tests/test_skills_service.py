""" 
Unit testing script
Write the unit tests for the code in skills_service.py below.  
"""

from services import skills_service
from schema.skills_schema import CitySchema as CS
import data_process as dp

def test_reverse_skill_title():
    '''
    Example unit test.
    '''
    s = 'mann'
    d = skills_service.reverse_skill_title(s)
    assert s == d['reversed_skill_title'][::-1]

def test_data_exists():
    '''
    Check that data.csv exists and is accessible.
    '''
    from os.path import exists
    assert exists('../data.csv')

def test_dataframe_loaded_correctly():
    '''
    Check that we get the desired Dataframe containing the data.csv, and
    a Dictionary name Area codes with keys as cities and values as MSA_ID of respective cities.
    '''
    import pandas as pd
    df, area_codes = dp.get_data()

    assert type(df) == type(pd.DataFrame())
    assert df['Total_Emp'].dtype == int
    assert df['MSA_ID'].dtype == int
    assert df['M_Areas'].dtype == 'O'
    assert type(area_codes) == dict
    assert 'new york' in area_codes