from datetime import datetime

from flask import Flask, render_template, redirect, url_for 
from blog.forms import NieuwePostFormulier
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcdefghijklmnopqrstuvwxyz'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


# database model

class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  titel = db.Column(db.String(500), nullable=True)
  content = db.Column(db.Text, nullable=False)
  auteur = db.Column(db.String(500), nullable=False)
  datum = db.Column(db.DateTime, nullable=False)

  
# routes

@app.route('/')
def home():
  posts = Post.query.order_by(Post.datum.desc()).all()
  
  return render_template('home.html', posts=posts)

@app.route('/nieuwe-post/', methods=['GET', 'POST'])
def nieuwe_post():
  form = NieuwePostFormulier()

  if form.validate_on_submit():
    post = Post(titel=form.titel.data, content=form.content.data, auteur=form.auteur.data, 
                datum=datetime.now())
    db.session.add(post)
    db.session.commit()

    return redirect(url_for('home'))

  return render_template('nieuwe-post.html', form=form)