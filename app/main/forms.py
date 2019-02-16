from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required


class PostForm(FlaskForm):
    body = TextAreaField("What's on your mind?", validators=[Required()])
    submit = SubmitField('Submit')