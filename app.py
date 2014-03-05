#!/usr/bin/env python

"""
Project documentation.
"""

__author__ = "twissell"
__copyright__ = "Copyright 2013, The project-name Project"
__credits__ = ["twissell"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "twissell"
__email__ = "twissel.development@gmail.com"
__status__ = "Prototype"

# import builtins
# import third-party
from flask import Flask, render_template, request, flash
from flask.views import View
from forms import ContactForm
from flask.ext.mail import Message, Mail


mail = Mail()
app = Flask(__name__, template_folder='blocks')
app.jinja_env.add_extension('jinja2.ext.with_')
app.secret_key = 'ronin'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'jackosinapsis@gmail.com'
app.config["MAIL_PASSWORD"] = '5260DaVinci5260'

mail.init_app(app)


class RenderTemplateView(View):

    def __init__(self, template_name):
        self.template_name = template_name

    def dispatch_request(self):
        return render_template(self.template_name)


class Contact(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        form = ContactForm()

        if request.method == 'POST':
            if form.validate() is False:
                flash('Todos los campos requeridos.')
                return render_template('contact/contact.html', form=form)
            else:
		msg = Message(form.subject.data,
			      sender=(form.name.data, form.email.data),
			      recipients=["jackosinapsis@gmail.com"])
		msg.html = """
		<b>De:</b> %s <i>%s</i>
		<h4><b>Mensaje:</b></h4>
		<p>%s</p>
		""" % (form.name.data, form.email.data, form.message.data)
		msg.body = """
		De: %s <%s>
		Mensaje:
		%s
		""" % (form.name.data, form.email.data, form.message.data)
		mail.send(msg)    
                return 'Form posted.'

        elif request.method == 'GET':
            return render_template('contact/contact.html', form=form)
# Routes
app.add_url_rule(
    '/',
    view_func=RenderTemplateView.as_view(
        'home', template_name='home/home.html')
)
app.add_url_rule(
    '/tourism',
    view_func=RenderTemplateView.as_view(
        'tourism', template_name='tourism/tourism.html')
)
app.add_url_rule('/contact/', view_func=Contact.as_view('contact'))
