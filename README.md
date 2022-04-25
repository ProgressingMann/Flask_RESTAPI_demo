# Flask_RESTAPI_demo

This is a basic flask application which provides demo for the following HOW TOs:
1) How to use flask_smorest, flask_restful and marshmallow along with flask module to create REST APIs. 
2) How to perform unit and integration testing with pytest.

The code provides 3 endpoints: <br>
**1) '/', (GET)** : a basic home page to get started with

**2) '/skills/reverse-skill-title', (POST)** : <br> 
      This endpoint requires input data in **JSON** body with key as 'skill_title'.

**3) '/get_data', (POST)** : <br>
      This endpoint requires input data in **JSON** body with key as 'city_name'.<br>
      Responses :-<br>
          a) You will get a 404 response if the JSON body won't contain the key 'city_name'.<br>
          b) You will get a 404 response if the JSON body contains the key 'city_name' but its value (city name) is not present in the data.csv.<br>
          c) You will get a 200 response with Job groups and their respective employment data if key 'city_name' is present in the JSON and its <br>
                  value is also present in the data.csv.
