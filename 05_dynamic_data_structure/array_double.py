def ArrayDouble(old_array: list):
    length: int = len(old_array)
    new_array: list = [None] * (2 * length)

    j: int = 0
    while j < length:
        new_array[j] = old_array[j]
        j += 1
    return new_array

print(ArrayDouble([1,2,3,4]))