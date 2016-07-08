# -*- coding: utf-8 -*-
"""Project models module.

All Project models will be defined within this module
"""

from google.appengine.ext import db


class WordModel(db.Model):
    """A single blog entry."""
    id = db.StringProperty(required=True)
    text = db.StringProperty(required=True)
    count = db.TextProperty(required=True)
    date_created = db.DateTimeProperty(auto_now_add=True)
    date_updated = db.DateTimeProperty(auto_now=True)

    def __str__(self):
        pass
