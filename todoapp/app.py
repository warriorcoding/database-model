from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/postgres'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#加数据库数据的话，url内容也会更新
class Todo(db.Model):#所以如果这个todos table已经建好了的话，在这一步后也不会被抹掉, map table to python??
    __tablename__='todos'
    id = db.Column(db.Integer, primary_key=True)#create the table
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<TODO {self.id} {self.description}>'

db.create_all()

@app.route('/todos/create', methods=['POST'])#listen for user input data?
def create_todo():
    description = request.form.get('description', '')
    todo = Todo(description=description)#把读进来的数据存进去
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/')
def index():#route handler or controller?
    return render_template('index.html', data=Todo.query.all())
