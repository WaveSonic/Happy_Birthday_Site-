from database import get_db_connection

# Отримання користувача за device_id
def get_user_by_device(device_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE device_id = ?', (device_id,)).fetchone()
    conn.close()
    return user

# Додавання нового користувача
def add_user(device_id, username):
    conn = get_db_connection()
    conn.execute('INSERT INTO users (device_id, username) VALUES (?, ?)', (device_id, username))
    conn.commit()
    conn.close()

# Оновлення кількості кліків
def increment_clicks(device_id):
    conn = get_db_connection()
    conn.execute('UPDATE users SET clicks = clicks + 1 WHERE device_id = ?', (device_id,))
    conn.commit()
    conn.close()
