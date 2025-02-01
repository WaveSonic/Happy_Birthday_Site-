from flask import Flask, render_template, request, redirect, url_for, session
import uuid
from database import init_db
from models import get_user_by_device, add_user, increment_clicks

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Ініціалізація бази даних
init_db()

# Головна сторінка
@app.route('/')
def index():
    device_id = session.get('device_id')
    user = get_user_by_device(device_id) if device_id else None

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

        add_user(device_id, username)
        session['device_id'] = device_id

        return redirect(url_for('index'))

    return render_template('register.html')

# Обробка кліку
@app.route('/click', methods=['POST'])
def click():
    device_id = session.get('device_id')
    if device_id:
        increment_clicks(device_id)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
