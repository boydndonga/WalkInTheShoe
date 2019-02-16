from flask import render_template, request, redirect, url_for, abort
from . import main
from .. import db
from flask_login import login_required

@main.route('/')
def index():
    return '<h1> Hello World </h1>'
