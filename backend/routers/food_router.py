from flask import Blueprint, request, jsonify
from crud.food_crud import get_all_foods, add_food_to_db

food_router = Blueprint('food_router', __name__)


@food_router.route('/foods', methods=['GET'])
def list_foods():
    try:
        # returns a list of tuples: (id, name, serving_size, calories, protein, carbs, fat)
        foods = get_all_foods()
        # unpack each tuple into a dict for JSON serialization
        result = [
            {
                'id':       f[0],
                'name':     f[1],
                'serving_size': f[2],
                'calories': f[3],
                'protein':  f[4],
                'carbs':    f[5],
                'fat':      f[6],
            }
            for f in foods
        ]
        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@food_router.route('/foods', methods=['POST'])
def create_food():
    try:
        food_data = request.get_json()
        if not food_data:
            return jsonify({'error': 'No data provided'}), 400

        # this will raise ValueError on bad data
        resp = add_food_to_db(food_data)
        return jsonify(resp), 201

    except ValueError as ve:
        # validation error from CRUD layer
        return jsonify({'error': str(ve)}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500
