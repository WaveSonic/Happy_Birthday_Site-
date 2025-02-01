from flask import Flask, render_template, request, redirect, url_for, session
from models import db, User
import uuid

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Налаштування бази даних
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clicker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Ініціалізація бази даних
with app.app_context():
    db.create_all()

# Головна сторінка
@app.route('/')
def index():
    device_id = session.get('device_id')
    user = User.query.filter_by(device_id=device_id).first() if device_id else None

    if user:
        return render_template('index.html', user=user)
    else:
        return redirect(url_for('register'))

# Сторінка реєстрації
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        device_id = str(uuid.uuid4())

        new_user = User(device_id=device_id, username=username)
        db.session.add(new_user)
        db.session.commit()

        session['device_id'] = device_id
        return redirect(url_for('index'))

    return render_template('register.html')

# Обробка кліку
@app.route('/click', methods=['POST'])
def click():
    device_id = session.get('device_id')
    user = User.query.filter_by(device_id=device_id).first()

    if user:
        user.clicks += 1
        db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
