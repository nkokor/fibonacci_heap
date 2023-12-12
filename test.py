import unittest
from FibHeap import FibHeap
from FibNode import FibNode

class TestFibonacciHeap(unittest.TestCase):
  def setUp(self):
      self.fib_heap = FibHeap()

  # inserting a single node to an empty heap
  def test_insert_single_node(self):
      node = FibNode(5)
      self.fib_heap.fib_heap_insert(node)
      self.assertEqual(self.fib_heap.fib_heap_minimum().key, 5)

  # inserting multiple nodes
  def test_insert_multiple_nodes(self):
      node1 = FibNode(5)
      self.fib_heap.fib_heap_insert(node1)
      self.assertEqual(self.fib_heap.fib_heap_minimum().key, 5)
      node2 = FibNode(3)
      self.fib_heap.fib_heap_insert(node2)
      self.assertEqual(self.fib_heap.fib_heap_minimum().key, 3)
      node3 = FibNode(1)
      self.fib_heap.fib_heap_insert(node3)
      self.assertEqual(self.fib_heap.fib_heap_minimum().key, 1)

  # extracting minimum from an empty heap
  def test_extract_min_empty_heap(self):
      extracted_min = self.fib_heap.fib_heap_extract_min()
      self.assertIsNone(extracted_min)

  # extracting minimum from a single node heap
  def test_extract_min_single_node(self):
      node = FibNode(8)
      self.fib_heap.fib_heap_insert(node)
      extracted_min = self.fib_heap.fib_heap_extract_min()
      self.assertEqual(extracted_min.key, 8)
      self.assertIsNone(self.fib_heap.fib_heap_minimum())

  # decreasing key success
  def test_decrease_key(self):
      node = FibNode(10)
      self.fib_heap.fib_heap_insert(node)
      self.fib_heap.fib_heap_decrease_key(node, 7)
      self.assertEqual(self.fib_heap.fib_heap_minimum().key, 7)

  # decreasing key with updating min
  def test_decrease_key_updating_min(self):
      node1 = FibNode(4)
      node2 = FibNode(3)
      node3 = FibNode(8)
      node4 = FibNode(2)
      node5 = FibNode(13)
      node6 = FibNode(27)
      self.fib_heap.fib_heap_insert(node1)
      self.fib_heap.fib_heap_insert(node2)
      self.fib_heap.fib_heap_insert(node3)
      self.fib_heap.fib_heap_insert(node4)
      self.fib_heap.fib_heap_insert(node5)
      self.fib_heap.fib_heap_insert(node6)
      self.assertEqual(self.fib_heap.fib_heap_minimum().key, 2)
      self.fib_heap.fib_heap_decrease_key(node6, 1)
      self.assertEqual(self.fib_heap.fib_heap_minimum().key, 1)

  # decrease key failure
  def test_decrease_key_exception(self):
    node = FibNode(10)
    self.fib_heap.fib_heap_insert(node)
    with self.assertRaises(ValueError) as context:
      self.fib_heap.fib_heap_decrease_key(node, 13)
    self.assertEqual(str(context.exception), "New key value is greater than current key value!")

  # deleting node from heap
  def test_delete_node(self):
    node_to_delete = FibNode(15)
    node_to_stay = FibNode(20)
    self.fib_heap.fib_heap_insert(node_to_delete)
    self.fib_heap.fib_heap_insert(node_to_stay)
    self.assertEqual(self.fib_heap.fib_heap_minimum().key, 15)
    self.fib_heap.fib_heap_delete(node_to_delete)
    self.assertEqual(self.fib_heap.fib_heap_minimum().key, 20)

  # deleting node leaving empty heap
  def test_delete_last_node(self):
    node_to_delete = FibNode(3)
    self.fib_heap.fib_heap_insert(node_to_delete)
    self.assertEqual(self.fib_heap.fib_heap_minimum().key, 3)
    self.fib_heap.fib_heap_delete(node_to_delete)
    self.assertEqual(self.fib_heap.fib_heap_minimum(), None)

  
  # heap union
  def test_heap_union(self):
     h1 = FibHeap()
     node1 = FibNode(3)
     node2 = FibNode(7)
     node3 = FibNode(18)
     node4 = FibNode(21)
     node5 = FibNode(22)
     h1.fib_heap_insert(node1)
     h1.fib_heap_insert(node2)
     h1.fib_heap_insert(node3)
     h1.fib_heap_insert(node4)
     h1.fib_heap_insert(node5)
     h2 = FibHeap()
     node6 = FibNode(1)
     node7 = FibNode(2)
     node9 = FibNode(12)
     node10 = FibNode(88)
     h2.fib_heap_insert(node6)
     h2.fib_heap_insert(node7)
     h2.fib_heap_insert(node9)
     h2.fib_heap_insert(node10)
     h = FibHeap.fib_heap_union(h1, h2)
     self.assertEqual(h.fib_heap_minimum(), node6)

if __name__ == '__main__':
  unittest.main()