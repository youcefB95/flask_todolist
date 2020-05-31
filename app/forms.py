from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, HiddenField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.tables import Task


class AddTaskForm(FlaskForm):
    content = StringField('content', validators=[DataRequired()])
    category = StringField('category', validators=[DataRequired()])
    submit = SubmitField('Create')


class DeleteTaskForm(FlaskForm):
    id = StringField(validators=[DataRequired()])
    submit = SubmitField('Delete')


class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[DataRequired()])
    submit = SubmitField('Submit')
