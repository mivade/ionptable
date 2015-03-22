"""Flask application for rendering Ion Trapping Periodic Table pages."""

from flask import Flask, render_template

app = Flask('ionptable')

@app.route('/')
def index():
    """Index page."""
    return render_template('index.html', title="Ion Trapping Periodic Table")

@app.route('/<ion>/')
def entry(ion):
    """Page showing details for a particular ion."""
    return render_template('ion.html', ion=ion)

if __name__ == "__main__":
    app.run(debug=True)
    