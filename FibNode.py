class Node():
  def __init__(self, key):
    self.p = None

    # one of node's children 
    self.child = None

    # left sibling of node
    self.left = None
    # right sibling of node
    self.right = None

    # number of node's children
    self.degree = 0

    # node is marked when it loses a child after it became a child of another node
    self.marked = False
    self.key = key
    
