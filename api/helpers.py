from passlib.context import CryptContext

pwd = CryptContext(
    schemes=['bcrypt'],
    deprecated='auto'
)

def get_hash(
        password: str
    ):
    hashed_password = pwd.hash(secret=password)
    return hashed_password

def verify_hash(
        password: str,
        hashed_password: str
    ):
    return pwd.verify(secret=password, hash=hashed_password)
