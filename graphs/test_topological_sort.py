import pytest
import topological_sort as ts

class TestVertex:
	def test_add_adjecency_good(self):
		vertex = ts.Vertex(name = 'A',value = 0)
		vertex.add_adjecency('B')
		assert vertex.adjacency_list.head.cargo == 'B'

	def test_add_adjecency_error(self):
		vertex = ts.Vertex(name = 'A',value = 0)
		vertex.add_adjecency('B')
		with pytest.raises(ValueError):
			vertex.add_adjecency('B')