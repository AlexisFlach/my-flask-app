from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='./templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
  __tablename__ = 'myratings'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(200))

  def __init__(self, name):
      self.name = name

@app.route('/')
def index():
  return render_template('home.html', title="My title from App")

@app.route('/submit', methods=['POST', 'GET'])
def submit():
  if request.method == 'GET':
    return render_template('form.html')
  if request.method == 'POST' :
    name = request.form['name']
    data = Student(name)
    db.session.add(data)
    db.session.commit()
    return render_template('home.html')

  
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')