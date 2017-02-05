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

