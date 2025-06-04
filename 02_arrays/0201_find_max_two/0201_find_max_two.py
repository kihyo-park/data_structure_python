def find_max_two(array: list[int]) -> list[int]:
    """
    -- Example 1 --
    input: [3, -1, 5, 0, 7, 4, 9, 1]
    return: [9, 7]

    -- Example 2 --
    input: [7]
    return: [7]
    """
    # We find the largest (and second largest) number(s) by comparing two elements in the given input sequentially. 
    if len(array) < 2:
        return array # Return the array when len(array) is just one.
    max1, max2 = array[:2] # Assume the first and second elements are max1 and max2
    if max2 > max1:
        max1, max2 = max2, max1
    for num in array[2:]: # Compare the other elements from the third element.
        if num > max1:
            max1, max2 = num, max1
        elif num > max2:
            max2 = num
    
    return [max1, max2]
    
# Test code
array = [[3, -1, 5, 0, 7, 4, 9, 1], [7]]
for i in array:
    print(f"The largest (and the second largest) number(s): {find_max_two(i)}")