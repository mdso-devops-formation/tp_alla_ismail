from pydantic import BaseSettings

class Settings(BaseSettings):
    POSTGRES_USER     : str = 'postgres'
    POSTGRES_PASSWORD : str = 'password'
    POSTGRES_IP       : str = 'localhost'
    POSTGRES_PORT     : str = '5432'
    POSTGRES_DB       : str = 'fastapi_database'

settings = Settings()

"""
class Settings:
    POSTGRES_USER : str = os.getenv("POSTGRES_USER",'postgresql')
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD",'password')
    POSTGRES_IP : str = os.getenv("POSTGRES_IP",'localhost')
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT",'5432') # default postgres port is 5432
    POSTGRES_DB : str = os.getenv("POSTGRES_DB",'fastapi_database')
    # DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_IP}:{POSTGRES_PORT}/{POSTGRES_DB}"
    
settings = Settings()


# DATABASE_URL ="postgresql://postgres:password@localhost:5432/fastapi_database"


"""