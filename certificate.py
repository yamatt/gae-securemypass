#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 This file is part of PROJECT NAME.

 PROJECT NAME is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 PROJECT NAME is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with PROJECT NAME.  If not, see <http://www.gnu.org/licenses/>.
"""
from google.appengine.ext import db
import Image
from os import path
from hashlib import md5
from StringIO import StringIO

class CertKey(db.Key):
    @staticmethod
    def generate_key_from_args(**kwargs):
        options = str(kwargs)
        options_hash = md5(kwargs).hexdigest()
        return options_hash
        
    @classmethod
    def from_options(cls, **kwargs):
        options_key = self.generate_key_from_args(**kwargs)
        return super(CertKey, cls).from_path("Certificate", options_key)
        

class Certificate(db.Model):
    email = db.IntegerProperty(required=True, choices=[0,1])
    hashing = db.IntegerProperty(required=True, choices=[0,1,2,3])
    salting = db.IntegerProperty(required=True, choices=[0,1,2])
    standard_certificate_image = db.BlobProperty(required=True)
    
    _cert_base_path = path.join("static", "img", "certificate")
    _cert_top_path = path.join(_cert_base_path, "cert-top.png")
    _cert_middle_path = path.join(_cert_base_path, "cert-middle.png")
    _cert_bottom_path = path.join(_cert_base_path, "cert-bottom.png")
    _cert_tick_path = path.join(_cert_base_path, "tick.png")
    _cert_ok_path = path.join(_cert_base_path, "ok.png")
    _cert_bad_path = path.join(_cert_base_path, "bad.png")
    
    _cert_width = 150
    _cert_top_height = 20
    _cert_middle_height = 1
    _cert_bottom_height = 11
    _cert_icon_margin = 10
    _cert_item_gap = 30
    _cert_text_margin = 38
    
    def __init__(self, **kwds):
        key = CertKey.generate_key_from_args(**kwargs)
        certificate_image = self._make_image(**kwargs)
        super(Certificate, self).__init__(key_name=key, standard_certificate_image=certificate_image, **kwargs)
    
    @staticmethod
    def _make_image(**kwargs):
        def calculate_height(**kwargs):
            item_count = len(kwargs)
            return self._cert_top_height + self._cert_bottom_height + (item_count * self._cert_item_gap)
            
        cert_height = calculate_height(**kwargs)
        new_cert_image = Image.new("RGBA", (self._cert_width, calculate_height(**kwargs)), (255,255,255,255))
        top_image = Image.open(self._cert_top_path)
        middle_image = Image.open(self._cert_middle_path)
        bottom_image = Image.open(self._cert_bottom_path)
        
        items_end_top = (cert_height-self._cert_bottom_height)
        new_cert_image.paste(top_image, (0,0))
        new_cert_image.paste(bottom_image, (0, items_end_top))
        
        #fill in the blanks
        for i in range(self._cert_top_height, items_end_top):
            new_cert_image.paste(middle_image, (0,i))
        
        icon_images = [Image.open(self._cert_tick_path), Image.open(self._cert_ok_path), Image.open(self._cert_bad_path)]
        
        count = 0
        for key, value in kwargs.items():
            top_position = self._cert_top_height + (count * self._cert_item_gap)
            new_cert_image.paste(icon_images[value], (self._cert_icon_margin, top_position))
            count += 1
            
        # pull out image in idiotic way
        s = StringIO()
        new_cert_image.save(s, format="PNG")
        return s.getvalue()

