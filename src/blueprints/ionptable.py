# -*- coding: utf-8 -*-
"""Flask blueprint for rendering Ion Trapping Periodic Table pages."""

import codecs
from flask import Blueprint, render_template, Markup, json
from markdown import markdown

TITLE = "Ion Trapping Periodic Table"

with codecs.open('groups.json', 'r', 'utf-8') as f:
    LINKS = json.load(f)
with open('data.json', 'r') as f:
    data = json.load(f)
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
    if str(ion) not in ['thorium', 'ytterbium']:
        levels_file = 'img/{}.svg'.format(ion)
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
        ion=ion, data=data[ion],
        levels_file=levels_file, levels_alt=ion,
        groups=groups, links=links
    )
