from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.tables import Task



class TaskForm(FlaskForm):
    content = StringField('content', validators=[DataRequired()])
    category = StringField('category', validators=[DataRequired()])
    submit = SubmitField('Create new task')

class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[DataRequired()])
    submit = SubmitField('Submit')