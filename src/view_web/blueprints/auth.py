from flask import Blueprint, request, jsonify, render_template, session, redirect, url_for
import uuid
from controller.ControladorUsuarios import ControladorUsuarios
from model.Usuarios import Usuario

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.json
        nombre = data.get('nombre')
        apellido = data.get('apellido')
        correo = data.get('correo')
        usuario = data.get('usuario')
        contraseña = data.get('contrasena')
        if nombre and apellido and correo and usuario and contraseña:
            try:
                # Verificar si el usuario ya existe
                try:
                    ControladorUsuarios.BuscarPorUsuario(usuario)
                    return jsonify({'error': 'El usuario ya existe'})
                except ValueError:
                    pass
                
                new_id = str(uuid.uuid4())
                
                nuevo_usuario = Usuario(nombre=nombre, apellido=apellido, id=new_id, correo=correo, user=usuario, contraseña=contraseña)
                ControladorUsuarios.InsertarUsuario(nuevo_usuario)
                return jsonify({'status': 'success', 'message': 'Usuario registrado exitosamente'})
            except Exception as e:
                return jsonify({'error': str(e)})
        return jsonify({'error': 'Todos los campos son requeridos'})
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.json.get('usuario')
        password = request.json.get('contrasena')
        try:
            user = ControladorUsuarios.BuscarPorUsuario(username)
            if password == user.contraseña:
                return jsonify({'status': 'success', 'message': 'Inicio de sesión exitoso'})
            else:
                return jsonify({'status': 'error', 'message': 'Contraseña incorrecta'})
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)})
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('auth.login'))
