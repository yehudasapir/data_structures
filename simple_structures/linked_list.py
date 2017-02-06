

class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)

    def __eq__(self,other):
    	if(other == None):
    		if(self.cargo == None and self.next == Node):
    			return True
    		return False
    	return self.cargo == other.cargo

    def __ne__(self,other):
    	return self.cargo <> other.cargo


class LinkedList:
	def __init__(self,cargo=None):
		self.head = self.tail = cargo

	def add(self,node):
		if(self.head == None):
			self.head = self.tail = node
			return
		self.tail.next = node
		self.tail = node

	#deletes the first node with similar value from list
	def delete(self,node):
		curr = prev = self.head
		while(curr):
			if (curr == node):
				prev.next = curr.next
				if (self.tail == curr):
					self.tail = prev
				return
			prev = curr
			curr = curr.next

	def __eq__(self,other):
		node1 = self.head
		node2 = other.head
		while (node1 and node2):
			if(node1 == node2):
				node1 = node1.next
				node2 = node2.next
			else:
				return False
		return True

	def __ne__(self,other):
		node1 = self.head
		node2 = other.head
		while (node1 and node2):
			if(node1 == node2):
				node1 = node1.next
				node2 = node2.next
			else:
				return True
		return False
