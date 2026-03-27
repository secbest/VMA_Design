from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('website/index.html')

@app.route('/portfolio')
def portfolio():
    return render_template('website/portfolio.html')

@app.route('/studio')
def studio():
    return render_template('website/studio.html')

@app.route('/contact')
def contact():
    return render_template('website/contact.html')

@app.route('/e-quote')
def e_quote():
    return render_template('e-quote/e-quote.html')

if __name__ == '__main__':
    app.run()