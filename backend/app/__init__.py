from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configuración de la aplicación
    app.config.from_object('app.config.Config')
    
    # Inicializar la base de datos
    db.init_app(app)
    
    # Configurar CORS
    CORS(app)
    
    # Importar y registrar las rutas
    from app.routes.login import login_blueprint
    app.register_blueprint(login_blueprint)
    
    with app.app_context():
        db.create_all()
    
    return app
