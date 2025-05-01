# crud/user_crud.py
from models.user import (
    create_user_table,
    add_user_sql,
    get_user_by_username_sql,
    get_user_by_id_sql,
)
from utils.security import hash_password, check_password

# ensure the users table is created
create_user_table()


def register_user(user_data: dict):
    """
    Validate input, hash the password, then delegate to the model.
    Expects {'username': str, 'password': str}.
    """
    username = user_data.get('username')
    password = user_data.get('password')
    if not username or not password:
        raise ValueError("Both username and password are required")
    if get_user_by_username_sql(username):
        raise ValueError(f"Username '{username}' is already taken")

    hashed = hash_password(password)
    add_user_sql(username, hashed)
    return {"message": f"User '{username}' created successfully"}


def authenticate_user(username: str, password: str):
    """
    Fetch stored hash, verify password, and return the user tuple on success.
    Otherwise return None.
    """
    user = get_user_by_username_sql(username)
    if not user:
        return None

    _, _, stored_hash = user  # Tuple unpacking
    if check_password(stored_hash, password):
        return user
    return None


def find_user_by_id(user_id: int):
    """Return the user tuple (id, username, password) or None."""
    return get_user_by_id_sql(user_id)
