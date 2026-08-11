import psycopg2
from config.settings import settings

def get_db_connection():
    try:
        connection = psycopg2.connect(
            host=settings.db_host,
            port=settings.db_port,
            user=settings.db_user,
            password=settings.db_password,
            dbname=settings.db_name
        )
        return connection
    except Exception as e:
        print(f"Error al conectar a PostgreSQL: {e}")
        raise e