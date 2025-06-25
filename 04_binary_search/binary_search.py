import math

def BinarySearch(array: list, target: int):
    """Assumption: arrays should be sorted in an ascending way"""
    IndexHigh: int = len(array) - 1
    IndexLow: int = 0
    while IndexLow  <= IndexHigh:
        IndexMid: int = math.floor((IndexHigh + IndexLow)/2)
        
        if array[IndexMid] == target:
            return IndexMid
        if array[IndexMid] < target:
            IndexLow = IndexMid + 1
        else:
            IndexHigh = IndexMid - 1
    return -1
    # Time complexity: O(log_2(N))

array = [-5, -1, 0, 3, 9, 11, 15, 17, 30, 35, 51, 54]
true_target = 15
false_target = 10

print(BinarySearch(array, true_target), BinarySearch(array, false_target))

# Have a look at Binary Section (이분법)