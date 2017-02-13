import sys

class HeapNode:
	def __init__(self, value = None, cargo = None, parent = None):
		self.value = value
		self.cargo = cargo
		self.parent = parent

class heap:
	def __init__(self, is_min = True):
		self.heap_arr = [sys.maxint]
		self.is_min = is_min

	def add(self, node = None):
		if node == None:
			raise ValueError("cant add None value to heap!")
		self.heap_arr.append(node)
		size = len(self.heap_arr)
		if size > 2:
			node.parent = self.heap_arr[size/2]
		else:
			node.parent = None
		bubble_up(node)

	def bubble_up(self,node):
		if(node == None):
			return
		if(node.parent ==  None):
			return
		if(node.value < node.parent.value):
			if(self.is_min):
				return
			else:
				self.swap(node,node.parent)
				self.bubble_up(node)
		else:
			if(self.is_min):
				self.swap(node,node.parent)
				self.bubble_up(node)
			else:
				return