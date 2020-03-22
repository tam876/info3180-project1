"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.models import UserProfile
from app.forms import SignUpForm
from werkzeug.utils import secure_filename
import os, datetime

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


@app.route('/profile', methods=["GET", "POST"])
def profile():
    form=SignUpForm()
    if request.method == "POST" and form.validate_on_submit():
            fname=form.fname.data
            lname=form.lname.data
            gender=form.gender.data
            email=form.email.data
            location=form.location.data
            biography=form.biography.data
            ppicture=form.ppicture.data
            filename = secure_filename(ppicture.filename)
            ppicture.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            joinpro= datetime.datetime.now()
            user= UserProfile(fname, lname, gender,email, location, biography, filename, joinpro)
            db.session.add(user)
            db.session.commit()
            flash("Profile successfully created", category="success")
            return redirect(url_for('profiles'))
    flash_errors(form)
    return render_template("profile.html", form=form)

@app.route('/profile/<userid>')
def user_pro(userid):
    userpro= UserProfile.query.get(userid)
    return render_template("user_profile.html", profile= userpro)
    

@app.route('/profiles')
def profiles():
    users= db.session.query(UserProfile).all()
    return render_template("profiles.html", profiles= users )

###
# The functions below should be applicable to all Flask apps.
###
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash("Error in the %s field - %s" % (
                getattr(form,field).label.text,
                error
            ),'danger')

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
