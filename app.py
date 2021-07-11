from flask import (
    Flask, render_template
)

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("status_line.html")