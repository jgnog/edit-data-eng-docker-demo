from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Database connection setup
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('POSTGRES_HOST'),
        database=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD')
    )
    return conn

# Route to fetch student data from PostgreSQL
@app.route('/api/students', methods=['GET'])
def get_students():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT name, email, creation_date FROM students')
    students = cur.fetchall()
    cur.close()
    conn.close()

    # Format the data into JSON response
    student_list = []
    for student in students:
        student_list.append({
            "name": student[0],
            "email": student[1],
            "creation_date": student[2].strftime('%Y-%m-%d %H:%M:%S')
        })
    return jsonify(student_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
