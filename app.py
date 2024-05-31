from flask import Flask, render_template, redirect, url_for
import os
import sys

# Asegúrate de que src esté en sys.path para poder importar módulos de la aplicación
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Importa los Blueprints después de configurar sys.path
from view_web.blueprints.compress import compress_bp
from view_web.blueprints.auth import auth_bp

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(__file__), 'src', 'view_web', 'templates'),
        static_folder=os.path.join(os.path.dirname(__file__), 'src', 'view_web', 'static')
    )
    
    # Configuración de una clave secreta para sesiones (requerido para flash messages)
    app.config['SECRET_KEY'] = 'supersecretkey'
    
    # Registra los Blueprints
    app.register_blueprint(compress_bp)
    app.register_blueprint(auth_bp)

    @app.route('/')
    def index():
        return render_template('inicio.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
