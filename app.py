import json

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello(name=None):
    with open('resume.json') as data_file:
        data = json.load(data_file)

    return render_template('resume.html', **data)

if __name__ == '__main__':
    app.run(debug=True)
