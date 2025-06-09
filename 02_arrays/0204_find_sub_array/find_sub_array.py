def find_sub_array(arr: list[int], s: int) -> list[int]:
    left: int = 0
    sub_total: int = 0
    for right in range(len(arr)):
        sub_total += arr[right]
        while left < right and sub_total > s:
            sub_total -= arr[left]
            left += 1
        if sub_total == s:
            return [left+1, right+1]
    return [-1]


# Test code
sample1 = ([1, 2, 3, 7, 5], 12)
sample2 = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15)
sample3 = ([1, 2, 3, 4], 0)
for arr, s in (sample1, sample2, sample3):
    print(find_sub_array(arr, s))