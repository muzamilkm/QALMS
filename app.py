from loginAndScrape.lmsLogin import lmsLogin
from loginAndScrape.qalamLoginScrape import qalamLogin
from loginAndScrape.lmsScrape import lmsScrape
import json
from txtData.attd_data import extractAttd
from flask import Flask, render_template, request, redirect, url_for, session    #render_template() looks for a template (HTML file) in the templates folder.
app = Flask(__name__)   #creates a flask object that will be run

app.secret_key = 'eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTY3MjE2MTYwMSwiaWF0IjoxNjcyMTYxNjAxfQ.uqmoow_iw48tGBIsBlcc_rWcqEVST_-k9r1yolp21Yw' #creates a secret key for the session



@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    login = 0
    session['logged_in'] = False
    if session['logged_in'] == True:
        return redirect(url_for('home'))
    if request.method == 'POST':
        username = request.form['username']
        qalampass = request.form['qalampass']
        lmspass = request.form['lmspass']
        session['username'] = username
        session['qalampass'] = qalampass
        session['lmspass'] = lmspass
            # Validate the form data
        if not all([username, qalampass, lmspass]):
            error = 'All fields are required'
            return render_template("login.html", error=error)          #we can pass the values to be shown in the login.html as parameters of render_template
        elif lmsLogin(username, lmspass) == "Login failed":
            error = 'Invalid LMS username or password. Please try again.'
            return render_template("login.html", error=error)          #we can pass the values to be shown in the login.html as parameters of render_template
        elif qalamLogin(username, qalampass) == "Login failed" :
            error = 'Invalid QALAM username or password. Please try again.'
            return render_template("login.html", error=error)          #we can pass the values to be shown in the login.html as parameters of render_template
        else:
            session['logged_in'] = True
            login += 1
            return redirect(url_for('home'))     #sends the login data to the home page, so we can properly login again
    return render_template("login.html", error=error)


@app.route('/', methods=['GET'])
def home():
    if session['logged_in'] == False:
        return redirect(url_for('login'))
    else:
        if login == 1:
            username = session.get('username', '')
            lmspass = session.get('lmspass', '')
            lmsScrape(username, lmspass)
        attdData = extractAttd()
        jsonAttd = json.loads(json.dumps(attdData))
        return render_template("home.html", data=jsonAttd)

@app.route('/about', methods=['GET'])
def about():
  return render_template('about.html')











#TO START SERVER ON LOCAL, USE python -m flask run