from FibNode import FibNode
import math, sys

class FibHeap:
  def __init__(self):
    self.min = None
    self.root_list = None
    self.n = 0
    FibHeap.node_id = 0

  # helper methods
    
  # adds node to root list
  def add_to_root_list(self, node):
    if self.root_list is None:
      self.root_list = node
    else:
      node.right = self.root_list
      node.left = self.root_list.left
      self.root_list.left.right = node
      self.root_list.left = node

  # removes node from root list
  def remove_from_root_list(self, node):
    if node == self.root_list:
      self.root_list = node.right
    node.left.right = node.right
    node.right.left = node.left

  # sets y as child of x
  def add_to_child_list(self, x, y):
    if x.child is None:
      x.child = y
    else:
      y.right = x.child.right
      y.left = x.child
      x.child.right.left = y
      x.child.right = y

  # removes y from x's children
  def remove_from_child_list(self, x, y):
    if x.child == x.child.right:
      x.child = None
    elif x.child == y:
      x.child = y.right
      y.right.parent = x
    y.left.right = y.right
    y.right.left = y.left
    
  # creates an empty heap
  @staticmethod
  def make_fib_heap():
    empty_heap = FibHeap()
    return empty_heap
  
  # returns minimum node
  def fib_heap_minimum(self):
    if self.min is not None:
        return self.min
    return None
  
  # returns list of nodes in a circular doubly linked list
  def get_nodes_from_doubly_linked_list(self, start_node):
    nodes = []
    current_node = start_node
    if current_node is not None:
        while True:
            nodes.append(current_node)
            current_node = current_node.right
            if current_node == start_node:
                break
    return nodes

  # return all nodes of subtree with given root
  def get_tree(self, root):
    nodes = []
    if root is None:
      return nodes
    nodes.append(root)
    child = root.child
    while child is not None:
      nodes.extend(self.get_tree(child))
      child = child.right
      if child is not None and child.id == root.child.id:
        break
    return nodes
  
  # returns list of all nodes in heap
  def get_all_nodes(self):
    nodes = []
    current = self.min
    if current is None:
      return nodes
    while True:
      nodes.extend(self.get_tree(current))
      current = current.right
      if current is not None and current.id == self.min.id:
        break
    return nodes

  # finds node with given key
  def find_node(self, key):
    for node in self.get_all_nodes():
      if node.key == key:
        return node
    return None
    
  # main methods

  # inserts new node with given key into heap
  def fib_heap_insert(self, key):
    new_node = FibNode(key)
    FibHeap.node_id = FibHeap.node_id + 1
    id = FibHeap.node_id
    new_node.id = id
    new_node.left = new_node
    new_node.right = new_node
    self.add_to_root_list(new_node)
    if self.min is None or (new_node.key < self.min.key):
      self.min = new_node
    self.n = self.n + 1
    return new_node
  
  # concatenation of two heaps into new heap
  @staticmethod
  def fib_heap_union(h1, h2):
    h = FibHeap.make_fib_heap()
    h.min = h1.min
    h.root_list = h1.root_list
    if h.root_list is None:
      h.root_list = h2.root_list
    elif h2.root_list is None:
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
  
  # extracts minimum node from heap
  def fib_heap_extract_min(self):
    z = self.min
    if z is not None:
        if z.child is not None:
            children = self.get_nodes_from_doubly_linked_list(z.child)
            for child in children:
                self.add_to_root_list(child)
                child.parent = None
        self.remove_from_root_list(z)
        if z == z.right:
            self.min = None
            self.root_list = None
        else:
            self.min = z.right
            self.consolidate()
        self.n = self.n - 1
    return z
  
  # concatenation of trees of same degree
  def consolidate(self):
    if self.root_list is not None:
        D = int(math.log(self.n, 2)) + 1
        A = [None] * D
        root_nodes = self.get_nodes_from_doubly_linked_list(self.root_list)
        for node in root_nodes:
            x = node
            d = x.degree
            while A[d] is not None:
                y = A[d]
                if x.key > y.key:
                    tmp = x
                    x = y
                    y = tmp
                self.fib_heap_link(y, x)
                A[d] = None
                d += 1
            A[d] = x
        for i in range(len(A)):
            if A[i] is not None:
                if A[i].key < self.min.key:
                   self.min = A[i]

  # adds y to tree x
  def fib_heap_link(self, y, x):
    self.remove_from_root_list(y)
    y.left = y
    y.right = y
    self.add_to_child_list(x, y)
    x.degree = x.degree + 1
    y.parent = x
    y.marked = False
  
  # decreases key of node with given value to new key value
  def fib_heap_decrease_key(self, key, new_key):
    node = self.find_node(key)
    if node is not None:
      if new_key >= key:
        raise ValueError("new key value is greater than or equal to current key")
      node.key = new_key
      y = node.parent
      if y is not None and node.key < y.key:
        self.cut(node, y)
        self.cascading_cut(y)
      if node.key < self.min.key:
        self.min = node
    return node
  
  def cut(self, x, y):
    self.remove_from_child_list(y, x)
    y.degree = y.degree - 1
    self.add_to_root_list(x)
    x.parent = None
    x.marked = False
  
  def cascading_cut(self, y):
    z = y.parent
    if z is not None:
      if y.marked is False:
        y.marked = True
      else:
        self.cut(y, z)
        self.cascading_cut(z)
  
  # removes node with given key from heap
  def fib_heap_delete(self, key):
    node = self.fib_heap_decrease_key(key, -sys.maxsize)
    if node is not None:
      self.fib_heap_extract_min()
      return node