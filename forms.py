from flask_wtf import Form, RecaptchaField
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError


class ContactForm(Form):
    name = TextField("Nombre", [validators.Required("Por favor escribe tu nombre.")])
    email = TextField("Correo electr&oacutenico", [validators.Required("Por favor escribe tu email."), validators.Email("Por favor escribe un email valido")])
    subject = TextField("Asunto", [validators.Required("Por favor escribe un asunto")])
    message = TextAreaField("Mensaje", [validators.Required("Por favor escribe un mensaje.")])
    recaptcha = RecaptchaField([validators.Required("Por favor completa el captcha")])
    submit = SubmitField("Enviar")
