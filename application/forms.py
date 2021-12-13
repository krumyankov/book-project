from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField, IntegerField
from wtforms.validators import DataRequired



class BooksList(FlaskForm):
    name = StringField('Book Name',validators=[DataRequired()])
    author = StringField('Author',validators=[DataRequired()])
    date_added = DateField('Date Added')
    status = StringField('Select status')
    date_target = DateField('To be read by date')
    suggested_by = StringField('Proposed by',validators=[DataRequired()])
    submit = SubmitField('Add Book')