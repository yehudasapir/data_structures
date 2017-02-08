import os
import sys
from sets import Set
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/' + '../simple_structures/')
import linked_list as ll

class Vertex:
	def __init__(self,name = None,value = 0,adjacency_list = None):
		self.name = name
		self.value = value
		self.adjacency_list = ll.LinkedList()
		self.in_degree = 0

	def add_adjecency(self,name_target):
		adge = self.adjacency_list.head
		while (adge):
			if adge.cargo == name_target:
				raise ValueError
			adge = adge.next
		self.adjacency_list.add(ll.Node(name_target))


class DirectedGraph:
	def __init__(self):
		self.vertices = []
		self.names_set = Set()

	def add_vertex(self,name = None, value = 0, adjacency_list = None):
		# check if vertex already exists
		if name not in self.names_set:
			node = Vertex(name,value,adjacency_list)
			self.vertices.append(node)
		else:
			raise ValueError

	def add_adge(self,name_source,name_target):
		source = find_vertex(name_source)
		source.add_adjecency(name_target)
				
	def find_vertex(self,name = None):
		for node in self.vertices:
			if node.name == name:
				return node
		return None
