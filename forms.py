from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf

class AddPetForm(FlaskForm):
    """The form for adding a new pet"""
    name = StringField("Pet Name", validators=[InputRequired(message="Name can't be blank")])
    species = StringField("Species", validators=[InputRequired(message="Species can't be blank"), AnyOf(values= ('cat', 'Cat', 'dog', 'Dog', 'porcupine', 'Porcupine'), message="Must be a cat, dog, or porcupine")])
    photo_url = StringField("Photo URL", validators=[URL(message="Invalid URL"), Optional()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30, message="That age is out of range")])
    notes = TextAreaField('Notes', validators=[Optional()])

class PetInfoForm(FlaskForm):
    """The form for editting a pet's info"""
    photo_url = StringField("Photo URL", validators=[
                            URL(message="Invalid URL"), Optional()])
    notes = TextAreaField('Notes', validators=[Optional()])
    available = BooleanField('Is Available:')
