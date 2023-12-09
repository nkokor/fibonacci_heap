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

  # asuming that x is already an initialized node with set key 
  def fib_heap_insert(self, x):
    x.degree = 0
    x.p = None
    x.child = None
    x.mark = False

    # if heap is empty x is the only root and heap minimum
    if self.min is None:
      self.root_list = x
      self.min = x

    # if heap is not empty x is inserted into root list
    # x is inserted as left sibling of heap minimum
    else:
      x.right = self.root_list
      x.left = self.root_list.left
      self.root_list.left.right = x
      self.root_list.left = x

      if self.min is None or x.key < self.min.key:
        self.min = x
    self.n = self.n + 1

  @staticmethod
  def fib_heap_union(h1, h2):
    h = FibHeap.make_fib_heap()

    # getting the last node in h1 root list
    h1_last = h1.root_list
    while h1_last.right is not None:
      h1_last = h1_last.right
    
    # getting the first node in h2 root list
    h2_first = h2.root_list
    while h2_first.left is not None:
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
