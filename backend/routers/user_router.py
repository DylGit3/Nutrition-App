from flask import Blueprint, request, jsonify
from crud.user_crud import register_user, authenticate_user, find_user_by_id

user_router = Blueprint('user_router', __name__)


@user_router.route('/user/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        resp = register_user(data)
        return jsonify(resp), 201

    except ValueError as ve:
        # thrown by register_user on missing fields or duplicate username
        return jsonify({'error': str(ve)}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@user_router.route('/user/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400

        user = authenticate_user(username, password)
        if not user:
            return jsonify({'error': 'Invalid credentials'}), 401

        user_id, user_name, _ = user
        return jsonify({
            'message': 'Login successful',
            'id': user_id,
            'username': user_name
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@user_router.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = find_user_by_id(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        uid, uname, _ = user
        return jsonify({
            'id': uid,
            'username': uname
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
