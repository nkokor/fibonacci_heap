import math

class FibHeap():
  def __init__(self):
    self.n = 0
    self.min = None
    self.root_list = None

  @staticmethod
  def make_fib_heap():
    return FibHeap()
  
  def fib_heap_minimum(self):
    return self.min
  
  def add_to_root_list(self, x):
    if self.root_list is not None:
      x.right = self.root_list.right
      x.left = self.root_list
      self.root_list.right.left = x
      self.root_list.right = x
    else:
      self.root_list = x

  def remove_from_root_list(self, x):
    if x == self.root_list:
      self.root_list = x.right
    x.left.right = x.right
    x.right.left = x.left

  # asuming that x is already an initialized node with set key 
  def fib_heap_insert(self, x):
    x.left = x
    x.right = x
    
    # adding new node to root list
    self.add_to_root_list(x)

    # updating heap minimum if neccessary
    if self.min is None or x.key < self.min.key:
      self.min = x

    # updating number of nodes
    self.n = self.n + 1
    return x

  @staticmethod
  def fib_heap_union(h1, h2):
    h = FibHeap.make_fib_heap()

    # getting the last node in h1 root list
    h1_last = h1.root_list
    while h1_last.right != h1_last:
      h1_last = h1_last.right
    
    # getting the first node in h2 root list
    h2_first = h2.root_list
    while h2_first.left != h2_first:
      h2_first = h2_first.left

    # concatenation of two root lists
    h1_last.right = h2_first
    h2_first.left = h1_last

    # setting new heap root list
    h.root_list = h1.root_list

    # setting heap minimum
    h.min = h1.min
    if h1.min is None or (h2.min is not None and h2.min.key < h1.min.key):
      h.min = h2.min
    h.n = h1.n + h2.n
    return h
  
  # helper function used to iterate through a doubly linked list
  def iterate(self, x):
    current_node = x
    stop = x
    flag = False
    while True:
      if current_node == stop and flag is True:
        break
      elif current_node == stop:
        flag = True
      yield current_node
      current_node = current_node.right

  def add_to_child_list(x, y):
    # adding y as new child of x
    if x.child is not None:
      y.right = x.child.right
      y.left = x.child
      x.child.right.left = y
      x.child.right = y
    else:
      x.child = y
    
    # updating degree of x and setting parent of y to x
    x.degree = x.degree + 1
    y.p = x
  
  def fib_heap_link(self, y, x):
    # removing y from root list 
    self.remove_from_root_list(y)
    y.left = y
    y.right = y

    # making y child of x
    self.add_to_child_list(x, y)

    y.mark = False

  def consolidate(self):
    A = []
    D = int(math.log(self.n) + 2)
    for i in range(0, D):
      A.append(None)
    # combining all trees of same degree
    root_nodes = [w for w in self.iterate(self.root_list)]
    for w in range(0, len(root_nodes)):
      x = root_nodes[w]
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

    # setting new heap minimum
    for i in range(0, D):
      if A[i] is not None:
        if A[i].key < self.min.key:
          self.min = A[i]

  def fib_heap_extract_min(self):
    z = self.min
    if z is not None:
      # add each child of z to root list and set parent to None
      if z.child is not None:
        children = [c for c in self.iterate(z.child)]
        for i in range(0, len(children)):
          self.add_to_root_list(children[i])
          children[i].p = None

      # removing z from root list
      self.remove_from_root_list(z)

      # updating root list and minimum to None if the heap will become empty
      if z.right == z:
        self.min = None
        self.root_list = None

      else:
        self.min = z.right
        self.consolidate()

      # reduce node count
      self.n = self.n - 1
    return z
  
  def cut(self, x, y):

    # removing x from y child nodes
    if y.child == y.child.right:
      y.child = None
    elif y.child == x:
      y.child = x.right
      x.right.p = y
    # removing x from sibling list
    x.left.right = x.right
    x.right.left = x.left

    y.degree = y.degree - 1
    self.add_to_root_list(x)
    x.p = None
    x.mark = False

  def cascading_cut(self, y):
    z = y.p 
    if z is not None:
      if y.mark is False:
        y.mark = True
      else:
        self.cut(y, z)
        self.cascading_cut(z)

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

  def fib_heap_delete(self, x):
    self.fib_heap_decrease_key(x, float('-inf'))
    self.fib_heap_extract_min()
