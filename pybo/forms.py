from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,PasswordField, EmailField
from wtforms.validators import DataRequired,Length, EqualTo, Email


class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목은 필수입력 항목입니다.')])
    content = StringField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])
    price = StringField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])


class AnswerForm(FlaskForm):
    content = TextAreaField('답변 내용', validators=[DataRequired('답변 내용은 필수입력 항목입니다.')])
