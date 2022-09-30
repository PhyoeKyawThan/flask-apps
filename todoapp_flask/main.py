from crypt import methods
from lib2to3.pgen2.token import EQUAL
from operator import imod
from queue import Empty
from flask import Flask, render_template, request, url_for, redirect
from flask_pymongo import PyMongo


app = Flask(__name__)
db_connection = PyMongo(app, uri='mongodb://127.0.0.1:27017/todoapp')
db = db_connection.db

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method=='POST':
        todo = request.form['todotext']
        db.mytodos.insert_one({'mytasks': todo})
        return redirect(url_for('toDo'))
    else:
        mytasks = db.mytodos.find()
        return render_template('todos.html',tasks=mytasks)

@app.route('/todos')
def toDo():
    mytasks = db.mytodos.find()
    return redirect(url_for('index'))



@app.route('/delete/<tasks>')
def delete(tasks):
    mytasks = db.mytodos.find()
    task_ = {'mytasks': tasks}
    db.mytodos.delete_one(task_)
    return redirect(url_for('index'))

if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 4000
    app.run(HOST, PORT, debug=True)
