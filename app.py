from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Cambia esto por una clave más segura en producción.

# Simulación de base de datos de usuarios
usuarios = {
    'Beymar': 'contraseña1',
    'Luis': 'contraseña2'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in usuarios and usuarios[username] == password:
        session['username'] = username
        return redirect(url_for('bienvenido'))
    else:
        flash('Nombre de usuario o contraseña incorrectos.')
        return redirect(url_for('index'))

@app.route('/bienvenido')
def bienvenido():
    if 'username' in session:
        return render_template('bienvenido.html', username=session['username'])
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
