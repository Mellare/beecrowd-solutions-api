from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/beecrowd/<int:id>")
def solution(id):
    return render_template(f"{id}.html")

@app.errorhandler(404)
def notFound(error404):
    return render_template("404.html"), 404

@app.errorhandler(500)
def serverError(error500):
    return render_template("500.html"), 500