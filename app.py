from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

# Dummy data
students = [
    {"name": "John Doe", "email": "johndoe@example.com", "creation_date": str(datetime.now())},
    {"name": "Jane Smith", "email": "janesmith@example.com", "creation_date": str(datetime.now())},
    {"name": "Alice Johnson", "email": "alicejohnson@example.com", "creation_date": str(datetime.now())}
]

# Define the route
@app.route('/api/students', methods=['GET'])
def get_students():
    return jsonify(students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
