from flask import Flask
from models.food import create_food_table  # Import food table creation function
from models.user import create_user_table  # Import user table creation function
from routers.food_router import food_router  # Import the food router blueprint
from routers.user_router import user_router  # Import the user router blueprint

app = Flask(__name__)

create_food_table()
create_user_table()

# Register the blueprints for food and user routes
app.register_blueprint(food_router)
app.register_blueprint(user_router)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
