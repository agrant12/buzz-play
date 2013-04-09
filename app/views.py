from flask import Blueprint, render_template, abort

from app import app

@app.route('/')
def index():
	return render_template("index.html",
		Title = "Home")

@app.route('/explore')
def explore():
	return render_template("explore.html",
		Title = "Explore")

@app.route('/radio')
def radio():
	return render_template("radio.html",
		Title = "Radio")