import sys

class HeapNode:
	def __init__(self, value = None, cargo = None):
		self.value = value
		self.cargo = cargo
	
	def __eq__(self,other):
		return self.value==other

	def __str__(self):
		return str(self.value)

	__repr__ = __str__

class Heap:
	def __init__(self, is_min = True):
		self.heap_arr = [sys.maxint]
		self.is_min = is_min

	def __str__(self):
		return str(self.heap_arr[1:])

	__repr__ = __str__

	def add(self, node = None):
		if node == None:
			raise ValueError("cant add None value to heap!")
		self.heap_arr.append(node)
		index = len(self.heap_arr) - 1
		self.bubble_up(index/2,index)

	def delete(self,obj=None):
		if(obj==None):
			return
		if isinstance(obj,int):
			self.delete_by_index(obj)
		elif(isinstance,HeapNode):
			self.delete_by_node(obj)

	def delete_by_node(self,obj):
		index = self.find_node(obj)
		if(index>0):
			self.delete_by_index(index)

	def find_node(self,obj):
		if(obj==None):
			return
		for index,node in enumerate(self.heap_arr):
			if(obj==node):
				return index
		return -1

	def delete_by_index(self,index):
		lenth=len(self.heap_arr)
		if(index>(lenth-1)):
			return
		last=self.heap_arr.pop()
		self.heap_arr[index]=last
		self.bubble_down(index,index*2)
		self.bubble_down(index,index*2+1)

	def pop(self):
		head=self.heap_arr[1]
		last = self.heap_arr.pop()
		if(len(self.heap_arr)>1):
			self.heap_arr[1]=last
			self.bubble_down(1,2)
			self.bubble_down(1,3)
		return head

	def bubble_up(self,parent_index, child_index):
		lenth = len(self.heap_arr)
		if (parent_index > (lenth-1) or child_index > (lenth-1)):
			return
		if(parent_index == 0 or child_index == 0):
			return
		if(self.heap_arr[parent_index].value < self.heap_arr[child_index].value):
			if(self.is_min):
				return
			else:
				self.swap(parent_index,child_index)
				self.bubble_up(parent_index/2,parent_index)
				return
		else:
			if(self.is_min):
				self.swap(parent_index,child_index)
				self.bubble_up(parent_index/2,parent_index)
				return
			else:
				return

	def bubble_down(self,parent_index, child_index):
		lenth = len(self.heap_arr)
		if (parent_index > (lenth-1) or child_index > (lenth-1)):
			return
		if(self.heap_arr[parent_index].value < self.heap_arr[child_index].value):
			if(self.is_min):
				return
			else:
				self.swap(parent_index,child_index)
				self.bubble_down(child_index,child_index*2)
				self.bubble_down(child_index,child_index*2+1)
				return
		else:
			if(self.is_min):
				self.swap(parent_index,child_index)
				self.bubble_down(child_index,child_index*2)
				self.bubble_down(child_index,child_index*2+1)
				return
			else:
				return

	def swap(self,source_index,target_index):
		tmp = self.heap_arr[source_index]
		self.heap_arr[source_index] = self.heap_arr[target_index]
		self.heap_arr[target_index] = tmp


if __name__ == "__main__":
	heap = Heap()
	heap.add(HeapNode(value = 5))
	heap.add(HeapNode(value = 9))
	heap.add(HeapNode(value = 3))
	heap.add(HeapNode(value = 7))
	heap.add(HeapNode(value = 11))
	heap.add(HeapNode(value = 1))
	print heap
	print heap.pop()
	print heap
	heap.delete(2)
	print heap
	while(len(heap.heap_arr)>1):
		print heap.pop(),",",
	print "\n"

	print "-----------------------"

	heap = Heap(is_min = False)
	heap.add(HeapNode(value = 5))
	heap.add(HeapNode(value = 9))
	heap.add(HeapNode(value = 3))
	heap.add(HeapNode(value = 7))
	heap.add(HeapNode(value = 11))
	heap.add(HeapNode(value = 1))
	print heap
	print heap.pop()
	print heap
	heap.delete(2)
	print heap
	while(len(heap.heap_arr)>1):
		print heap.pop(),",",
	print "\n"
