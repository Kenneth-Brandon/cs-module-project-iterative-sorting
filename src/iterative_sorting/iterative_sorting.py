import time

arr = [43, 2, 1, 77, 53, 54, 44, 6]

# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        # Your code here
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr


print('\nSelection Sort')
selection_start = time.time()
print(selection_sort(arr))
selection_end = time.time()
print(f"Runtime: {selection_end - selection_start}")

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # Your code here
    swaps = True
    for i in range(len(arr)):
        swaps = False
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps = True
        if swaps == False:
            break
    return arr


print('\nBubble Sort')
bubble_start = time.time()
print(bubble_sort(arr))
bubble_end = time.time()
print(f"Runtime: {bubble_end - bubble_start}")

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here
    if len(arr) == 0:
        return arr

    if min(arr) < 0:
        return "Error, negative numbers not allowed in the Count Sort"

    max_value = max(arr) + 1
    counts = [0] * (max_value)
    result = [0] * len(arr)

    for value in arr:
        counts[value] += 1

    sum_val = 0
    for i in range(len(counts)):
        temp = counts[i]
        counts[i] = sum_val
        sum_val += temp

    for value in arr:
        result[counts[value]] = value
        counts[value] += 1
    return result


# print(counting_sort([4, 2, 2, 8, 3, 3, 1]))
print('\nCounting Sort')
counting_start = time.time()
print(counting_sort(arr))
counting_end = time.time()
print(f"Runtime: {counting_end - counting_start}")
