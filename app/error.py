from app import app, db
from flask import render_template

@app.errorhandler(404)
def not_found_error(error):
	return render_template('404.html'), 404
	
@app.errorhandler(500)
def ibternal_error(error):
	db.session.rollback() #otkat seansa bazy dannyh
	return render_template('500.html'), 500
