from flask import Flask,render_template,request 
from flask_bootstrap import Bootstrap
import videoTester

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def inde():
    return render_template("index.html")

@app.route('/expression') 
def expression():
    p= videoTester.exp()
    return render_template("face.html",data=p)


@app.route('/face') 
def face():
    return render_template("face.html",data = "Anxiety and Depression Detection")