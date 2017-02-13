import sys
import pytest
import topological_sort as ts

class TestVertex:
	def test_add_adjecency_good(self):
		vertex1 = ts.Vertex(name = 'A',value = 0)
		vertex2 = ts.Vertex(name = 'B',value = 0)
		vertex1.add_adjecency(vertex2)
		assert vertex1.adjacency_list.head.cargo.name == 'B'

	def test_add_adjecency_error(self):
		vertex1 = ts.Vertex(name = 'A',value = 0)
		vertex2 = ts.Vertex(name = 'B',value = 0)
		vertex1.add_adjecency(vertex2)
		with pytest.raises(ValueError):
			vertex1.add_adjecency(vertex2)

	def test_add_adjecency_in_degree(self):
		vertex1 = ts.Vertex(name = 'A',value = 0)
		vertex2 = ts.Vertex(name = 'B',value = 0)
		vertex1.add_adjecency(vertex2)
		assert vertex2.in_degree == 1
		vertex3 = ts.Vertex(name = 'C',value = 0)
		vertex3.add_adjecency(vertex2)
		assert vertex2.in_degree == 2


class TestDirectedAcyclicGraph:
	def test_add_vertex_good(self):
		dag = ts.DirectedAcyclicGraph()
		dag.add_vertex(name = 'A')
		assert dag.vertices[0].name == 'A'
		dag.add_vertex(name = 'B')
		assert dag.vertices[1].name == 'B'

	def test_add_vertex_bad(self):
		dag = ts.DirectedAcyclicGraph()
		dag.add_vertex(name = 'A')
		with pytest.raises(ValueError):
			dag.add_vertex(name = 'A')

	def test_add_adge_good(self):
		dag = ts.DirectedAcyclicGraph()
		dag.add_vertex(name = 'A')
		dag.add_vertex(name = 'B')
		dag.add_adge('A','B')
		assert dag.vertices[0].adjacency_list.head.cargo.name == 'B'

	def test_add_adge_no_such_adge(self):
		dag = ts.DirectedAcyclicGraph()
		with pytest.raises(ValueError):
			dag.add_adge('A','B')
		dag.add_vertex(name = 'A')
		with pytest.raises(ValueError):
			dag.add_adge('A','B')
		with pytest.raises(ValueError):
			dag.add_adge('A','A')
		with pytest.raises(ValueError):
			dag.add_adge('B','B')

	def test_find_vertex_good(self):
		dag = ts.DirectedAcyclicGraph()
		dag.add_vertex(name = 'A')
		assert dag.find_vertex('A').name == 'A'

	def test_is_cycle_error(self):
		dag = ts.DirectedAcyclicGraph()
		dag.add_vertex(name = 'A')
		dag.add_vertex(name = 'B')
		dag.add_vertex(name = 'C')
		dag.add_adge('A','B')
		dag.add_adge('B','C')
		# test simple cycle
		with pytest.raises(ValueError):
			dag.add_adge('B','A')
		# test more complex cycle
		with pytest.raises(ValueError):
			dag.add_adge('C','A')

class TestTopologicalSort:
	def test_find_in_degree_zero(self):
		dag = ts.DirectedAcyclicGraph()
		dag.add_vertex(name = 'A')
		top_search = ts.TopologicalSort(dag)
		top_search.find_in_degree_zero()
		assert len(top_search.in_degree_zero_queue) == 1
		top_search.in_degree_zero_queue.clear()
		dag.add_vertex(name = 'B')
		top_search.find_in_degree_zero()
		assert len(top_search.in_degree_zero_queue) == 2
		top_search.in_degree_zero_queue.clear()
		dag.add_adge('A','B')
		top_search.find_in_degree_zero()
		assert len(top_search.in_degree_zero_queue) == 1	

	def test_reduce_in_degree(self):
		dag = ts.DirectedAcyclicGraph()
		dag.add_vertex(name = 'A')			
		dag.add_vertex(name = 'B')
		assert dag.vertices[1].in_degree == 0
		dag.add_adge('A','B')
		top_search = ts.TopologicalSort(dag)
		assert dag.vertices[1].in_degree == 1
		top_search.reduce_in_degree(dag.vertices[0])
		assert dag.vertices[1].in_degree == 0

	def test_find_topology(self,capfd):
		dag = ts.DirectedAcyclicGraph()
		dag.add_vertex(name = 'A')
		dag.add_vertex(name = 'B')
		dag.add_vertex(name = 'C')
		dag.add_vertex(name = 'D')
		dag.add_vertex(name = 'E')
		dag.add_vertex(name = 'F')
		dag.add_adge('A','B')
		dag.add_adge('A','D')
		dag.add_adge('B','C')
		dag.add_adge('C','D')
		dag.add_adge('D','E')
		dag.add_adge('C','E')
		dag.add_adge('E','F')
		top_search = ts.TopologicalSort(dag)
		top_search.find_topology()
		print top_search.sorted_topology
		out,err=capfd.readouterr()
		assert out == '[A, B, C, D, E, F]\n'
		

		