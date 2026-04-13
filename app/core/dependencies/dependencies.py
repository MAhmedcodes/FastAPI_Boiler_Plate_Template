from app.core.Database.database import Sessionlocal

#database dependency
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()