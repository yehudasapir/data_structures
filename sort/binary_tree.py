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
		curr_depth = 0
		while(curr_head):
			prev_head = curr_head
			curr_depth+=1			
			if(curr_head.node_value < new_node.node_value):	
				curr_head = curr_head.right_child
			else:
				curr_head = curr_head.left_child
		#print "add child under:",prev_head.node_value, " with value:", new_node.node_value
		prev_head.add_child(new_node)
		curr_depth+=1
		if(curr_depth>self.depth):
			self.depth = curr_depth
			#print "increase depth to:", self.depth

	def traverse_dfs_tree(self,node,traversed_arr = []):
		if(node is None):
			return
		left_child = node.left_child
		right_child = node.right_child
		self.traverse_dfs_tree(left_child,traversed_arr)
		#print node.node_value, ", ",
		traversed_arr.append(node.node_value)
		self.traverse_dfs_tree(right_child,traversed_arr)
		return traversed_arr
		


	def print_tree(self):
		print "display tree with depth:", self.depth
		childs_arr = []
		childs_arr.append(self.head)
		depth = 1
		while(childs_arr):
			print "level:", depth, "-- ", childs_arr, ":",
			new_childs_arr = []
			for i in range(len(childs_arr)):
				curr_node = childs_arr[i]
				if(curr_node):
					print curr_node.node_value,
					if(curr_node.left_child):
						new_childs_arr.append(curr_node.left_child)
					if(curr_node.right_child):
						new_childs_arr.append(curr_node.right_child)
				else:
					print "NIL",
			childs_arr = new_childs_arr
			depth+=1
			print "\n",


if __name__ == "__main__":
	my_arr  = [2,5,7,22,53,77,12,66,44]
	my_tree = BinaryTree()
	for i in range(len(my_arr)):
		print "----adding:", my_arr[i]
		my_tree.insert(my_arr[i])
	my_tree.print_tree()
	sorted_arr = my_tree.traverse_dfs_tree(my_tree.head)
	print "\n",sorted_arr
