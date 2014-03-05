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
from flask import Flask, render_template
from flask.views import View


app = Flask(__name__, template_folder='blocks')
app.jinja_env.add_extension('jinja2.ext.with_')


class RenderTemplateView(View):

    def __init__(self, template_name):
        self.template_name = template_name

    def dispatch_request(self):
        return render_template(self.template_name)


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
