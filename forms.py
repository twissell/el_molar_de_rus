from flask_wtf import Form, RecaptchaField
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError


class ContactForm(Form):
    name = TextField("Name", [validators.Required("Por favor escribe tu nombre.")])
    email = TextField("Email", [validators.Required("Por favor escribe tu email."), validators.Email("Por favor escribe un email valido")])
    subject = TextField("Subject", [validators.Required("Por favor escribe un asunto")])
    message = TextAreaField("Message", [validators.Required("Por favor escribe un mensaje.")])
    recaptcha = RecaptchaField()
    submit = SubmitField("Send")
