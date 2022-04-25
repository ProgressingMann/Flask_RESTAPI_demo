from api.skills_resource import skills_bp, gd_blp


def init_app(app):
    '''
    Registering the blueprints
    '''
    app.register_blueprint(blp=skills_bp)
    app.register_blueprint(blp=gd_blp)