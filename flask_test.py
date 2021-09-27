from flask import Flask, render_template
from markupsafe import escape
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
