from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class CommentForm(FlaskForm):

    comment = TextAreaField('Add a comment', validators=[Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):

    title = StringField('Pitch title',validators=[Required()])
    pitch = TextAreaField('Add a Pitch', validators=[Required()]) 
    category = SelectField('Choose Pitch Category', choices = [('Interview','Interview'),('Sales','Sales'),('Promotion','Promotion'),('Pick Up Lines','Pick Up Line')],validators=[Required()])
    submit = SubmitField('Add')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')