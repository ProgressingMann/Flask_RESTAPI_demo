import marshmallow as ma


class SkillsTitleInputSchema(ma.Schema):
    skill_title = ma.fields.String()
    class Meta:
        unknown = ma.EXCLUDE


class SkillsReverseTitleOutputSchema(ma.Schema):
    skill_title = ma.fields.String()
    reversed_skill_title = ma.fields.String()

class CitySchema(ma.Schema):
    city_name = ma.fields.String()
    class Meta:
        unknown = ma.EXCLUDE

    @ma.post_load
    def return_city(self, data, **kwargs):
        return data