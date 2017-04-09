# -*- encoding: utf-8 -*-

import os
import hashlib

from flask import Flask
from flask_rq2 import RQ
from flask_sqlalchemy import SQLAlchemy

# -----------------------------------------------------------------------------
# Initialize Flask / RQ / SQLAlchemy

cwd = os.path.dirname(os.path.abspath(__file__))
static_folder = os.path.join(cwd, '../../static')
template_folder = os.path.join(cwd, '../../templates')

app = Flask(
        __name__,
        static_folder=static_folder,
        template_folder=template_folder
        )
app.config.from_object('emoji.config')

db = SQLAlchemy(app)
rq = RQ(app)

# -----------------------------------------------------------------------------
# Initialize template values

app.jinja_env.globals['debug'] = app.config['DEBUG']
app.jinja_env.globals['domain'] = app.config['SITE_DOMAIN']
app.jinja_env.globals['description'] = app.config['SITE_DESCRIPTION']
app.jinja_env.globals['history_enabled'] = app.config['HISTORY_ENABLED']

app.jinja_env.globals['js_min_checksum'] = \
    hashlib.md5(open(app.config['JS_MIN_PATH'], 'rb').read()).hexdigest()

# -----------------------------------------------------------------------------
# Initialize cache

from emoji.factory.cache import make_cache

cache = make_cache()

# -----------------------------------------------------------------------------
# Import routes

import emoji.routes.api.emoji
import emoji.routes.api.font
import emoji.routes.api.history
import emoji.routes.emoji
import emoji.routes.emoji_download
import emoji.routes.home
