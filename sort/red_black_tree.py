class Node():

	RED = "red"
	BLACK = "black"

	def __init__(self,value):
		self.node_value = value
		self.left_child = self.right_child = None
		self.color = Node.RED
		self.parent = None

	def add_child(self, new_node):
		#print "add child to:", self.node_value
		new_node.parent = self
		if new_node.node_value > self.node_value:
			self.right_child = new_node
			#print "add right child:", new_node.node_value
		else:
			self.left_child = new_node
			#print "add left child:", new_node.node_value


class RBTree():

	def __init__(self):
		self.head = None
		self.depth = 0

	def insert(self,value):
		new_node = Node(value)
		# head insertion
		if self.head is None:
			new_node.color = Node.BLACK # Root should always be black
			self.head = new_node
			self.depth = 1
			#print "create head:",new_node.node_value
			return
		# find the new node parent
		curr_head = prev_head = self.head
		curr_depth = 0
		while(curr_head):
			#print "curr head:",curr_head.node_value
			prev_head = curr_head
			curr_depth+=1			
			if(curr_head.node_value < new_node.node_value):	
				curr_head = curr_head.right_child
			else:
				curr_head = curr_head.left_child
		# update depth if needed
		if(curr_depth>self.depth):
			self.depth = curr_depth
			#print "increase depth to:", self.depth
		print "add child under:",prev_head.node_value, " with value:", new_node.node_value
		prev_head.add_child(new_node)
		curr_node = new_node
		while (self.is_violating(curr_node)):
			curr_node = self.fix_violation(curr_node)

	def is_violating(self,node):
		# if none probably header  - no violation.
		if(node is None or node.parent is None):
			return False
		# check for 2 conscutive red nodes
		if (node.color == Node.RED and node.parent.color == Node.RED):
			print "conscutive red vialation!!!"
			return True
		else:
			return False

	def fix_violation(self,node):
		child_node = node
		parent_node = self.go_up(node,1)
		gp_node = self.go_up(node,2)
		ggp_node = self.go_up(node,3)
		uncle = self.get_uncle(child_node)
		# case: parent and uncle are red - solution is to recolor both.
		if(uncle is not None and uncle.color == Node.RED):
			print "fix recolor - uncle is:", uncle.node_value
			uncle.color = Node.BLACK
			parent_node.color = Node.BLACK
			if(gp_node <> self.head):
				gp_node.color = Node.RED
			return gp_node
		# check for classic right-rotation case
		if(child_node.node_value < parent_node.node_value and parent_node.node_value < gp_node.node_value):
			print "fix right rotation"
			self.rotate_right(gp_node,parent_node)
			if (self.head == gp_node):
				print "change header to:", parent_node.node_value
				self.head = parent_node
				parent_node.parent = None
			return parent_node
		# check for classic left-rotation
		if(child_node.node_value > parent_node.node_value and parent_node.node_value > gp_node.node_value):
			print "fix left rotation"
			self.rotate_left(gp_node,parent_node)
			if (self.head == gp_node):
				print "change header to:", parent_node.node_value
				self.head = parent_node
				parent_node.parent = None
			return parent_node
		#check for left-rifht rotation
		if(child_node.node_value > parent_node.node_value and parent_node.node_value < gp_node.node_value):
			print "-----------------fix left and right---------------"
			self.rotate_left(parent_node,child_node)
			self.rotate_right(gp_node,child_node)
		# check for right left rotation
		if(child_node.node_value < parent_node.node_value and parent_node.node_value > gp_node.node_value):
			print "--------------fix right and left------------------"
			self.rotate_right(parent_node,child_node)
			self.rotate_left(gp_node,child_node)

	def rotate_right(self,head,child):
		print "fix right rotation"
		# connect parent to gp parent (aka ggp)
		self.connect_nodes(child,self.go_up(head,1))
		# set parent to be the new header and set to black
		child.color = Node.BLACK
		# connect parent right child to be ggp left child 
		head.left_child = child.right_child
		if (child.right_child is not None):
			child.right_child.parent = head
		# connect gp to be child of new header
		self.connect_nodes(head,child)
		# set childeren to new header to red
		head.color = Node.RED
		# set new header if needed
		if (self.head == head):
			print "change header to:", child.node_value
			self.head = child
			child.parent = None
		return child

	def rotate_left(self,head,child):
		print "fix left rotation"
		# connect parent to gp parent (aka ggp)
		self.connect_nodes(child,self.go_up(head,1))
		# set parent to be the new header and set to black
		child.color = Node.BLACK
		# connect parent right child to be ggp left child 
		head.right_child = child.left_child
		if(child.left_child is not None):
			child.left_child.parent = head
		# connect gp to be child of new header
		self.connect_nodes(head,child)
		# set childeren to new header to red
		head.color = Node.RED
		# set new header if needed
		if (self.head == head):
			print "change header to:", child.node_value
			self.head = child
			child.parent = None
		return child

	def connect_nodes(self,source,target):
		# if not target  - nothing to connect
		if(target is None):
			return
		# connect child to point on nre father
		source.parent = target
		# connect father to point on child
		if source.node_value < target.node_value:
			target.left_child = source
		else:
			target.right_child = source


	def get_uncle(self,node):
		if(node.parent is None):
			return None
		gp = self.go_up(node,2)
		if (gp is None):
			return None
		is_left_node = True
		if (node.parent.node_value > gp.node_value):
			is_left_node = False
		if (is_left_node):
			return gp.right_child
		else:
			return gp.left_child

	def go_up(self,node,generation):
		papa = node
		for i in range(generation):
			if(papa is None):
				return
			papa = papa.parent
		return papa

	def traverse_tree(self,node):
		#traverse left
		if(node is None):
			return
		left_child = node.left_child
		right_child = node.right_child
		self.traverse_tree(left_child)
		if (node.parent is not None):
			print node.node_value, " color:", node.color, " parent:", node.parent.node_value, " | "
		else:
			print node.node_value, " color:", node.color, " parent: None | "
		self.traverse_tree(right_child)


	def print_tree(self):
		print "display tree with depth:", self.depth
		childs_arr = []
		childs_arr.append(self.head)
		depth = 1
		counter = 0
		while(childs_arr and counter < 20):
			print "level:", depth, "-- ", childs_arr, ":",
			new_childs_arr = []
			for i in range(len(childs_arr)):
				curr_node = childs_arr[i]
				if(curr_node):
					print curr_node.node_value, "-", curr_node.color, " parent->", 
					if(curr_node.parent):
						print curr_node.parent.node_value,
					else:
						print "None",
					if(curr_node.left_child):
						new_childs_arr.append(curr_node.left_child)
					if(curr_node.right_child):
						new_childs_arr.append(curr_node.right_child)
				else:
					print "NIL",
			counter+=1
			childs_arr = new_childs_arr
			depth+=1
			print "\n",


my_arr  = [2,5,7,22,53,77,12,66,44,234,57,213,33,1,8,99,100,80,81,82,83,84,85,86,87,88,89,90,91,92]
#my_arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
my_tree = RBTree()
for i in range(len(my_arr)):
	print "----adding:", my_arr[i]
	my_tree.insert(my_arr[i])
	my_tree.print_tree()
#my_tree.print_tree()
#my_tree.traverse_tree(my_tree.head)
