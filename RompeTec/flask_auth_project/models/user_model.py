import psycopg2
import bcrypt
from config import Config

class UserModel:
    def __init__(self):
        self.conn = psycopg2.connect(Config.SQLALCHEMY_DATABASE_URI)
        self.cursor = self.conn.cursor()

    def create_user(self, nombre, username, email, telefono, ciudad, password, token):
        self.cursor.execute("""
            INSERT INTO users (nombre, username, email, telefono, ciudad, password, token, active)
            VALUES (%s, %s, %s, %s, %s, %s, %s, FALSE)
        """, (nombre, username, email, telefono, ciudad, password, token, False))
        self.conn.commit()

    def get_user_by_email(self, email):
        self.cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        row = self.cursor.fetchone()
        return self.row_to_dict(row)

    def get_user_by_id(self, user_id):
        self.cursor.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
        row = self.cursor.fetchone()
        if row:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, row))
        return None

    def check_password(self, email, password):
        self.cursor.execute("SELECT password FROM usuarios WHERE email = %s", (email,))
        row = self.cursor.fetchone()
        if row and bcrypt.checkpw(password.encode(), row[0].encode()):
            return True
        return False

    def delete_user(self, user_id):
        self.cursor.execute("DELETE FROM usuarios WHERE id = %s", (user_id,))
        self.conn.commit()

    def activate_user(self, email):
        self.cursor.execute("UPDATE users SET active = TRUE WHERE email = %s", (email,))
        self.conn.commit()

    def update_password(self, email, new_password):
        self.cursor.execute("UPDATE users SET password = %s WHERE email = %s", (new_password, email))
        self.conn.commit()

    def row_to_dict(self, row):
        if not row:
            return None
        return {
            'id': row[0],
            'nombre': row[1],
            'username': row[2],
            'email': row[3],
            'telefono': row[4],
            'ciudad': row[5],
            'password': row[6],
            'token': row[7],
            'active': row[8]
        }
