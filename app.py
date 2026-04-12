from flask import Flask, render_template
app = Flask(__name__)


@app.route('/home')
def hello_world():
    return render_template('index.html')


@app.route('/health')
def health_check():
    return "server health is good and is up and running"


app.run(port=80)
