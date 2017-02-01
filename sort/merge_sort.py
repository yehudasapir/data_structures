import sys, getopt

def sort_arr(source_arr):
	print "start:", source_arr
	size = len(source_arr)
	print size
	if(size < 2):
		return source_arr
	
	sorted_arr = []
	if (size == 2):
		num1 = source_arr[0]
		num2 = source_arr[1]
		if (num1 > num2):
			sorted_arr.append(num2)
			sorted_arr.append(num1)
			return sorted_arr
		else:
			sorted_arr.append(num1)
			sorted_arr.append(num2)
			return sorted_arr
	half = size/2
	arr1 = sort_arr(source_arr[:half])
	arr2 = sort_arr(source_arr[half:]) 
	print "merge:", arr1, ":", arr2
	return merge_sort_arrs(arr1,arr2)


def merge_sort_arrs(sorted_arr1, sorted_arr2):
	merged_sorted_arr = []
	size1 = len(sorted_arr1)
	size2 = len(sorted_arr2)
	print "size1:", size1
	print "size2:", size2
	index1=index2=0
	# loop until one of arrays is finished
	while (index1 < size1 and index2 < size2):
		if sorted_arr1[index1] < sorted_arr2[index2]:
			merged_sorted_arr.append(sorted_arr1[index1])
			index1+=1
		else:
			merged_sorted_arr.append(sorted_arr2[index2])
			index2+=1
	# if array 1 is not done add it
	while (index1 < size1):
		merged_sorted_arr.append(sorted_arr1[index1])
		index1+=1
	# if array 2 is not done add it
	while (index2 < size2):
		merged_sorted_arr.append(sorted_arr2[index2])
		index2+=1
			
	print "sorted arr:", merged_sorted_arr
	return merged_sorted_arr


if __name__ == "__main__":
	my_arr  =[2,8,4,11,55,88,4,7,90,1,34,55,345,56,3,567,234,67,333]
	sort_arr(my_arr)






