import unittest
from FibHeap import FibHeap
from FibNode import FibNode

class TestFobonacciHeap(unittest.TestCase):
  def setUp(self):
      self.fib_heap = FibHeap()

  # inserting a single node to an empty heap
  def test_insert_single_node(self):
      node = FibNode(5)
      self.fib_heap.fib_heap_insert(node)
      self.assertEqual(self.fib_heap.fib_heap_minimum().key, 5)

  # inserting multiple nodes
  def test_insert_single_node(self):
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

if __name__ == '__main__':
  unittest.main()