import psycopg2
import bcrypt
from config import Config

class UserModel:

    def get_connection(self):
        conn = psycopg2.connect(Config.SQLALCHEMY_DATABASE_URI)
        return conn, conn.cursor()

    def create_user(self, nombre, username, email, telefono, ciudad, password, token, rol='usuario'):
        conn, cursor = self.get_connection()
        try:
            cursor.execute("""
                INSERT INTO users (nombre, username, email, telefono, ciudad, password, token, active, rol)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (nombre, username, email, telefono, ciudad, password, token, False, rol))
            conn.commit()
            return True
        except psycopg2.errors.UniqueViolation as e:
            conn.rollback()
            return str(e)
        finally:
            cursor.close()
            conn.close()

    def email_exists(self, email):
        conn, cursor = self.get_connection()
        cursor.execute("SELECT 1 FROM users WHERE email = %s", (email,))
        exists = cursor.fetchone() is not None
        cursor.close()
        conn.close()
        return exists

    def username_exists(self, username):
        conn, cursor = self.get_connection()
        cursor.execute("SELECT 1 FROM users WHERE username = %s", (username,))
        exists = cursor.fetchone() is not None
        cursor.close()
        conn.close()
        return exists

    def get_user_by_email(self, email):
        conn, cursor = self.get_connection()
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return self.row_to_dict(row)

    def get_user_by_id(self, user_id):
        conn, cursor = self.get_connection()
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        row = cursor.fetchone()
        if row:
            columns = [desc[0] for desc in cursor.description]
            result = dict(zip(columns, row))
        else:
            result = None
        cursor.close()
        conn.close()
        return result

    def get_user_by_username(self, username):
        conn, cursor = self.get_connection()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return self.row_to_dict(row)

    def check_password(self, email, password):
        conn, cursor = self.get_connection()
        cursor.execute("SELECT password FROM users WHERE email = %s", (email,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row and bcrypt.checkpw(password.encode(), row[0].encode()):
            return True
        return False

    def delete_user(self, user_id):
        conn, cursor = self.get_connection()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
        cursor.close()
        conn.close()

    def activate_user(self, email):
        conn, cursor = self.get_connection()
        cursor.execute("UPDATE users SET active = TRUE WHERE email = %s", (email,))
        conn.commit()
        cursor.close()
        conn.close()

    def update_password(self, email, new_password):
        conn, cursor = self.get_connection()
        cursor.execute("UPDATE users SET password = %s WHERE email = %s", (new_password, email))
        conn.commit()
        cursor.close()
        conn.close()

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
