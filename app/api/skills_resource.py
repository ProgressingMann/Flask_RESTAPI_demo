from typing import Dict, List, Any
from flask_restful import Resource, abort
from flask_smorest import Blueprint
from flask import request
from schema.skills_schema import (
    SkillsTitleInputSchema,
    SkillsReverseTitleOutputSchema,
    CitySchema as CS
)
from services import skills_service as skills_svc
from marshmallow import ValidationError

import data_process as dp

skills_bp = Blueprint("Skills", __name__, description="Skills Endpoints")


@skills_bp.route("/skills/reverse-skill-title")
class SkillsReverseTitleResource(Resource):
    @skills_bp.arguments(SkillsTitleInputSchema)
    @skills_bp.response(status_code=200, schema=SkillsReverseTitleOutputSchema)
    def post(self, body: Dict[str, str]):
        """ Reverse and lowercase the skill title word """
        reverse_skill_title_output = skills_svc.reverse_skill_title(
            external_skill_title=body["skill_title"]
        )
        return reverse_skill_title_output


df, area_codes = dp.get_data()
cities = list(area_codes.keys())

def city_exists(city_name):
    '''
    Checks whether the given city name exists in our data (the data.csv in our case) or not.
    Inputs: 
        city_name (str) : Name of the city
    Exceptions: 
        Abort with a 404 response in case the city name is not found.
    '''
    if city_name not in cities:
        abort(404, message=f'Given city does not exist!')


gd_blp = Blueprint("gd_blp", __name__, description="Data Retreiving Endpoint")

@gd_blp.route('/')
def home():
    return 'Enter City name to display data'

@gd_blp.route('/get_data')
class GetDataResource(Resource):
    @gd_blp.arguments(schema=CS, unknown=None)
    @gd_blp.response(status_code=200)
    def post(self, args):
        if args == {}:
            abort(404, message=f'Please check your input data type and json keys!')
        try:
            schema = CS()
            city = schema.load(args) # Checks whether city name is a string or not
            city_name = schema.dump(city)['city_name'] # Get back our city name
            city_name = city_name.lower() # Convert to lower case to handle Upper and Lower case mismatches
            city_exists(city_name=city_name) # Check whether the entered city name exists in our list of cities or not.
            city_code = area_codes[city_name] 
            employment_data = dp.get_employment_data(df, city_code)
            return employment_data

        # As name of city has to be string, we return exception when city name is not a string.
        except ValidationError as err: 
            abort(404, message=f'Please check your input data type and json keys!')