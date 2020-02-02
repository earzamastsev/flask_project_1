from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/departure/<departure>')
def departure(departure):
    return render_template('departure.html', departure=departure)


@app.route('/tour/<id>/')
def tour(id):
    return render_template('tour.html', id=id)


app.run()
