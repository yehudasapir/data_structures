import os
import sys
from sets import Set
from collections import deque
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
		if(other == None):
			if (self.name == None):
				return True
			else:
				return False
		return self.name == other.name

	def __ne__(self,other):
		return self.name <> other.name

	def __hash__(self):
		return  hash(self.name)

	def __str__(self):
		return self.name

	__repr__ = __str__

class DirectedAcyclicGraph:
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
			target.parents.update(source.parents)
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
	def __init__(self,dag):
		if dag is not None:
			self.dag = dag
		else:
			self.dag = DirectedAcyclicGraph()
		self.in_degree_zero_queue = deque()
		self.sorted_topology = []

	def find_in_degree_zero(self):
		#print self.dag.vertices
		for node in self.dag.vertices:
			#print "node:", node.name, " in_degree:",node.in_degree 
			if node.in_degree == 0:
				#print "find_in_degree_zero:", node.name
				self.in_degree_zero_queue.appendleft(node)

	def find_topology(self):
		sort_arr = []
		self.find_in_degree_zero()
		while(self.in_degree_zero_queue):
			curr_vertex = self.in_degree_zero_queue.pop()
			sort_arr.append(curr_vertex)
			self.reduce_in_degree(curr_vertex)
		#print sort_arr
		self.sorted_topology = sort_arr

	def reduce_in_degree(self, source_vertex):
		curr_vertex  = source_vertex.adjacency_list.head
		while(curr_vertex):
			curr_vertex.cargo.in_degree-=1
			if(curr_vertex.cargo.in_degree == 0):
				self.in_degree_zero_queue.append(curr_vertex.cargo)
			curr_vertex = curr_vertex.next

	def __str__(self):
		return str(self.sorted_topology)

	__repr__ = __str__

if __name__ == "__main__":
	dag = DirectedAcyclicGraph()
	dag.add_vertex(name = 'A')
	dag.add_vertex(name = 'B')
	dag.add_vertex(name = 'D')
	dag.add_vertex(name = 'C')
	dag.add_vertex(name = 'F')
	dag.add_vertex(name = 'E')
	dag.add_adge('A','B')
	dag.add_adge('A','D')
	dag.add_adge('B','C')
	dag.add_adge('C','D')
	dag.add_adge('D','E')
	dag.add_adge('C','E')
	ts = TopologicalSort(dag)
	ts.find_topology()
	print ts
	
