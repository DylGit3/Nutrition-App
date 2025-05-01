# crud/food_crud.py
from models.food import (
    create_food_table,
    add_food,
    get_foods,
    update_food,
    delete_food
)

# create_food_table()


def get_all_foods():
    return get_foods()


def add_food_to_db(food_data):
    if not food_data.get('name'):
        raise ValueError("Food name is required")
    add_food(
        food_data['name'],
        food_data['serving_size'],
        food_data['calories'],
        food_data['protein'],
        food_data['carbs'],
        food_data['fat']
    )
    return {"message": "Food added successfully!"}


def update_food_in_db(food_id, food_data):
    if not food_data.get('name'):
        raise ValueError("Food name is required")
    update_food(
        food_id,
        food_data['name'],
        food_data['serving_size'],
        food_data['calories'],
        food_data['protein'],
        food_data['carbs'],
        food_data['fat']
    )
    return {"message": f"Food with ID {food_id} updated successfully!"}


def delete_food_in_db(food_id):
    delete_food(food_id)
    return {"message": f"Food with ID {food_id} deleted successfully!"}
