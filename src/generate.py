# -*- coding: utf-8 -*-
"""File for generating the ion trapping periodic table pages."""

from flask import Flask
from flask_frozen import Freezer
from blueprints import ionptable
import pandas as pd

app = Flask(__name__, static_folder='static', static_url_path='/ionptable/static')

# Read data files
ions = pd.read_csv("data/ions.csv")
isotopes = pd.read_csv("data/isotopes.csv", index_col=0)

# Ion pages to render
app.config['ions'] = ions.name.tolist()

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
