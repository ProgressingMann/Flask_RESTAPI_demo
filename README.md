# Flask RESTAPI demo

This is a basic flask application which provides demo for the following HOW TOs:
1) How to use flask_smorest, flask_restful and marshmallow along with flask module to create REST APIs. 
2) How to perform unit and integration testing using pytest.

## Follow the below steps linearly to run the flask application
<ol>
      <li> Clone this repository to your local storage.</li>
      <li> Open your terminal and navigate to the directory where you cloned this repository.</li>
      <li> Type <strong>pip install -r requirements.txt</strong> in your terminal and hit enter. This downloads all the dependencies required for the flask app to function             properly.</li>
      <li> Now move to the 'app' folder in the repository by typing cd app.</li>
      <li> Type python app.py to spin the server and this should start your flask application :).</li>    
</ol>


## The code provides 3 endpoints: <br>
**1) '/', (GET)** : A basic home page to get started with.

**2) '/skills/reverse-skill-title', (POST)** : <br> 
      This endpoint requires input data in **JSON** body with key as 'skill_title'.

**3) '/get_data', (POST)** : <br>
      This endpoint requires input data in **JSON** body with key as 'city_name'.<br>
      Responses :-<br>
          a) You will get a 404 response if the JSON body won't contain the key 'city_name'.<br>
          b) You will get a 404 response if the JSON body contains the key 'city_name' but its value (city name) is not present in the data.csv. <br>
          c) You will get a 200 response with Job groups and their respective employment data if key 'city_name' is present in the JSON and its
                  value is also present in the data.csv.

## Unit and Integration Test: <br>
<ol>
      <li> Open your terminal and navigate to the directory where this repository is cloned and then move to the <strong>app</strong> folder.</li>
      <li> Copy the command <strong>python -m pytest -p no:warnings</strong>, paste it in your terminal and hit enter. It's that simple!
</ol>
