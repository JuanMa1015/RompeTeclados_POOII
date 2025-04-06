import psycopg2
import bcrypt
from config import Config

class UserModel:
    def __init__(self):
        self.conn = psycopg2.connect(Config.SQLALCHEMY_DATABASE_URI)
        self.cursor = self.conn.cursor()

    def create_user(self, nombre, username, email, telefono, ciudad, password, token, rol='usuario'):
        try:
            self.cursor.execute("""
                INSERT INTO users (nombre, username, email, telefono, ciudad, password, token, active, rol)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (nombre, username, email, telefono, ciudad, password, token, False, rol))
            self.conn.commit()
            
            return True
        
        except psycopg2.errors.UniqueViolation as e:
            self.conn.rollback()
            return str(e)

    #Verificar si el username o el correo existe 
    def email_exists(self, email):
        self.cursor.execute("SELECT 1 FROM users WHERE email = %s", (email,))
        return self.cursor.fetchone() is not None

    def username_exists(self, username):
        self.cursor.execute("SELECT 1 FROM users WHERE username = %s", (username,))
        return self.cursor.fetchone() is not None


    def get_user_by_email(self, email):
        self.cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        row = self.cursor.fetchone()
        return self.row_to_dict(row)

    def get_user_by_id(self, user_id):
        self.cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        row = self.cursor.fetchone()
        if row:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, row))
        return None
    
    def get_user_by_username(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        row = self.cursor.fetchone()
        return self.row_to_dict(row)


    def check_password(self, email, password):
        self.cursor.execute("SELECT password FROM users WHERE email = %s", (email,))
        row = self.cursor.fetchone()
        if row and bcrypt.checkpw(password.encode(), row[0].encode()):
            return True
        return False

    def delete_user(self, user_id):
        self.cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
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
            'active': row[8],
            'created_at': row[9],
            'rol': row[10]
        }
