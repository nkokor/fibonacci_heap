class FibHeap():
  def __init__(self):
    self.n = 0
    self.min = None

  # asuming that x is already an initialized node with set key 
  def fib_heap_insert(self, x):
    x.degree = 0
    x.p = None
    x.child = None
    x.mark = False

    # if heap is empty x is the only root and heap minimum
    if self.min is None:
      self.root_list = [x]
      self.min = x

    # if heap is not empty x is inserted into root list
    else:
      min_left = self.min.left
      self.min.left = x
      x.right = self.min
      if min_left is not None:
        min_left.right = x
        x.left = min_left
      self.root_list.append(x)

      if x.key < self.min.key:
        self.min = x
    self.n = self.n + 1