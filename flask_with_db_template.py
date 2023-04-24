from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, redirect, request

from sqlalchemy import desc
from sqlalchemy import select
from sqlalchemy.orm import Session as session

import random
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)


class User(db.Model):
  id = db.Column('student_id', db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  city = db.Column(db.String(50))
  address = db.Column(db.String(200))
  pin = db.Column(db.Integer)


names = ['Kacper', 'Daniel', 'Bartek', 'Denis', 'Damian']
cities = ['Gdansk', 'Wroclaw', 'Paris']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


@app.route('/add')
def add():
  try:
    db.create_all()
    for i in range(15):
      selected_name = random.choice(names)
      selected_city = random.choice(cities)
      selected_number = random.choice(numbers)

      user = User(name=f'{selected_name}',
                  city=f'{selected_city}',
                  address=f'{i}',
                  pin=selected_number + i)
      db.session.add(user)
      db.session.commit()

  except:
    print('created')

  return redirect(url_for('show'))


@app.route('/show')
def show():
  users = User.query.all()
  stmt = select(User).order_by(desc(User.pin))
  x = db.session.execute(stmt)
  for i in x:
    print(i)

  return render_template('users.html', users=users)


@app.route('/form', methods=['GET', 'POST'])
def form():

  if request.method == 'POST':
    pass
  return render_template('form.html')


@app.route('/')
def blank():
  return 'x'


app.run(host='0.0.0.0', port=8080)
