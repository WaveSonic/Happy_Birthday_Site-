from flask import Flask, render_template, request, jsonify, session
from models import db, User
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clicker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret_key'

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    device_id = session.get('device_id')
    if not device_id:
        device_id = str(uuid.uuid4())
        session['device_id'] = device_id

    user = User.query.filter_by(device_id=device_id).first()
    if not user:
        user = User(device_id=device_id, username='Guest')
        db.session.add(user)
        db.session.commit()

    return render_template('index.html', user=user)

@app.route('/click', methods=['POST'])
def click():
    device_id = session.get('device_id')
    user = User.query.filter_by(device_id=device_id).first()
    if user:
        user.cookies += 1 * user.booster_modifier
        db.session.commit()
    return jsonify({'cookies': user.cookies})

if __name__ == '__main__':
    app.run(debug=True)
