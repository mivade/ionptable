# -*- coding: utf-8 -*-
"""File for generating the ion trapping periodic table pages."""

from flask import Flask
from flask.ext.frozen import Freezer
from blueprints import ionptable

app = Flask(__name__, static_folder='static', static_url_path='/ionptable/static')
app.config['ions'] = [
    'barium', 'beryllium', 'cadmium', 'calcium',
    'magnesium', 'mercury', 'radium', 'strontium',
    'thorium', 'ytterbium']
app.register_blueprint(ionptable.table, url_prefix='/ionptable')
freezer = Freezer(app)

@freezer.register_generator
def ion_generator():
    for ion in app.config['ions']:
        yield '/ionptable/{}/'.format(ion)

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        freezer.freeze()
    elif sys.argv[1] == 'run':
        app.run(debug=True)
    elif sys.argv[1] == 'test':
        freezer.run(debug=True)
    