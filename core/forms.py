# -*- coding: utf-8 -*-
import wtforms
from wtforms_tornado import Form

from config import web


class SearchForm(Form):
    # TODO: Define form fields here
    class Meta:
        csrf = False
        csrf_secret = web.SECRET_KEY
        locales = ('en_GB', 'en')

    url = wtforms.TextField('url', [wtforms.validators.DataRequired()])


@property
def _arguments(self):
    return self.handler().request.arguments


def __iter__(self):
    return iter(self._arguments)


def __len__(self):
    return len(self._arguments)


def __contains__(self, name):
    # We use request.arguments because get_arguments always returns a
    # value regardless of the existence of the key.
    return (name in self._arguments)


def getlist(self, name):
    # get_arguments by default strips whitespace from the input data,
    # so we pass strip=False to stop that in case we need to validate
    # on whitespace.
    return self.handler().get_arguments(name, strip=False)


def __getitem__(self, name):
    return self.handler().get_argument(name)
