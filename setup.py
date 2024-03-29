#!/usr/bin/env python
from setuptools import find_packages, setup

from djangocms_education import __version__


REQUIREMENTS = [
    'django-cms>=3.11',
    'djangocms-text-ckeditor>=5.1.4',
    'python-dateutil>=2.8.2',
]

setup(
    name='djangocms-education',
    version=__version__,
    author='Simon Krull',
    author_email='simonkrull@mailbox.org',
    maintainer='Simon Krull',
    maintainer_email='simonkrull@mailbox.org',
    url='https://github.com/crydotsnake/djangocms-education',
    license='BSD-3-Clause',
    description='Adds a Plugin for embedding your Resume to your website.',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
)
