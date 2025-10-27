from model.client_model import Client

from api.database import db

def client_register_controller(data):
    new_client = Client(
        name=data["name"],
        cpf=data["cpf"],
        email=data["email"],
        phone=data["phone"],
        user_id=data["user_id"]
    )

    db.session.add(new_client)
    db.session.commit()

    return None
