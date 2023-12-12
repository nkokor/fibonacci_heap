import math

class FibHeap():

  def __init__(self):
    self.n = 0
    self.min = None
    self.root_list = None

  # helper methods

  # adds node to root list
  def add_to_root_list(self, node):
    if self.root_list is not None:
      node.right = self.root_list.right
      node.left = self.root_list
      self.root_list.right.left = node
      self.root_list.right = node
    else:
      self.root_list = node

  # removes node from root list
  def remove_from_root_list(self, node):
    if node == self.root_list and node.right == node:
      self.root_list = None
    else:
      if node == self.root_list:
        self.root_list = node.right
      node.left.right = node.right
      node.right.left = node.left

  # sets new child of parent
  def add_to_child_list(parent, child):
    # adding child as new child of parent
    if parent.child is not None:
      child.right = parent.child.right
      child.left = parent.child
      parent.child.right.left = child
      parent.child.right = child
    else:
      parent.child = child
    # updating degree of parent and setting parent of child to parent
    parent.degree = parent.degree + 1
    child.p = parent

  # removes child from parent
  def remove_from_child_list(parent, child):
    # removing child from parent's child list
    if parent.child == parent.child.right:
      parent.child = None
    elif parent.child == child:
      parent.child = child.right
      child.right.p = parent
    child.left.right = child.right
    child.right.left = child.left
    child.p = None
    parent.degree = parent.degree - 1

  # creates an empty heap
  @staticmethod
  def make_fib_heap():
    return FibHeap()
  
  # returns minimum node of heap
  def fib_heap_minimum(self):
    return self.min
  
  # main methods
  
  # inserts pre-initialized node into heap
  def fib_heap_insert(self, node):
    node.degree = 0
    node.p = None
    node.child = None
    node.mark = False
    # adding new node to root list
    self.add_to_root_list(node)
    # updating heap minimum if neccessary
    if self.min is None or node.key < self.min.key:
      self.min = node
    # updating number of nodes
    self.n = self.n + 1

  # combines two heaps into brand new heap
  # NOT FINISHED
  @staticmethod
  def fib_heap_union(h1, h2):
    h = FibHeap.make_fib_heap()
    h.min = h1.min
    h.root_list = h1.root_list
    # concatenation of h2 and h root lists
    if h.root_list == None:
      h.root_list = h2.root_list
    elif h2.root_list == None:
      h.root_list = h1.root_list
    else:
      last_node_h = h.root_list.left
      last_node_h2 = h2.root_list.left
      last_node_h.right = h2.root_list
      h2.root_list.left = last_node_h
      last_node_h2.right = h.root_list
      h.root_list.left = last_node_h2
    if h1.min is None or (h2.min is not None and h2.min.key < h1.min.key):
      h.min = h2.min
    h.n = h1.n + h2.n 
    return h
  
  # extracts minimum node from heap, returns extracted node
  def fib_heap_extract_min(self):
    z = self.min
    if z is not None:
      # adding each child of z to root list and set parent to None
      if z.child is not None:
        current_child = z.child
        while True:
          next_child = current_child.right
          self.add_to_root_list(current_child)
          current_child.p = None
          if next_child == z.child:
            break
          current_child = next_child
      # removing z from root list
      self.remove_from_root_list(z)
      # updating root list and minimum to None if the heap will become empty
      if z.right == z:
        self.min = None
      else:
        self.min = z.right
        self.consolidate()
      # reduce node count
      self.n = self.n - 1
    return z
  
  # combines trees of the same degree
  # NOT FINISHED
  def consolidate(self):
    A = []
    D = int(math.log(self.n, 2))
    for i in range(0, D):
      A.append(None)
    # combining all trees of same degree
    w = self.root_list
    while True:
      x = w
      d = x.degree
      while A[d] is not None:
        y = A[d]
        if x.key > y.key:
          tmp = x
          x = y
          y = tmp
        self.fib_heap_link(y, x)
        A[d] = None
        d = d + 1
      A[d] = x
      if w.right == self.root_list:
        break
      w = w.right
    # setting new heap minimum
    self.min = None
    for i in range(0, D):
      if A[i] is not None:
        if self.min is None:
          self.root_list = A[i]
          self.min = A[i]
        else:
          self.add_to_root_list(A[i])
          if A[i].key < self.min.key:
            self.min = A[i]

  # inserts tree with root y into tree with root x
  def fib_heap_link(self, y, x):
    # removing y from root list 
    self.remove_from_root_list(y)
    # making y child of x
    self.add_to_child_list(x, y)
    y.mark = False

  # decreases value of key of the given node to the new given value
  def fib_heap_decrease_key(self, x, k):
    if k > x.key:
      raise ValueError("New key value is greater than current key value!")
    x.key = k
    y = x.p 
    if y is not None and x.key < y.key:
      self.cut(x, y)
      self.cascading_cut(y)
    if x.key < self.min.key:
      self.min = x
  
  # removes child from parent tree and adds it to the root list
  def cut(self, child, parent):
    # removing child from child list of parent
    self.remove_from_child_list(parent, child)
    self.add_to_root_list(child)
    child.mark = False

  # performs cut operation until unmarked parent node is reached
  def cascading_cut(self, y):
    z = y.p 
    if z is not None:
      if y.mark is False:
        y.mark = True
      else:
        self.cut(y, z)
        self.cascading_cut(z)

  # removes given node from heap
  def fib_heap_delete(self, x):
    self.fib_heap_decrease_key(x, float('-inf'))
    self.fib_heap_extract_min()
