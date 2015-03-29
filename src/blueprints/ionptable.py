# -*- coding: utf-8 -*-
"""Flask blueprint for rendering Ion Trapping Periodic Table pages."""

import codecs
from flask import Blueprint, render_template, Markup, json
from markdown import markdown

TITLE = "Ion Trapping Periodic Table"
IMAGES = {
    'barium': 'img/BaLevels.svg',
    'beryllium': 'img/BeLevels.svg',
    'calcium': 'img/CaLevels.svg',
    'cadmium': 'img/CdLevels.svg',
    'mercury': 'img/HgLevels.svg',
    'magnesium': 'img/MgLevels.svg',
    'strontium': 'img/SrLevels.svg'
}
GROUPS = {
    'barium': [u'Düsseldorf', 'Innsbruck', 'Georgia Tech', 'Northwestern', 'Ulm', 'Washington'],
    'beryllium': [u'Düsseldorf', 'NIST'],
    'calcium': ['Aarhus', 'Basel', 'Berkeley', 'Innsbruck', 'Oxford'],
    'cadmium': ['Maryland'],
    'mercury': ['NIST'],
    'magnesium': ['Aarhus', 'MPQ', 'NIST'],
    'strontium': ['MIT', 'MIT Lincoln Lab', 'NIST', 'NPL', 'Paris', 'Innsbruck'],
    'thorium': ['Michigan'],
    'ytterbium': ['Duke', 'GTRI', 'Maryland']
}

with codecs.open('groups.json', 'r', 'utf-8') as f:
    LINKS = json.load(f)
with open('isotopes.json', 'r') as f:
    isotopes = json.load(f)
with open('static/img/ptable.svg', 'r') as f:
    # Don't include the first 3 lines which include stuff we don't
    # want/need to embed.
    svg = f.readlines()[3:]
    ptable_svg = Markup(''.join(svg))

def from_markdown(filename):
    """Read a Markdown file and convert to HTML."""
    with codecs.open(filename, 'r', 'utf-8') as f:
        text = f.read()
    return Markup(markdown(text, output_format='html5'))

table = Blueprint('ptable', __name__)

@table.route('/')
def index():
    """Index page."""
    text = from_markdown('index.md')
    return render_template(
        'index.html', title=TITLE, text=text, ptable_svg=ptable_svg)

@table.route('/<ion>/')
def entry(ion):
    """Page showing details for a particular ion."""
    if str(ion) in IMAGES:
        levels_file = IMAGES[ion]
    else:
        levels_file = None
    if ion in GROUPS:
        groups = GROUPS[ion]
        links = [LINKS[group] for group in groups]
    else:
        groups = ''
        links = ''
    print(levels_file)
    return render_template(
        'ion.html', title=(ion.title() + ' - ' + TITLE),
        ion=ion, data=isotopes[ion],
        levels_file=levels_file, levels_alt=ion,
        groups=groups, links=links
    )