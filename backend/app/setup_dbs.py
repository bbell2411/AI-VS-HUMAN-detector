from app.database import Base, engine

def setup_database():
    """Create all database tables."""
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    setup_database()
    

#another table and columns for model_info 
#tests!
#schema or this func? same thing or?