import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print(BASE_DIR)


class Config(object):
    def __init__(self, cdict):
        attrs = set(self.attrs)  # copy and "unfreeze"
        for k, v in cdict.items():
            attrs.remove(k)  # check if the key is allowed, mark it as present
            setattr(self, k, v)
        if len(attrs) != 0:
            raise KeyError('missing required config keys: %s' % attrs)


class WebConfig(Config):
    attrs = frozenset([
        'STATIC_PATH',
        'TEMPLATE_PATH',
        'SECRET_KEY',
        'DATABASE',
        'DEBUG',
        'XSRF_COOKIES'
    ])

__doc = json.load(open('config.json', 'r'))
web = WebConfig(__doc['PROD'])
