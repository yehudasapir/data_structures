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


class TestDirectedGraph:
	def test_add_vertex_good(self):
		dag = ts.DirectedGraph()
		dag.add_vertex(name = 'A')
		assert dag.vertices[0].name == 'A'
		dag.add_vertex(name = 'B')
		assert dag.vertices[1].name == 'B'

	def test_add_vertex_bad(self):
		dag = ts.DirectedGraph()
		dag.add_vertex(name = 'A')
		with pytest.raises(ValueError):
			dag.add_vertex(name = 'A')

	def test_add_adge_good(self):
		dag = ts.DirectedGraph()
		dag.add_vertex(name = 'A')
		dag.add_vertex(name = 'B')
		dag.add_adge('A','B')
		assert dag.vertices[0].adjacency_list.head.cargo.name == 'B'

	def test_add_adge_no_such_adge(self):
		dag = ts.DirectedGraph()
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
		dag = ts.DirectedGraph()
		dag.add_vertex(name = 'A')
		assert dag.find_vertex('A').name == 'A'
		

		