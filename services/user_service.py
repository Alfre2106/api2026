from psycopg2.extras import RealDictCursor
from database.connection import get_db_connection
from schemas.user_schema import UserCreate, UserUpdate

class UserService:

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT id, nombre, correo FROM usuarios;")
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        return users

    @staticmethod
    def get_by_id(user_id: int):
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT id, nombre, correo FROM usuarios WHERE id = %s;", (user_id,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user

    @staticmethod
    def create(user_data: UserCreate):
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(
            "INSERT INTO usuarios (nombre, correo) VALUES (%s, %s) RETURNING id, nombre, correo;",
            (user_data.nombre, user_data.correo)
        )
        new_user = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return new_user

    @staticmethod
    def update(user_id: int, user_data: UserUpdate):
        user = UserService.get_by_id(user_id)
        if not user:
            return None

        updated_name = user_data.nombre if user_data.nombre is not None else user['nombre']
        updated_email = user_data.correo if user_data.correo is not None else user['correo']

        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(
            "UPDATE usuarios SET nombre = %s, correo = %s WHERE id = %s RETURNING id, nombre, correo;",
            (updated_name, updated_email, user_id)
        )
        updated_user = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return updated_user

    @staticmethod
    def delete(user_id: int):
        user = UserService.get_by_id(user_id)
        if not user:
            return False

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = %s;", (user_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True