#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

FEED_DOMAIN = SITEURL
RELATIVE_URLS = False

ARTICLE_URL = 'posts/{lang}/{date:%Y}/{date:%b}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{lang}/{date:%Y}/{date:%b}/{date:%d}/{slug}.html'
ARTICLE_LANG_URL = ARTICLE_URL
ARTICLE_LANG_SAVE_AS = ARTICLE_SAVE_AS
PAGE_URL = 'pages/{lang}/{slug}.html'
PAGE_SAVE_AS = 'pages/{lang}/{slug}.html'
PAGE_LANG_URL = PAGE_URL
PAGE_LANG_SAVE_AS = PAGE_SAVE_AS
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'
AUTHOR_URL = 'author/{slug}.html'
AUTHOR_SAVE_AS = 'author/{slug}.html'
AUTHORS_SAVE_AS = 'meta/authors.html'
CATEGORIES_SAVE_AS = 'meta/categories.html'
TAGS_SAVE_AS = 'meta/tags.html'
INDEX_SAVE_AS = 'index.html'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

FEED_ALL_RSS = 'feeds/all.rss.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = "UA-138955998-1"
