# -*- encoding: utf-8 -*-

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

metadata = sa.MetaData()

EmojiLog = sa.Table(
	'emoji_log',
	metadata,
	sa.Column('id', sa.Integer, primary_key=True),
	sa.Column('text', sa.String(255), nullable=False),
	sa.Column('color', sa.CHAR(8), nullable=False),
	sa.Column('back_color', sa.CHAR(8), nullable=False),
	sa.Column('font', sa.String(255), nullable=False),
	sa.Column('size_fixed', sa.Boolean(), nullable=False),
	sa.Column('align', sa.String(255), nullable=False),
	sa.Column('stretch', sa.Boolean(), nullable=False),
	sa.Column('public_fg', sa.Boolean(), nullable=False),
	sa.Column('generated_at', sa.DateTime(), nullable=False),
	sa.Column('created_at', sa.DateTime(), nullable=False),
	sa.Column('updated_at', sa.TIMESTAMP(), nullable=False)
)



if __name__ == '__main__':
    pass
