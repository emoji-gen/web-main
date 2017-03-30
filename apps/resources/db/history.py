# -*- coding: utf-8 -*-

import json
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy import CHAR, TIMESTAMP
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import DeclarativeMeta

# from apps import config
from apps.resources.inflator import Inflator

Base = declarative_base()
inflator = Inflator()

# -----------------------------------------------------------------------------

class EmojiLog(Base):
    __tablename__ = 'emoji_log'

    id           = Column('id', Integer, primary_key=True)
    text         = Column('text', String(255), nullable=False)
    color        = Column('color', CHAR(8), nullable=False)
    back_color   = Column('back_color', CHAR(8), nullable=False)
    font         = Column('font', String(255), nullable=False)
    size_fixed   = Column('size_fixed', Boolean(), nullable=False)
    align        = Column('align', String(255), nullable=False)
    stretch      = Column('stretch', Boolean(), nullable=False)
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
            size_fixed=False,
            align='center',
            stretch=True,
            public_fg=True,
            generated_at=None
            ):
        self.text         = text
        self.color        = color
        self.back_color   = back_color
        self.font         = font
        self.size_fixed   = size_fixed
        self.align        = align
        self.stretch      = stretch
        self.public_fg    = public_fg
        self.generated_at = generated_at or datetime.now()
        self.updated_at   = datetime.now()
        self.created_at   = datetime.now()

# -----------------------------------------------------------------------------

def logging(
            text,
            color,
            back_color,
            font,
            size_fixed=False,
            align='center',
            stretch=True,
            public_fg=True,
            ):
    emoji_log = EmojiLog(
            text,
            color,
            back_color,
            font,
            size_fixed,
            align,
            stretch,
            public_fg
            )
    session   = make_session()
    session.add(emoji_log)
    session.commit()


def search(
        limit=10
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
