"""Flask application for rendering Ion Trapping Periodic Table pages."""

from flask import Flask, render_template, Markup
from markdown import markdown

app = Flask('ionptable')

def from_markdown(filename):
    """Read a Markdown file and convert to HTML."""
    with open(filename, 'r') as f:
        text = f.read().decode('utf-8')
    return Markup(markdown(text, output_format='html5'))

@app.route('/')
def index():
    """Index page."""
    text = from_markdown('index.md')
    return render_template(
        'index.html', title="Ion Trapping Periodic Table", text=text)

@app.route('/<ion>/')
def entry(ion):
    """Page showing details for a particular ion."""
    return render_template('ion.html', ion=ion)

if __name__ == "__main__":
    app.run(debug=True)
    