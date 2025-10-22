def no_users_found_middleware(data):
    if not data:
        return "No users found!"
    
    return None