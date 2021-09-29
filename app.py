from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# App Routes for main pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# App Routes for portfolio pages
@app.route('/engineering')
def engineering():
    return render_template('portfolio-items/eng.html')

@app.route('/data')
def data():
    return render_template('portfolio-items/data.html')

@app.route('/software')
def software():
    return render_template('portfolio-items/software.html')

@app.route('/volunteering')
def volunteering():
    return render_template('portfolio-items/volunteer.html')