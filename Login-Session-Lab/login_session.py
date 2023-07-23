from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/',methods = ['GET','POST'] ) # What methods are needed?
def home():
	quote = request.form["q"]
	autherquote = request.form["athrq"]
	autherage = request.form["athra"]
	try:
	  login_session["q"] = quote
	  login_session["athrq"] = autherquote
	  login_session["athra"] = autherage
	return render_template('home.html')


@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html',quote = "q", autherquote = "athrq",autherage = "athra") # What variables are needed?


@app.route('/thanks',methods = ['GET','POST'])
def thanks():
	try:
	  login_session["q"] = quote
	  login_session["athrq"] = autherquote
	  login_session["athra"] = autherage
	  return render_template('thanks.html')

	
	except:
		return render_template('/error.html')



	 
	


if __name__ == '__main__':
	app.run(debug=True)