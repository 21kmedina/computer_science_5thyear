#use flask to be our server and send/recive data from the web
from flask import Flask, render_template,url_for,request
app=Flask(__name__)

@app.route('/')
@app.route('/homepage')
def home_pg():
    return render_template('homepage.html')

@app.route('/survey')
def survey_pg():
    return render_template('survey_page.html')

@app.route('/results')
def results_pg():
    return render_template('results_page.html')
if __name__=="__main__":
    app.run()