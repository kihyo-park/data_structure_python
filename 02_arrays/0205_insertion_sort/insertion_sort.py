def InsertionSort(array: list):
    n: int = len(array)
    i: int = 1
    while i < n:
        current = array[i] # outer loop: start from i = 1 in the initialized setting(=not sorted yet)
        j: int = i-1
        while j >= 0 and array[j] > current: # inner loop: repeat sorted prefixes from the end of the arry by using index 'j'.
            array[j+1] = array[j]
            j -= 1
        array[j+1] = current
        i += 1
    return array

array = [61, 82, 67, 4, 98, 20, 37, 85]
print(InsertionSort(array))


    