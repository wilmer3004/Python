from flask import Flask
from flask_cors import CORS

# Routes
from .routes import IndexRoutes, ProgramaRoutes, TypeDocRoutes, JornadaRoutes, AmbienteRoutes,TrimestreRoutes

app = Flask(__name__)

def init_app(config):
    # Configuración
    app.config.from_object(config)

    # Habilitar CORS para un dominio en especifico  en todos los endpoints
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Blueprints
    app.register_blueprint(IndexRoutes.main, url_prefix='/')
    # Tipo de documento
    app.register_blueprint(TypeDocRoutes.main, url_prefix='/TypeDoc')
    # Jornada
    app.register_blueprint(JornadaRoutes.main, url_prefix='/Jornada')
    # Ambiente
    app.register_blueprint(AmbienteRoutes.main, url_prefix='/Ambiente')
    # Trimestres
    app.register_blueprint(TrimestreRoutes.main, url_prefix='/Trimestre')
    # Programas
    app.register_blueprint(ProgramaRoutes.main, url_prefix='/Programa')
    
    return app
