# from app.factory import create_app
# from flask_restful import Resource, Api
from factory import create_app
# from flask import request, render_template, url_for, jsonify
# from schema.skills_schema import CitySchema as CS

# from marshmallow import ValidationError
# import data_process as dp

# app = create_app()
# api = Api(app)

# df, area_codes = dp.get_data()
# cities = list(area_codes.keys())

# def city_exists(city_name):
#     '''
#     Checks whether the given city name exists in our data (the data.csv in our case) or not.
#     Input: Name of the city
#     Output: None
#     Handles: Returns a 404 response in case the city name is not found.
#     '''
#     if city_name not in cities:
#         abort(404, message=f'City with name {city_name} does not exist!')

# class GetData(Resource):
#     def get(self, city_name):
#         d = {'city_name': city_name}
#         try:
#             schema = CS()
#             city = schema.load(d) # Checks whether city name is a string or not
#             city_name = schema.dump(city)['city_name'] # Get back our city name
#             city_name = city_name.lower() # Convert to lower case to handle Upper and Lower case mismatches
#             city_exists(city_name=city_name) # Check whether the entered city name exists in our list of cities or not.
#             city_code = area_codes[city_name] 
#             employment_data = dp.get_employment_data(df, city_code)
#             # print(jsonify(employment_data))
#             # return jsonify(employment_data)
#             return employment_data

#         # As name of city has to ba string, we return exception when city name is not a string.
#         except ValidationError as err: 
#             print(err)
#             return err

    
# # Note: There are multiple ways to pass the city name, such as passing it using a query string.
# api.add_resource(GetData, '/<string:city_name>')
# # api.add_resource()

app = create_app()
app.run(debug=True)