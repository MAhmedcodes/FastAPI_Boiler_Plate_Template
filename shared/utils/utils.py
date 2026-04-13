from passlib.context import CryptContext

#password hashing
pwd_context = CryptContext(schemes="bcrypt", deprecated = "auto")

def hashing(password: str):
    return pwd_context.hash(password)

def verify(pss , hashpass):
    return pwd_context.verify(pss, hashpass)