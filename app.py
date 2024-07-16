from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123454321",
    database="tododb"
)

cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/todos', methods=['GET'])
def get_todos():
    cursor.execute("SELECT id, task FROM todos")
    todos = cursor.fetchall()
    return jsonify([{'id': todo[0], 'task': todo[1]} for todo in todos])

@app.route('/add_todo', methods=['POST'])
def add_todo():
    new_task = request.json['task']
    cursor.execute("INSERT INTO todos (task) VALUES (%s)", (new_task,))
    db.commit()
    return '', 201

@app.route('/delete_todo/<int:id>', methods=['DELETE'])
def delete_todo(id):
    cursor.execute("DELETE FROM todos WHERE id = %s", (id,))
    db.commit()
    return '', 204

@app.route('/update_todo/<int:id>', methods=['PUT'])
def update_todo(id):
    updated_task = request.json['task']
    cursor.execute("UPDATE todos SET task = %s WHERE id = %s", (updated_task, id))
    db.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
