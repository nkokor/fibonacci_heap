class FibNode:
  def __init__(self, key):
      self.key = key
      self.parent = None
      self.child = None
      self.left = None
      self.right = None
      self.degree = 0
      self.marked = False
      id = None
  
  def __lt__(self, other):
      return self.key < other.key
  
  # prints out information on node
  def print_node(self):
    key = self.key
    parent = None
    if self.parent is not None:
      parent = self.parent.key
    left = None
    if self.left is not None:
      left = self.left.key
    right = None
    if self.right is not None:
      right = self.right.key
    degree = self.degree
    print("key: " + str(key) + " parent: " + str(parent) + " left sibling: " + str(left) + " right sibling: " + str(right) + " degree: " + str(degree) + '\n')
   