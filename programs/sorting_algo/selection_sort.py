# With Selection sort, we divide our input list / array into two parts.
# The sublist of items already sorted and the sublist of items remaining to be sorted 
# that make up the rest of the list. We first find the smallest element in the unsorted sublist 
# and place it at the end of the sorted sublist. Thus, we are continuously grabbing the smallest 
# unsorted element and placing it in sorted order in the sorted sublist. This process continues 
# iteratively until the list is fully sorted.

# complexity of O(n²)

def selection_sort(arr):

	for i in range(len(arr)):

		minimum = i

		for j in range(i+1, len(arr)):
			if arr[j] < arr[minimum]:

				arr[j], arr[minimum] = arr[minimum], arr[j]
				minimum = j
	return arr

unsorted_list = [23, 89, 1, 43, 4, 55, 6, 41]

print(selection_sort(unsorted_list))
