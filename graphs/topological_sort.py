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
		self.parents = Set()

	def add_adjecency(self,vertex):
		adge = self.adjacency_list.head
		while (adge):
			if adge.cargo == vertex:
				raise ValueError("adge already exists for:" + vertex.name)
			adge = adge.next
		self.adjacency_list.add(ll.Node(vertex))
		vertex.in_degree+=1

	def __eq__(self,other):
		return self.name == other.name

	def __ne__(self,other):
		return self.name <> other.name


class DirectedGraph:
	def __init__(self):
		self.vertices = []
		self.names_set = Set()

	def add_vertex(self,name = None, value = 0, adjacency_list = None):
		# check if vertex already exists
		if name not in self.names_set:
			node = Vertex(name,value,adjacency_list)
			self.vertices.append(node)
			self.names_set.add(name)
		else:
			raise ValueError("vertex already exists:" + name)

	def add_adge(self,name_source,name_target):
		source = self.find_vertex(name_source)
		if(source is None):
			raise ValueError("no such vertex:" + name_source)
		target = self.find_vertex(name_target)
		if(target is None):
			raise ValueError("no such vertex:" + name_target)
		if(name_source == name_target):
			raise ValueError("cant connect vertex to itself:" + name_source)
		if not self.is_cycle(source,target):
			source.add_adjecency(target)
			target.parents.add(source.parents)
			target.parents.add(source)
		else:
			raise ValueError("cycle is not allowed:" + name_target)
				
	def find_vertex(self,name = None):
		for node in self.vertices:
			if node.name == name:
				return node
		return None

	def is_cycle(self,vertex_from,vertex_to):
		if vertex_to in vertex_from.parents:
			return True
		return False



class TopologicalSort:
	def __init__(self):
		self.dr = DirectedGraph()
