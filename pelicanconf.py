#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mike Nikandrovs'
SITENAME = 'Mike Projects'
SITEURL = ''
TIMEZONE = 'Europe/Dublin'
DEFAULT_LANG = 'English'

OUTPUT_PATH = '../output'
PATH = 'content'


THEME = 'theme'
BOOTSTRAP_THEME = 'flatly'
PYGMENTS_STYLE = 'monokai'

PLUGIN_PATHS = ['plugins/',]
PLUGINS = ['i18n_subsites',]
JINJA_ENVIRONMENT = {'extensions':['jinja2.ext.i18n'],}



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('OneFile', 'https://login.onefile.co.uk/Keychain'),
         ('SLH email', 'https://cas.slh.ie/OWA/auth/logon.aspx?replaceCurrent=1&url=https%3a%2f%2fcas.slh.ie%2fOWA%2f'),
         ('Yahoo email', 'https://mail.yahoo.com/d/folders/1?.intl=ie&.lang=en-IE&.partner=none&.src=fp'),
         ('UCD gmail', 'https://mail.google.com/mail/u/0/#inbox'),)

# Social widget
SOCIAL = (('Dummy link 1', '#'),
          ('Dummy link 2', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True