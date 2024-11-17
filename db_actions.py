from db import Gym_Bro, Session


def add_client(name,text):
    with Session() as session:
        client = Gym_Bro(name=name,  text=text)
        session.add(client)
        session.commit()
        session.refresh(client)
        return client.id
    
    
def get_Gym_Bro():
    with Session() as session:
        return session.query(Gym_Bro).all()
    

def get_client(id):
    with Session() as session:
        return session.query(Gym_Bro).where(Gym_Bro.id == id).first()


def update_client(id, name, text):
    with Session() as session:
        client =  session.query(Gym_Bro).filter_by(id=id).first()
        client.name = name
        client.text = text
        session.commit()
        return "Дані Оновлени"
        
        
def delete_client(id):
    with Session() as session:
        client = session.query(Gym_Bro).filter_by(id=id).first()
        session.delete(Gym_Bro)
        session.commit()
        return "У відвідувача скінчився обонімент"