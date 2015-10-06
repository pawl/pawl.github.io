import json

from flask import Flask, render_template

app = Flask(__name__)


def get_resume_json():
    with open('resume.json') as data_file:
        return json.load(data_file)


@app.route('/')
def resume():
    template_data = get_resume_json()
    return render_template('resume.html', **template_data)


@app.route('/resume_no_border.html')
def resume_no_border():
    template_data = get_resume_json()
    return render_template('resume_no_border.html', **template_data)


if __name__ == '__main__':
    app.run(debug=True)
