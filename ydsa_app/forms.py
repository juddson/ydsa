from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Email, Length

class JoinForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=120)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=255)])
    wants_newsletter = BooleanField("Add me to the newsletter for upcoming events")
    # Honeypot (anti-bot): leave empty in UI
    website = HiddenField()  # bots often fill everything
    submit = SubmitField("Join")
