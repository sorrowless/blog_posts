#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.curdir)
from sensitive_settings import *

#SITEURL = ''
SITEURL = 'https://blog.sbog.ru'

PATH = 'content'
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images']

OUTPUT_PATH = 'output/'

# Base settings
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'common'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS_WIDGET_NAME = "_"
#LINKS = (('All categories', 'meta/categories.html'),)

# Social widget
#SOCIAL_WIDGET_NAME
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)
HIDE_SIDEBAR = True

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Themes
THEME_STATIC_DIR = 'theme'
THEME = 'pelican-themes/pelican-bootstrap3/'
# Bootstrap3 theme-related setting
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
BANNER = 'images/banner.jpg'
BANNER_SUBTITLE = 'Yet another DevOps blog'
FAVICON = 'images/favicon.ico'

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ['i18n_subsites', "optimize_images"]
