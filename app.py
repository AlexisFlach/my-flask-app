from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='./templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/lektiondb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Tech(db.Model):
  __tablename__ = 'ratings'
  id = db.Column(db.Integer, primary_key=True)
  user = db.Column(db.String(200))
  tool = db.Column(db.String(200))
  rating = db.Column(db.Integer)
  comments = db.Column(db.Text())

  def __init__(self, user, tool, rating, comments):
      self.user = user
      self.tool = tool
      self.rating = rating
      self.comments = comments

class User(db.Model):
  __tablename__ = 'ratings'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(200))
  tool = db.Column(db.String(200))
  rating = db.Column(db.Integer)
  comments = db.Column(db.Text())

  def __init__(self, user, tool, rating, comments):
      self.user = user
      self.tool = tool
      self.rating = rating
      self.comments = comments


@app.route('/')
def index():
  return render_template('home.html', title="My title from App")

@app.route('/submit', methods=['POST', 'GET'])
def submit():
  if request.method == 'GET':
    return render_template('form.html')
  if request.method == 'POST' :
    user = request.form['user']
    tool = request.form['tool']
    rating = request.form['rating']
    comments = request.form['comments']
    data = Tech(user, tool, rating, comments)
    db.session.add(data)
    db.session.commit()
    return render_template('home.html')

  
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')