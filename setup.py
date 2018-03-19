# Big app example: https://github.com/Robpol86/Flask-Large-Application-Example

from setuptools import setup

setup(
    name='FlaskProject',
    packages=['app'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)