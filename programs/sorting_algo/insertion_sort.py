# On each loop iteration, insertion sort removes one element from the array.
# It then finds the location where that element belongs within another sorted array 
# and inserts it there. It repeats this process until no input elements remain.

# complexity - Insertion sort runs in O(n) time in its best case 
# and runs in O(n^2) in its worst and average cases.

def insertion_sort(arr):

	for i in range(len(arr)):

		pos = i
		cursor = arr[i]
		print("pos =>", pos, "cursor =>", cursor)
		while pos > 0 and arr[pos-1] > cursor:
			print(arr[pos-1], cursor, "-1 pos & cursor")

			arr[pos] = arr[pos - 1]
			pos = pos - 1

		arr[pos] = cursor
	return arr

unsorted_list = [23, 89, 1, 43, 4, 55, 6, 41]

print(insertion_sort(unsorted_list))
