import linked_list as ll


class TestNode:
	def test__eq__true(self):
		node1 = ll.Node(cargo="Test")
		node2 = ll.Node(cargo="Test")
		assert node1 == node2

	def test__eq__false(self):
		node1 = ll.Node(cargo="Test1")
		node2 = ll.Node(cargo="Test2")
		assert (node1 == node2) == False

	def test__ne__true(self):
		node1 = ll.Node(cargo="Test1")
		node2 = ll.Node(cargo="Test2")
		assert node1 <> node2

	def test__ne__false(self):
		node1 = ll.Node(cargo="Test")
		node2 = ll.Node(cargo="Test")
		assert (node1 <> node2) == False

class TestLinkedList:
	def test_add(self):
		my_ll = ll.LinkedList()
		for x in range(0, 3):
			my_ll.add(ll.Node(cargo = x))
			assert my_ll.tail.cargo == x
			assert my_ll.head.cargo == 0

	def test_delete(self):
		my_ll = ll.LinkedList()
		for x in range(0, 3):
			my_ll.add(ll.Node(cargo = x))
		my_ll.delete(ll.Node(2))
		assert my_ll.tail.cargo == 1

	# TODO - test eq
	# TODO - test ne


