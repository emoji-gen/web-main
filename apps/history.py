# -*- coding: utf-8 -*-

import json
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy import CHAR, TIMESTAMP
from sqlalchemy.orm             import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import DeclarativeMeta

from . import config

Base = declarative_base()

# -----------------------------------------------------------------------------

class AlchemyEncoder(json.JSONEncoder):
    IGNORE_COLUMNS = [ 'created_at', 'updated_at' ]

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            fields   = {}
            columns  = [ x for x in dir(obj) if not x.startswith('_') and x != 'metadata' ]
            for column in columns:
                if column in self.IGNORE_COLUMNS:
                    continue
                data = obj.__getattribute__(column)

                if isinstance(data, datetime):
                    data = int(data.timestamp()) # epoch

                try:
                    json.dumps(data)
                    fields[column] = data
                except TypeError:
                    fields[column] = None
            return fields

        return json.JSONEncoder.default(self, obj)

# -----------------------------------------------------------------------------

class EmojiLog(Base):
    __tablename__ = 'emoji_log'

    id           = Column('id', Integer, primary_key=True)
    text         = Column('text', String(255), nullable=False)
    color        = Column('color', CHAR(8), nullable=False)
    back_color   = Column('back_color', CHAR(8), nullable=False)
    font         = Column('font', String(255), nullable=False)
    public_fg    = Column('public_fg', Boolean(), nullable=False)
    generated_at = Column('generated_at', DateTime(), nullable=False)
    created_at   = Column('created_at', DateTime(), nullable=False)
    updated_at   = Column('updated_at', TIMESTAMP(), nullable=False)

    def __init__(
            self,
            text,
            color,
            back_color,
            font,
            public_fg=True,
            generated_at=None
            ):
        self.text         = text
        self.color        = color
        self.back_color   = back_color
        self.font         = font
        self.public_fg    = public_fg
        self.generated_at = generated_at or datetime.now()
        self.created_at   = datetime.now()


# -----------------------------------------------------------------------------

engine = None
def get_engine():
    global engine

    if not engine:
        engine = create_engine(
                config.mysql_url,
                encoding='utf-8',
                echo=config.debug
                )
    return engine


session_factory = None
def make_session():
    global session_factory

    if not session_factory:
        session_factory = sessionmaker(bind=get_engine(), autocommit=False)
    return session_factory()


def logging(
            text,
            color,
            back_color,
            font,
            public_fg=True,
            ):
    emoji_log = EmojiLog(text, color, back_color, font, public_fg)
    session   = make_session()
    session.add(emoji_log)
    session.commit()


def search(
        limit=20
        ):
    session    = make_session()
    emoji_logs = (session
        .query(EmojiLog)
        .filter(EmojiLog.public_fg == True)
        .order_by(EmojiLog.generated_at.desc())
        .limit(limit)
        .all()
        )
    session.close()

    return emoji_logs
