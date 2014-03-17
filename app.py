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


app = Flask(__name__, template_folder='blocks')
app.config.from_object('config')
app.config.from_envvar('EXTRA_APP_SETTINGS', silent=True)
app.jinja_env.add_extension('jinja2.ext.with_')

mail = Mail()
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
                return render_template('contact/contact.html', success=True)

        elif request.method == 'GET':
            return render_template('contact/contact.html', form=form)
# Routes
app.add_url_rule(
    '/',
    view_func=RenderTemplateView.as_view(
        'home', template_name='home/home.html')
)
app.add_url_rule(
    '/products/',
    view_func=RenderTemplateView.as_view(
        'products', template_name='products/products.html')
)
app.add_url_rule(
    '/tourism/',
    view_func=RenderTemplateView.as_view(
        'tourism', template_name='tourism/tourism.html')
)
app.add_url_rule(
    '/winery/',
    view_func=RenderTemplateView.as_view(
        'winery', template_name='winery/winery.html')
)

app.add_url_rule(
    '/location/',
    view_func=RenderTemplateView.as_view(
        'location', template_name='location/location.html')
)

app.add_url_rule(
    '/about/',
    view_func=RenderTemplateView.as_view(
        'about', template_name='about/about.html')
)
app.add_url_rule('/contact/', view_func=Contact.as_view('contact'))
