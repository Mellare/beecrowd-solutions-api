from flask import Flask, render_template

app = Flask(__name__)

@app.route("/beecrowd/<int:id>")
def solution(id):
    return render_template(f"{id}.html")