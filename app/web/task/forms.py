from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError, DataRequired, EqualTo

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, Field, widgets
from wtforms.validators import DataRequired, ValidationError, DataRequired, EqualTo

class CommandForm(FlaskForm):
    command = StringField('Команда:', validators=[DataRequired()] , render_kw = {'autocomplete':"off"})
    submit = SubmitField('Отправить')
    #command()