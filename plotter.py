import numpy             as np
import matplotlib.pyplot as plt
from cycler import cycler
import re

class PlotData:

  def __init__(self, points, dataseries):
    self.points = np.array(points)
    self.dataseries = np.array(dataseries)

  @staticmethod
  def init_from_file(filename):
    loadarray = np.loadtxt(filename)
    if re.search(r'@columns', open(filename).read()): loadarray = loadarray.transpose()
    return PlotData(loadarray[0], loadarray[1:])

  def save_to_file(self, filename, floatfmt='%.18e'):
    savearray = np.append(self.points.reshape(1,-1), self.dataseries, axis=0)
    head = '@rows'
    np.savetxt(filename, savearray, fmt=floatfmt, header=head)

  def set_reference_series(self, index):
    reference_series = self.dataseries[index]
    self.dataseries  = np.delete(self.dataseries, index, axis=0) - reference_series

  def set_color_cycle(self, color_cycle, label_cycle=None):
    if label_cycle is None:
      plt.rc('axes', prop_cycle=(cycler('color', color_cycle)))
    else:
      plt.rc('axes', prop_cycle=(cycler('color', color_cycle) + cycler('label', label_cycle)))

  def scale_x(self, scalar): self.points *= scalar

  def scale_y(self, scalar): self.dataseries *= scalar

  def plot_all(self, linestyle, **kwargs):
    for series in self.dataseries:
      plt.plot(self.points, series, linestyle, **kwargs)

  def set_aspect_by_adjusting_width(self, aspect_ratio):
    fig = plt.gcf()
    width, height = fig.get_size_inches()
    adjusted_width = height * aspect_ratio
    fig.set_size_inches([adjusted_width, height])

