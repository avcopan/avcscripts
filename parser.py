import re
import numpy as np

class ParseFile:
  def __init__(self, path):
    self.filecontents = open(path).read()

  def findfloats(self, matchstring):
    return np.array([float(match) for match in re.findall(matchstring, self.filecontents)])

