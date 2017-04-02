# -*- encoding: utf-8 -*-

from datetime import datetime

from emoji import db

class EmojiLog(db.Model):
    __tablename__ = 'emoji_log'

    id           = db.Column('id', db.Integer, primary_key=True)
    text         = db.Column('text', db.String(255), nullable=False)
    color        = db.Column('color', db.CHAR(8), nullable=False)
    back_color   = db.Column('back_color', db.CHAR(8), nullable=False)
    font         = db.Column('font', db.String(255), nullable=False)
    size_fixed   = db.Column('size_fixed', db.Boolean(), nullable=False)
    align        = db.Column('align', db.String(255), nullable=False)
    stretch      = db.Column('stretch', db.Boolean(), nullable=False)
    public_fg    = db.Column('public_fg', db.Boolean(), nullable=False)
    generated_at = db.Column('generated_at', db.DateTime(), nullable=False)
    created_at   = db.Column('created_at', db.DateTime(), nullable=False)
    updated_at   = db.Column('updated_at', db.TIMESTAMP(), nullable=False)

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

