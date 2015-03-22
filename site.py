"""Flask application for rendering Ion Trapping Periodic Table pages."""

from flask import Flask, render_template, Markup, json
from markdown import markdown

TITLE = "Ion Trapping Periodic Table"
IMAGES = {
    'barium': 'img/BaLevels.png',
    'beryllium': 'img/BeLevels.png',
    'calcium': 'img/CaLevels.png',
    'cadmium': 'img/CdLevels.png',
    'mercury': 'img/HgLevels.png',
    'magnesium': 'img/MgLevels.png',
    'strontium': 'img/SrLevels.png'
}

with open('isotopes.json', 'r') as f:
    isotopes = json.load(f)

app = Flask('ionptable')
app.config['ions'] = [
    'barium', 'beryllium', 'cadmium', 'calcium',
    'magnesium', 'mercury', 'radium', 'strontium',
    'thorium', 'ytterbium'
]

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
        'index.html', title=TITLE, text=text)

@app.route('/<ion>/')
def entry(ion):
    """Page showing details for a particular ion."""
    if str(ion) in IMAGES:
        levels_file = IMAGES[ion]
    else:
        levels_file = None
    print(levels_file)
    return render_template(
        'ion.html', title=(ion.title() + ' - ' + TITLE),
        ion=ion, isotopes=isotopes[ion],
        levels_file=levels_file, levels_alt=ion)

if __name__ == "__main__":
    app.run(debug=True)
    