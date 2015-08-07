import numpy             as np
import matplotlib.pyplot as plt
import re

class PlotData:

  def __init__(self, points, dataseries):
    self.points = np.array(points)
    self.dataseries = np.array(dataseries)

  def save_to_file(self, filename, floatfmt='%.18e'):
    savearray = np.append(self.points.reshape(1,-1), self.dataseries, axis=0)
    head = '@rows'
    np.savetxt(filename, savearray, fmt=floatfmt, header=head)

  @staticmethod
  def load_from_file(filename):
    loadarray = np.loadtxt(filename)
    if re.search(r'@columns', open(filename).read()): loadarray = loadarray.transpose()
    return PlotData(loadarray[0], loadarray[1:])


class DataPlotter:

  def __init__(self, filename):
    pd = PlotData.load_from_file(filename)
    points = pd.points
    dataseries = pd.dataseries
    self.pd, self.points, self.dataseries = pd, points, dataseries

  def scale_x(self, scalar): self.points *= scalar

  def scale_y(self, scalar): self.dataseries *= scalar

  def plot_all(self, linestyle, **kwargs):
    for series in self.dataseries:
      plt.plot(self.points, series, linestyle, **kwargs)

