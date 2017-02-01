import numpy as np

class Node():

	def __init__(self,value):
		self.node_value = value
		self.left_child = self.right_child = None

	def add_child(self, new_node):
		#print "add child to:", self.node_value
		if new_node.node_value > self.node_value:
			self.right_child = new_node
			#print "add right child:", new_node.node_value
		else:
			self.left_child = new_node
			#print "add left child:", new_node.node_value


class BinaryTree():

	def __init__(self):
		self.head = None
		self.depth = 0

	def insert(self,value):
		new_node = Node(value)
		# head insertion
		if self.head is None:
			self.head = new_node
			self.depth = 1
			#print "create head:",new_node.node_value
			return
		# find the new node parent
		curr_head = prev_head = self.head
		curr_depth = 1
		while(curr_head):
			prev_head = curr_head
			curr_depth+=1			
			if(curr_head.node_value < new_node.node_value):	
				curr_head = curr_head.right_child
			else:
				curr_head = curr_head.left_child
		#print "add child under:",prev_head.node_value, " with value:", new_node.node_value
		prev_head.add_child(new_node)
		if(curr_depth>self.depth):
			self.depth = curr_depth
			#print "increase depth to:", self.depth

	def traverse_tree(self,node):
		#traverse left
		if(node is None):
			return
		left_child = node.left_child
		right_child = node.right_child
		self.traverse_tree(left_child)
		print node.node_value, ", ",
		self.traverse_tree(right_child)
		


	def print_tree(self):
		w = 2**(self.depth-1)
		h = self.depth
		tree_matrix = np.zeros((h,w))
		print "display tree with depth:", self.depth
		childs_arr = []
		childs_arr.append(self.head)
		depth = 1
		index = w/2-1
		skip = 2
		while(childs_arr):
			print "level:", depth, "-- ", childs_arr, ":",
			new_childs_arr = []
			for i in range(len(childs_arr)):
				curr_node = childs_arr[i]
				if(curr_node):
					print curr_node.node_value,
					tree_matrix.itemset((depth-1,index),curr_node.node_value)
					new_childs_arr.append(curr_node.left_child)
					new_childs_arr.append(curr_node.right_child)
				else:
					print "NIL",
				index+=skip
			childs_arr = new_childs_arr
			depth+=1
			index = w/2 - (self.depth - 1)
			if depth == self.depth:
				skip=1
			print "\n",
		print "--------------tree_matrix-------------------"
		h,w = tree_matrix.shape
		for i in range(h):
			for j in range(w):
				print tree_matrix.item((i,j)),
			print "\n",

my_arr  = [2,5,7,22,53,77,12,66,44]
my_tree = BinaryTree()
for i in range(len(my_arr)):
	print "----adding:", my_arr[i]
	my_tree.insert(my_arr[i])
#my_tree.print_tree()
my_tree.traverse_tree(my_tree.head)

# my_sorted_arr = [0,1,2,3,4,5,6,7,8,9]
# my_blbanced_tree = BinaryTree()
# def split_arr(arr):
# 	size = len(arr)
# 	print "working on:", arr
# 	if not arr:
# 		print "null array"
# 		return
# 	if size == 1:
# 		print "inserting:", arr[0]
# 		my_blbanced_tree.insert(arr[0])
# 		return
# 	else:
# 		print "inserting:", arr[size/2]
# 		my_blbanced_tree.insert(size/2)
# 		split_arr(arr[:(size/2)])
# 		split_arr(arr[(size/2+1):])

# split_arr(my_sorted_arr)
# my_blbanced_tree.print_tree()
