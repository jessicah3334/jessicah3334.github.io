from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/cv')
def cv():
    return render_template('cv.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')