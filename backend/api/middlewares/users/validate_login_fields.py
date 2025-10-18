def validate_login_fields(data):
    required_fields = ['username', 'password']

    for field in required_fields:
        if field == "" or not data[field]:
            return f"{field} is required"
    
    return None