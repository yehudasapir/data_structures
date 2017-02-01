import merge_sort as ms

class TestMergeSort:

	def test_sort_arr(self):
		assert ms.sort_arr([4,3,2,1,5,6,7,9,10,8]) == [1,2,3,4,5,6,7,8,9,10]

	def test_merge_sort_arrs(self):
		assert ms.merge_sort_arrs([1,3,5,7,9],[2,4,6,8,10,11,12]) == [1,2,3,4,5,6,7,8,9,10,11,12]

