from app.database import Base, engine
from app.config import settings
from app.models.prediction import PredictionRecord, ModelInfoRecord

def setup_database():
    """Create all database tables."""
    print(f"Creating tables in: {settings.DATABASE_URL}")
    print(f"Registered tables: {list(Base.metadata.tables.keys())}")  
    
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ create_all() completed successfully")
        
        # Verify tables were actually created
        from sqlalchemy import inspect
        inspector = inspect(engine)
        created_tables = inspector.get_table_names()
        print(f"Tables found after creation: {created_tables}")
        
    except Exception as e:
        print(f"err during table creation: {e}")

if __name__ == "__main__":
    setup_database()