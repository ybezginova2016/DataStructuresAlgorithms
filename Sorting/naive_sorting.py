"""
Sorting-rearranging a collection of items into increasing or decreasing order-is a common problem
in computing. Sorting is used to preprocess the collection to make searching faster (as we saw
with binary search through an array), as well as identify items that are similar (e.g., students are
sorted on test scores).

Naive sorting algorithms run in O(n^2) time. A number of sorting algorithms run in O(nlogn)
time-heapsort, merge sort, and quicksort are examples
"""
# Approach:

# Create a Python file containing the required functions.
# Create another Python file and import the previous Python file into it.
# Call the functions defined in the imported file.

# Searching for the smallest element
def findSmallest(arr):
    smallest = arr[0] # storing the smallest
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

ls = [1, 55, -1, -13]
print(findSmallest(ls))