class Node():
  def __init__(self, key):
    self.p = None
    self.child = None
    self.left = None
    self.right = None
    self.degree = 0
    self.marked = False
    self.key = key
    
