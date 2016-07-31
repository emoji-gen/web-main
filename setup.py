"""
Ultimate Slack Emoji Generator
"""

from setuptools import setup, find_packages
from codecs     import open
from os         import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='emoji-web',
    version='1.0.0',
    description='Ultimate Slack Emoji Generator',
    long_description=long_description,
    url='https://github.com/pine/Emoji-Web.git',
    license='MIT',
)

