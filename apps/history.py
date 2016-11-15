# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy import CHAR, TIMESTAMP
from sqlalchemy.orm             import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime

from . import config

engine = create_engine(
        'mysql+pymysql://root:@localhost/emoji',
        encoding='utf-8',
        echo=config.debug
        )

Session = sessionmaker(bind=engine, autocommit=False)
Base    = declarative_base()

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

def logging(
            text,
            color,
            back_color,
            font,
            public_fg=True,
            ):
    emoji_log = EmojiLog(text, color, back_color, font, public_fg)
    session   = Session()
    session.add(emoji_log)
    session.commit()


def search():
    session    = Session()
    emoji_logs = (session
        .query(EmojiLog)
        .filter(EmojiLog.public_fg == True)
        .order_by(EmojiLog.generated_at.desc())
        .limit(20)
        .all()
        )
    session.close()

    return emoji_logs



print(search())
