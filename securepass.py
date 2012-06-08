#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       untitled.py
#       
#       Copyright 2012 Matt Copperwaite <copperwaitem01@01webpc930>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       
#       


from webapp2 import RequestHandler, WSGIApplication
import jinja2
from os import path
from forms import CertificateForm

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(path.join(path.dirname(__file__), "templates")))

class FrontPage(RequestHandler):
    def get(self):
        form = CertificateForm()
        template = jinja_environment.get_template('form.tmp.html')
        self.response.out.write(template.render({"form": form}))
        
class FaqPage(RequestHandler):
    def get(self):
        template = jinja_environment.get_template('faq.tmp.html')
        self.response.out.write(template.render())
        
class AboutPage(RequestHandler):
    def get(self):
        template = jinja_environment.get_template('about.tmp.html')
        self.response.out.write(template.render())
        
class CertPage(RequestHandler):
    def get(self):
        results = CertificateForm(self.request.params)
        if results.validate():
            template = jinja_environment.get_template('cert.tmp.html')
            self.response.out.write(template.render())
        else:
            self.response.redirect("/")

app = WSGIApplication([
        ('/', FrontPage),
        ('/faq', FaqPage),
        ('/about', AboutPage),
        ('/certificate', CertPage)
    ],
    debug=True
)
