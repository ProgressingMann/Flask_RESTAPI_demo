from schema.skills_schema import CitySchema

def valid_city_name(city_name):
    d = {'city_name': city_name}
    schema = CitySchema()
    city = schema.load(d)


def reverse_skill_title(external_skill_title: str) -> dict:
    """ Reverse and lowercase the skill title string """
    reversed_skill_title = external_skill_title[::-1].lower()
    output = {
        "skill_title": external_skill_title,
        "reversed_skill_title": reversed_skill_title,
    }
    return output