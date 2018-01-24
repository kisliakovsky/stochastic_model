from pathlib import Path
from typing import Tuple
# noinspection PyPep8Naming
from datetime import time as Time

from matplotlib import pyplot
from matplotlib.dates import DateFormatter

from src.model import Model
from src.util import paths
import seaborn

RESULTS_DIR = Path("../results")
paths.create_dir(RESULTS_DIR)

COLORS = {
    -1: "#FFFFFF",
    0: "#96bf33",
    1: "#E2571E",
    2: "#FF7F00",
    3: "#4B0082",
    4: "#00FF00",
    5: "#FFFF00",
    6: "#0000FF",
    7: "#FF0000",
    8: "#8B00FF",
    9: "#000000"
}


def save_stacked_plot(x, y1, y2, title: str):
    figure, axes = pyplot.subplots()
    axes.set_title(title)
    axes.set_xlabel("day")
    axes.set_ylabel("number of infectious")
    axes.set_ylim((0, 110))
    axes.stackplot(x, y1, y2)
    path = Path(RESULTS_DIR, title).with_suffix(".png")
    path_str = str(path)
    pyplot.savefig(path_str)


def save_plot(x, y, title: str):
    figure, axes = pyplot.subplots()
    axes.set_title(title)
    axes.set_xlabel("day")
    axes.set_ylabel("number of immigrants")
    axes.set_ylim((0, 300))
    axes.plot(x, y)
    axes.grid()
    path = Path(RESULTS_DIR, title).with_suffix(".png")
    path_str = str(path)
    pyplot.savefig(path_str)


EXACT_X = [1979, 2000, 2011]
EXACT_Y = [30, 6141, 169]
ROUGH_X = [1980, 1983, 1990, 1993, 1999, 2001, 2003, 2009, 2010]
ROUGH_Y = [50, 160, 900, 2500, 5800, 5400, 4500, 700, 400]
CAPTURES_X = list(range(1979, 2012))
CAPTURES_Y = [0, 0, 0, 0, 60, 60, 60, 60, 60, 60, 60,
              60, 60, 60, 851, 827, 1144, 1314, 1628, 1356, 2282,
              3884, 3375, 2199, 2572, 2529, 2585, 2705, 779, 941, 601,
              311, 150]


def save_complex_model_plot(model1: Model, model2: Model, model3: Model):
    figure, axes = pyplot.subplots()
    axes.set_title(model1.get_name())
    axes.set_xlabel("year")
    axes.set_ylabel("number of individuals")
    # axes.set_ylim((0, 8000))
    axes.set_xlim((1975, 2015))
    x1, y1 = model1.run()
    x2, y2 = model2.run()
    x3, y3 = model3.run()
    axes.plot(x1 + x2, y1 + y2, '#0000ff', label='Proposed model')
    axes.plot(x3, y3, '#ff0000', label='Alternative model')
    axes.plot(CAPTURES_X, CAPTURES_Y, '#339933', label='Captures')
    axes.scatter(ROUGH_X, ROUGH_Y, 7, '#ff9900', label='Inexact population size')
    axes.scatter(EXACT_X, EXACT_Y, 7, '#00ff00', label='Exact population size')
    axes.grid()
    axes.legend()
    path = Path(RESULTS_DIR, model1.get_name()).with_suffix(".png")
    path_str = str(path)
    pyplot.savefig(path_str)


def save_comparison(model1: Model, model2: Model, title: str):
    models = model1, model2
    figure, axes_bunch = pyplot.subplots(1, 2, sharey="row")
    figure.suptitle(title)
    figure.set_figwidth(15)
    for i in range(2):
        axes = axes_bunch[i]
        model = models[i]
        _save_stacked_plot(model, axes)
    path = Path(RESULTS_DIR, "hiv_spread").with_suffix(".png")
    path_str = str(path)
    pyplot.savefig(path_str)


def _save_stacked_plot(model, axes):
    axes.set_title(model.get_name())
    axes.set_xlabel("day")
    axes.set_ylabel("number of infected")
    axes.set_ylim((0, model.get_population_size()))
    x, y1, y2 = model.run()
    axes.stackplot(x, y1, y2)
