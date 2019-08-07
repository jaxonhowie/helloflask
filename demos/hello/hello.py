# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li
    :license: MIT, see LICENSE for more details.
"""
import click
from flask import Flask, url_for

app = Flask(__name__)

app.config['ADMIN_NAME'] = 'Jaxon'
app.config.update(
    TESTING=True,
    SECRTET_KEU=''
)


# the minimal Flask application
@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'


# bind multiple URL for one view function
@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1>Hello, Flask!</h1>'


# dynamic route, URL variable default
# @app.route(url_for('greet', name='jack'))
@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, %s!</h1>' % name


# @app.route(url_for('func', content='jack'))
@app.route('/say', defaults={'content': 'hi'})
@app.route('/say/<content>')
def func(content):
    return '<h1>I want to say %s to you!</h1>' % content


# custom flask cli command
@app.cli.command()
def hello():
    """Just say hello."""
    click.echo('Hello, Human!')
    click.echo('hello hello,no problem')


@app.cli.command()
def custom_cmd():
    """A custom command written by Jaxon Howie"""
    click.echo('This is a custom command')
