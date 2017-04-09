import json

from flask import (Flask, render_template, request, 
                   make_response, url_for, redirect)

app = Flask(__name__)
application = app

@app.route('/')
def index():
    # load json data
    with open("./data/steps.json", 'r') as j:
        step_data = json.load(j)

    return render_template(
        'index.html',
        step_data = step_data["activities-steps"]
    )

if __name__ == '__main__':
    # must set debug=False before public hosting
    app.run(debug=True, host='0.0.0.0', port=8000)

