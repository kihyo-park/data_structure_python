def LinearScan(array: list, target: int):
    i: int = 0
    while i < len(array):
        if array[i] == target:
            return i
        i += 1
    return -1
    # Time copmlexity: O(n)

array = [1, 2, 3, 4]
true_target = 4
false_target = 5

print(LinearScan(array, true_target), LinearScan(array, false_target))