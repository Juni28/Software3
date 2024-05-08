from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Esto se usa para manejar sesiones y cookies.

# Datos de prueba para validar inicio de sesión
usuarios = {
    "usuario1": "psw",
    "usuario2": "password2"
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in usuarios and usuarios[username] == password:
            session['logged_in'] = True
            session['username'] = username
            flash('Inicio de sesión exitoso!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Usuario o contraseña incorrectos.', 'error')

    return render_template('login.html')


@app.route('/home')
def home():
    if 'logged_in' in session and session['logged_in']:
        return render_template('home.html', username=session['username'])
    else:
        flash('Necesitas iniciar sesión primero.', 'error')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    flash('Sesión cerrada.', 'info')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
