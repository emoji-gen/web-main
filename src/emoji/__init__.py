# -*- encoding: utf-8 -*-

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

cwd = os.path.dirname(os.path.abspath(__file__))
static_folder = os.path.join(cwd, '../../static')
template_folder = os.path.join(cwd, '../../templates')

app = Flask(
        __name__,
        static_folder=static_folder,
        template_folder=template_folder
        )

app.config.from_object('emoji.config')
app.jinja_env.globals['debug'] = app.config['DEBUG']
# app.jinja_env.globals['domain']      = config.site_domain
# app.jinja_env.globals['description'] = config.site_description

db = SQLAlchemy(app)

# -----------------------------------------------------------------------------

import emoji.routes.api.font
import emoji.routes.emoji
import emoji.routes.home
