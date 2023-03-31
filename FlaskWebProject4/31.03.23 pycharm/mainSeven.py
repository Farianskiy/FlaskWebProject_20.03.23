from flask import Flask, request, render_template
from jinja2 import Template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('indexSeven.html')

if __name__ == "__main__":
    app.run(debug=True)




