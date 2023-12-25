import unittest
from FibHeap import FibHeap
from FibNode import FibNode

class TestFibonacciHeap(unittest.TestCase):
  def setUp(self):
      self.fib_heap = FibHeap()

  # fib_heap_insert tests

  # inserting a single node to an empty heap
  def test_insert_single_node(self):
      self.fib_heap.fib_heap_insert(5)
      self.assertEqual(self.fib_heap.fib_heap_minimum().key, 5)

  # inserting multiple nodes
  def test_insert_multiple_nodes(self):
      self.fib_heap.fib_heap_insert(5)
      self.assertEqual(self.fib_heap.fib_heap_minimum().key, 5)
      self.fib_heap.fib_heap_insert(3)
      self.assertEqual(self.fib_heap.fib_heap_minimum().key, 3)
      self.fib_heap.fib_heap_insert(1)
      self.assertEqual(self.fib_heap.fib_heap_minimum().key, 1)

  # fib_heap_union tests

  # union of two non-empty heaps
  def test_heap_union(self):
     h1 = FibHeap()
     h1.fib_heap_insert(3)
     h1.fib_heap_insert(7)
     h1.fib_heap_insert(18)
     h1.fib_heap_insert(21)
     h1.fib_heap_insert(22)
     h2 = FibHeap()
     h2.fib_heap_insert(1)
     h2.fib_heap_insert(2)
     h2.fib_heap_insert(12)
     h2.fib_heap_insert(88)
     h = FibHeap.fib_heap_union(h1, h2)
     self.assertEqual(h.fib_heap_minimum().key, 1)

  # union of an empty and non-empty heap
  def test_heap_union_empty(self):
     h1 = FibHeap()
     h2 = FibHeap()
     h2.fib_heap_insert(1)
     h2.fib_heap_insert(2)
     h2.fib_heap_insert(12)
     h2.fib_heap_insert(88)
     h = FibHeap.fib_heap_union(h1, h2)
     self.assertEqual(h.fib_heap_minimum().key, 1)

  # fib_heap_extract_min tests

  # extracting minimum from an empty heap
  def test_extract_min_empty_heap(self):
      extracted_min = self.fib_heap.fib_heap_extract_min()
      self.assertIsNone(extracted_min)

  # extracting minimum from a single node heap
  def test_extract_min_single_node(self):
      self.fib_heap.fib_heap_insert(8)
      self.fib_heap.fib_heap_extract_min()
      self.assertEqual(self.fib_heap.fib_heap_minimum(), None)

  # fib_heap_decrease_key tests

  # decreasing key success
  def test_decrease_key(self):
      self.fib_heap.fib_heap_insert(10)
      self.fib_heap.fib_heap_decrease_key(10, 7)
      self.assertEqual(self.fib_heap.fib_heap_minimum().key, 7)

  # decreasing key with updating min
  def test_decrease_key_updating_min(self):
      self.fib_heap.fib_heap_insert(4)
      self.fib_heap.fib_heap_insert(3)
      self.fib_heap.fib_heap_insert(8)
      self.fib_heap.fib_heap_insert(2)
      self.fib_heap.fib_heap_insert(13)
      self.fib_heap.fib_heap_insert(27)
      self.assertEqual(self.fib_heap.fib_heap_minimum().key, 2)
      self.fib_heap.fib_heap_decrease_key(27, 1)
      self.assertEqual(self.fib_heap.fib_heap_minimum().key, 1)

  # decrease key failure
  def test_decrease_key_exception(self):
    self.fib_heap.fib_heap_insert(10)
    with self.assertRaises(ValueError) as context:
      self.fib_heap.fib_heap_decrease_key(10, 13)
    self.assertEqual(str(context.exception), "new key value is greater than or equal to current key")

  # fib_heap_delete tests

  # deleting node from heap
  def test_delete_node(self):
    self.fib_heap.fib_heap_insert(15)
    self.fib_heap.fib_heap_insert(20)
    self.assertEqual(self.fib_heap.fib_heap_minimum().key, 15)
    self.fib_heap.fib_heap_delete(15)
    self.assertEqual(self.fib_heap.fib_heap_minimum().key, 20)

  # deleting node leaving empty heap
  def test_delete_last_node(self):
    self.fib_heap.fib_heap_insert(3)
    self.assertEqual(self.fib_heap.fib_heap_minimum().key, 3)
    self.fib_heap.fib_heap_delete(3)
    self.assertEqual(self.fib_heap.fib_heap_minimum(), None)

  # deleting non-existant node
  def test_delete_non_existing_node(self):
    self.fib_heap.fib_heap_insert(4)
    self.fib_heap.fib_heap_insert(3)
    self.fib_heap.fib_heap_insert(8)
    self.fib_heap.fib_heap_insert(2)
    self.fib_heap.fib_heap_insert(13)
    self.fib_heap.fib_heap_insert(27)
    self.assertEqual(6, self.fib_heap.n)
    self.fib_heap.fib_heap_delete(33)
    self.assertEqual(6, self.fib_heap.n)

if __name__ == '__main__':
  unittest.main()