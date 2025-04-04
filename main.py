from flask import Flask, render_template

app = Flask(__name__)

# Glavna stran
@app.route('/')
def home():
    return render_template('index.html')

# Stran s storitvami
@app.route('/services')
def services():
    return render_template('services.html')

# Galerija
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# Prijava
@app.route('/login')
def login():
    return render_template('login.html')

# Registracija
@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
