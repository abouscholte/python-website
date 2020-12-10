from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class NieuwePostFormulier(FlaskForm):
  titel = StringField('Voeg een titel toe aan je post')
  content = TextAreaField('Voeg content toe aan je post', validators=[DataRequired()])
  auteur = StringField('Vul je naam in', validators=[DataRequired()])
  submit = SubmitField('Voeg toe')