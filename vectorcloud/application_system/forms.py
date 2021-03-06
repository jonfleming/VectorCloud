#!/usr/bin/env python3

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField,\
    MultipleFileField, BooleanField
from wtforms.validators import DataRequired


class UploadScript(FlaskForm):
    script_name = StringField('Name of SDK application',
                              validators=[DataRequired()])

    description = TextAreaField('Description')

    author = StringField('Author Name')

    website = StringField('Website')

    script = FileField('Set Main Python File',
                       validators=[FileAllowed(['py'])])

    script_helpers = MultipleFileField('Add Support Files',
                                       validators=[FileAllowed(['py'])])

    icon = FileField('Add Icon Image',
                     validators=[FileAllowed(['jpg', 'png'])])

    upload = SubmitField('Upload')

    update = SubmitField('Update')

    run_in_bkrd = BooleanField('Run in Background?')


class AppSettings(FlaskForm):
    variable = TextAreaField('Enter settings variables', validators=[DataRequired()])

    value = StringField('Value')

    save = SubmitField('Save')
