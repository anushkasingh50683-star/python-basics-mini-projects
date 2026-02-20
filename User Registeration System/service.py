from database import insert_user


def register_user(name):
    name = name.strip()

    if not name :
        return "Error : Name cannot be empty"
    
    if len(name) < 3:
        return "Error : Name must be at least 3 characters long"
    
    insert_user(name)

    return "User registered successfully."
