""" 
Integration testing script 
Write the integration tests for the code in skills_resource.py below.
"""
import data_process as dp
import json

df, area_codes = dp.get_data()

mimetype = 'application/json'
headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
}

def test_example_skills_resource(client):
    '''
    When the '/' page is routed to the GET Request,
    Then check that it returns status 200 with valid response data.
    '''
    skills_dict = {'skill_title' : 'mann'}
    response = client.post('/skills/reverse-skill-title', json=skills_dict)
    assert response.status_code == 200
    assert b'nnam' in response.data

def test_home_page(client):
    '''
    When the '/' page is routed to the GET Request,
    Then check that it returns a 200 status code.
    '''
    response = client.get('/')
    assert response.status_code == 200
    assert b'Enter City name to display data' in response.data

def test_invalid_path(client):
    '''
    When any path other than '/get_data' or '/' is hit,
    Then check that it Returns a 404 status (page does not exists).
    '''
    response = client.get('/anypage')
    assert response.status_code == 404

def test_invalid_data_key(client):
    '''
    When the '/get_data' page is hit with a GET request,
    Check that it has an invalid dictionary key, similar to the field name in our CitySchema ('city_name'), and
    Return a 404 status code when key 'city_name' is not found.
    '''
    data = {'city': 'new york'}
    response = client.post('/get_data', json=data)
    assert response.status_code == 404
    assert b'Please check your input data type and json keys!' in response.data

def test_city_not_found(client):
    '''
    When the '/get_data' page is hit with a GET request,
    Check that when a city does not exist in our data.csv, 
    Then it Returns a 404 status code.
    '''
    data = {'city_name' : 'boston'}
    response = client.post('/get_data', json=data, headers=headers)
    assert response.status_code == 404
    assert b'Given city does not exist!' in response.data


def test_valid_data(client):
    '''
    When the '/get_data' page is hit with a GET request,
    Check that the city exists in our data.csv, and
    Return a 200 status code with job groups and total employment data.
    '''
    data = {'city_name' : 'new york'}
    response = client.post('/get_data', json=data, headers=headers)
    response_dict = json.loads(response.data)

    assert response.status_code == 200
    assert len(response_dict) > 0
    # Check that Actors job group (present in our data.csv) is present in the json keys.
    assert 'Actors' in response_dict
    # Values of the json data must be integers, as humans can't be fractions.
    assert type(response_dict['Actors']) == int 