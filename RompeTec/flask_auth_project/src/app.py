from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mail import Mail, Message
from config import Config
from models.ModelUsuario import UserModel
from itsdangerous import URLSafeTimedSerializer
import bcrypt
from functools import wraps
import re

app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)
user_model = UserModel()
s = URLSafeTimedSerializer(app.config['SECRET_KEY'])


#Control de sesiones por roles
def login_required(rol=None):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                flash('Inicia sesión para continuar', 'warning')
                return redirect(url_for('login'))  # Ajusta a tu ruta de login
            if rol and session.get('rol') != rol:
                flash('No tienes permiso para acceder a esta página', 'error')
                return redirect(url_for('unauthorized'))  # Puedes crear esta ruta
            return f(*args, **kwargs)
        return decorated_function
    return wrapper

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        username = request.form['username']
        email = request.form['email']
        telefono = request.form['telefono']
        ciudad = request.form['ciudad']
        plain_password = request.form['password']

        # Validar email
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            flash('Correo inválido', 'error')
            return redirect(url_for('register'))

        # Validar contraseña
        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$'
        if not re.match(password_regex, plain_password):
            flash('La contraseña debe tener al menos 8 caracteres, incluyendo una mayúscula, una minúscula, un número y un carácter especial.', 'error')
            return redirect(url_for('register'))

        # Validar teléfono
        if not re.match(r'^\d{10}$', telefono):
            flash('El teléfono debe tener exactamente 10 dígitos', 'error')
            return redirect(url_for('register'))
        
        # Validar si ya existe el correo o el usuario
        if user_model.get_user_by_email(email):
            flash("Este correo ya está registrado.", "error")
            return redirect(url_for('register'))

        if user_model.get_user_by_username(username):
            flash("Este nombre de usuario ya existe.", "error")
            return redirect(url_for('register'))

        # Solo después de validar todo, generas el hash
        password = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())
        token = s.dumps(email, salt='email-confirm')
        confirm_url = url_for('confirm_email', token=token, _external=True)

        user_model.create_user(nombre, username, email, telefono, ciudad, password.decode(), token)

        if user_model:
            msg = Message('Confirma tu cuenta', recipients=[email], body=f'Confirma tu cuenta: {confirm_url}')
            msg.html = render_template('emails/confirmation.html', user = nombre, confirm_url= confirm_url)
            mail.send(msg)
            flash('Correo de confirmación enviado.', 'success')
            return redirect(url_for('login'))
        else:
            if "users_email_key" in user_model:
                flash("Este correo ya esta registrado.", "error")
            elif "users_username_key" in user_model:
                flash("Este nombre de usuario ya existe.", "error")
            else:
                flash("Error al registrar usuario.", "error")
        
    return render_template('register.html')


@app.route('/confirm/<token>')
def confirm_email(token):
    try:
        email = s.loads(token, salt='email-confirm', max_age=3600)
        user_model.activate_user(email)
        flash('Cuenta activada. Inicia sesión.', 'success')
    except:
        flash('El enlace expiró o no es válido.', 'error')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = user_model.get_user_by_email(email)
        if user and user['active'] and bcrypt.checkpw(password.encode(), user['password'].encode()):
            session.permanent = True  # Esto activa el tiempo de expiración
            session['user_id'] = user['id']
            session['rol'] = user['rol']
            flash('Bienvenido!', 'success')
            return redirect(url_for('dashboard'))
        flash('Credenciales inválidas o cuenta no activada.', 'error')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Sesión cerrada', 'success')
    return redirect(url_for('login'))


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required(rol='usuario')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = user_model.get_user_by_id(session['user_id'])

    if request.method == 'POST':
        # Cambio de contraseña
        if 'current_password' in request.form:
            current = request.form['current_password']
            new = request.form['new_password']
            confirm = request.form['confirm_password']

            if new != confirm:
                flash('Las contraseñas no coinciden', 'error')
            else:
                if user_model.check_password(user['email'], current):
                    hashed = bcrypt.hashpw(new.encode(), bcrypt.gensalt()).decode()
                    user_model.update_password(user['email'], hashed)
                    flash('Contraseña actualizada correctamente', 'success')
                else:
                    flash('Contraseña actual incorrecta', 'danger')

        # Eliminación de cuenta
        if 'confirm_password' in request.form and 'current_password' not in request.form:
            user_model.delete_user(user['id'])
            session.clear()
            flash('Cuenta eliminada exitosamente', 'success')
            return redirect(url_for('register'))

    return render_template('dashboard.html', user=user, navbar = True)


@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    if request.method == 'POST':
        email = request.form['email']
        user = user_model.get_user_by_email(email)
        if user:
            token = s.dumps(email, salt='recover-password')
            url = url_for('reset_password', token=token, _external=True)
            msg = Message('Recupera tu contraseña', recipients=[email], body=f'Reestablece tu contraseña: {url}')
            msg.html = render_template('emails/forgot.html', user = user['username'], recover_url = url)
            mail.send(msg)
            flash('Revisa tu correo para restablecer la contraseña.', 'success')
        else:
            flash('Correo no registrado.', 'error')
    return render_template('forgot.html')

@app.route('/reset/<token>', methods=['GET', 'POST'])
def reset_password(token):
    try:
        email = s.loads(token, salt='recover-password', max_age=3600)
    except:
        flash('Token inválido o expirado.', 'error')
        return redirect(url_for('login'))
    if request.method == 'POST':
        password = bcrypt.hashpw(request.form['password'].encode(), bcrypt.gensalt())
        user_model.update_password(email, password.decode())
        flash('Contraseña actualizada. Inicia sesión.', 'success')
        return redirect(url_for('login'))
    return render_template('reset.html')

if __name__ == '__main__':
    app.run(debug=True)