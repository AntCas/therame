from flask import (Flask, render_template, request, 
                   make_response, url_for, redirect)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html' 
    )

# must set debug=False before public hosting
app.run(debug=True, host='0.0.0.0', port=8000)

