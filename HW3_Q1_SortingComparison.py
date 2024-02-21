import numpy as np
import numpy as np
import time
import matplotlib.pyplot as plt

'''
Code is from https://www.geeksforgeeks.org/insertion-sort/
'''
# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):

	# Traverse through 1 to len(arr)
	for i in range(1, len(arr)):

		key = arr[i]

		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key


# This code is contributed by Mohit Kumra

'''
Code is from https://www.geeksforgeeks.org/merge-sort
'''
# Python program for implementation of MergeSort


def mergeSort(arr):
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements
		L = arr[:mid]

		# Into 2 halves
		R = arr[mid:]

		# Sorting the first half
		mergeSort(L)

		# Sorting the second half
		mergeSort(R)

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

# This code is contributed by Mayank Khanna



lengths = range(1, 20)
mergeTimes = []
insertTimes = []
# Loop and time the sorting algorithms
for i in range(1, 20):
    arr = np.arange(i, 0, -1)
    print(arr)
    # Time merge sort
    start_time = time.time()
    for _ in range(5000):
        mergeSort(arr.copy())
    mergeTimes.append(time.time() - start_time)
    
    # Time insertion sort
    start_time = time.time()
    for _ in range(5000):
        insertionSort(arr.copy())
    insertTimes.append(time.time() - start_time)

# Plotting the results
plt.figure()
plt.plot(lengths, mergeTimes, label='Merge Sort Time')
plt.plot(lengths, insertTimes, label='Insertion Sort Time')
plt.xlabel('Array Length')
plt.ylabel('Time (seconds)')
plt.title('Merge Sort vs. Insertion Sort Performance')
plt.xticks(range(1, 20))
plt.legend()
plt.show()