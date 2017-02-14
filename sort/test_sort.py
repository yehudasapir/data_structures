import merge_sort as ms
class TestMergeSort:
	def test_sort_arr(self):
		assert ms.sort_arr([4,3,2,1,5,6,7,9,10,8]) == [1,2,3,4,5,6,7,8,9,10]

	def test_merge_sort_arrs(self):
		assert ms.merge_sort_arrs([1,3,5,7,9],[2,4,6,8,10,11,12]) == [1,2,3,4,5,6,7,8,9,10,11,12]

import binary_tree as bt
class TestBinaryTree:
	def test_node_add_small_node(self):
		node = bt.Node(2)
		new_node = bt.Node(1)
		node.add_child(new_node)
		assert node.left_child == new_node

	def test_node_add_big_node(self):
		node = bt.Node(2)
		new_node = bt.Node(3)
		node.add_child(new_node)
		assert node.right_child == new_node

	def test_bt_insert(self):
		my_arr  = [2,5,7]
		my_tree = bt.BinaryTree()
		for i in range(len(my_arr)):
			my_tree.insert(my_arr[i])
		assert my_tree.head.node_value == 2
		assert my_tree.depth == 3

	def test_bt_sort(self):
		my_arr  = [2,5,7,19,13,20,15,22,4]
		my_tree = bt.BinaryTree()
		for i in range(len(my_arr)):
			my_tree.insert(my_arr[i])
		assert my_tree.traverse_dfs_tree(my_tree.head) == [2,4,5,7,13,15,19,20,22]

import heap
class TestHeap:
	def test_add_min(self):
		hp = heap.Heap()
		hp.add(heap.HeapNode(value = 5))
		assert hp.heap_arr[1]==5
		hp.add(heap.HeapNode(value = 9))
		assert hp.heap_arr[2]==9
		hp.add(heap.HeapNode(value = 3))
		assert hp.heap_arr[1]==3

	def test_add_max(self):
		hp = heap.Heap(is_min=False)
		hp.add(heap.HeapNode(value=5))
		assert hp.heap_arr[1]==5
		hp.add(heap.HeapNode(value=9))
		assert hp.heap_arr[1]==9
		hp.add(heap.HeapNode(value=3))
		assert hp.heap_arr[3]==3

	def test_delete_max(self):
		hp = heap.Heap(is_min=False)
		hp.add(heap.HeapNode(value=5))
		hp.add(heap.HeapNode(value=9))
		hp.add(heap.HeapNode(value=3))
		hp.delete(10)
		hp.delete(1)
		assert hp.heap_arr[1]==5
		hp.delete(heap.HeapNode(value=5))
		assert hp.heap_arr[1]==3

	def test_delete_min(self):
		hp = heap.Heap(is_min=True)
		hp.add(heap.HeapNode(value=5))
		hp.add(heap.HeapNode(value=9))
		hp.add(heap.HeapNode(value=3))
		hp.delete(10)
		hp.delete(1)
		assert hp.heap_arr[1]==5
		hp.delete(heap.HeapNode(value=5))
		assert hp.heap_arr[1]==9	



	#def test_delete_min(self):	


# heap = Heap()
# heap.add(HeapNode(value = 5))
# heap.add(HeapNode(value = 9))
# heap.add(HeapNode(value = 3))
# heap.add(HeapNode(value = 7))
# heap.add(HeapNode(value = 11))
# heap.add(HeapNode(value = 1))
# print heap
# print heap.pop()
# print heap
# heap.delete(2)
# print heap
# while(len(heap.heap_arr)>1):
# 	print heap.pop(),",",
# print "\n"