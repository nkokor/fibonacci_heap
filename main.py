from classes.FibHeap import FibHeap
from classes.FibNode import FibNode

# test heap
heap = FibHeap()
key_values = [3, 18, 42, 12, 98, 46, 24, 15]
for i in range(0, len(key_values)):
  heap.fib_heap_insert(key_values[i])

heap.fib_heap_extract_min()
heap.fib_heap_extract_min()
heap.fib_heap_extract_min()

nodes = heap.get_all_nodes()
for node in nodes:
  node.print_node()