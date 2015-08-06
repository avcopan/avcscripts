import numpy             as np
import matplotlib.pyplot as plt
import re

class PlotData:

  available_options = {'keylist':list, 'labels':dict, 'colors':dict}

  def __init__(self, points, dataseries, keylist):
    self.points = points
    self.dataseries = dataseries
    self.keylist = keylist

  
  

class DataPlotter:

  def __init__(self, filename, transpose=False):
    self.transpose = transpose
    self.parse_comment_lines(filename)
    contents = np.loadtxt(filename)
    if transpose: contents = contents.transpose()
    self.points     = contents[0]
    self.dataseries = contents[1:]

  def parse_comment_lines(self, filename):
    comments = ''.join(re.findall(r'#(.*)', open(filename).read()))
    if comments is '': return
    match = re.match(r'\s*(columns|rows)', comments)
    if match:
      self.transpose = 'columns' in match.groups()
      comments = match.re.sub('', comments)
    keys, lbls = [], []
    for item in comments.split('|'):
      key, lbl = item.split(':')
      keys.append(key.strip())
      lbls.append(lbl.strip())
    self.keys = keys
    self.labels = dict(zip(keys, lbls))

  def scale_x(self, scalar): self.points *= scalar

  def scale_y(self, scalar): self.dataseries *= scalar

  def plot_all(self, linestyle, **kwargs):
    for series in self.dataseries:
      plt.plot(self.points, series, linestyle, **kwargs)

