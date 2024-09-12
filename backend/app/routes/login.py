from flask import request, jsonify, Blueprint
from app.models.Usuario import Usuario
from app import db
from werkzeug.exceptions import HTTPException

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/registro', methods=['POST'])
def registro():
    try:
        data = request.get_json()  # Recibe los datos en formato JSON
        print(f"Datos recibidos: {data}")  # Verifica qué datos estás recibiendo

        # Extraer los campos que el usuario ingresa
        id = data.get('id')
        nombres = data.get('nombres')
        apellidos = data.get('apellidos')
        password = data.get('password')
        email = data.get('email')

        # Validar que todos los campos obligatorios están presentes
        if not id or not nombres or not apellidos or not password or not email:
            return jsonify({'error': 'Faltan campos obligatorios'}), 400

        # Verificar si el ID o el email ya están registrados
        usuario_existente = Usuario.query.filter((Usuario.id == id) | (Usuario.email == email)).first()
        if usuario_existente:
            return jsonify({'error': 'El ID o el email ya están en uso'}), 400

        # Crear un nuevo usuario
        nuevo_usuario = Usuario(id=id, nombres=nombres, apellidos=apellidos, password=password, email=email)
        db.session.add(nuevo_usuario)
        db.session.commit()

        return jsonify({'message': 'Usuario creado exitosamente'}), 201

    except Exception as e:
        print(f"Error específico: {e}")  # Muestra el error en la consola
        db.session.rollback()  # Revertir si hay un error
        return jsonify({'error': f'Error en el registro: {str(e)}'}), 400

    
    
@login_blueprint.route('/login', methods=['POST'])
def login():
    try:
        id = request.json.get('id')
        password = request.json.get('password')
        
        # Verificar en la base de datos si el usuario existe
        usuario = Usuario.query.filter_by(id=id).first()
        if usuario is None:
            return jsonify({'error': 'Usuario no encontrado'}), 404
        if usuario.password != password:
            return jsonify({'error': 'Contraseña incorrecta'}), 401
        return jsonify({'message': 'Bienvenido!'}), 200
    except HTTPException as e:
        return jsonify({'error': str(e.description)}), e.code
    except Exception as e:
        return jsonify({'error': 'Error interno del servidor'}), 500

