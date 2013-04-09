from flask import Blueprint, render_template, abort

from app import app

@app.route('/')
def index():
	return 'Lets get Started!'