from sqlalchemy import String, create_engine
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, Mapped, DeclarativeBase


engine = create_engine("sqlite:///clients.db", echo=True)
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass

        
class Gym_Bro(Base):
    __tablename__ = "clients"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    text: Mapped[str] = mapped_column(String())
    

def create_db():
    Base.metadata.create_all(bind=engine)