from flask
import Flask, request, render_template
import sqlite3
import bcrypt

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('form_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT,
            age INTEGER,
            email TEXT,
            fundamental_completed TEXT,
            high_school_completed TEXT,
            skin_color TEXT,
            gender TEXT,
            preferred_course TEXT,
            terms_agreed TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    full_name = request.form.get('full_name')
    age = request.form.get('age')
    email = request.form.get('email')
    fundamental_completed = request.form.get('fundamental_completed')
    high_school_completed = request.form.get('high_school_completed')
    skin_color = request.form.get('skin_color')
    gender = request.form.get('gender')
    preferred_course = request.form.get('preferred_course')
    terms_agreed = request.form.get('terms_agreed')

    # Insert into database
    conn = sqlite3.connect('form_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO user_data (
            full_name, age, email, fundamental_completed, 
            high_school_completed, skin_color, gender, 
            preferred_course, terms_agreed
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        full_name, age, email, fundamental_completed, 
        high_school_completed, skin_color, gender, 
        preferred_course, terms_agreed
    ))
    conn.commit()
    conn.close()

    return "Form submitted successfully!"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)