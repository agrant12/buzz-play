from flask import Blueprint, render_template, redirect, flash, abort
from werkzeug import check_password_hash, generate_password_hash

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

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)