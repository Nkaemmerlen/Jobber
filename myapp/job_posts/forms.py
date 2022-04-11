from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired

class JobPostForm(FlaskForm):
  title = StringField('Title', validators=[DataRequired()])
  company = StringField('Company', validators=[DataRequired()])
  pay = IntegerField('Pay')
  language = TextAreaField('Language')
  framework = TextAreaField('Framework')
  database = TextAreaField('Database')
  submit = SubmitField('Post')