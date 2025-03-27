from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def run_website():
    app.run(host='0.0.0.0', port=8180)

run_website()