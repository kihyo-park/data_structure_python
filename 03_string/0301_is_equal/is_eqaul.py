def StringEqual(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False
    
    n: int = len(str1)
    i: int = 0
    while i < n and str1[i] == str2[i]:
        i += 1
    
    return i == n

str1, str2 = "Hello world", "Hello friend" # False 
str3, str4 = "Hello world", "Hello world" # True
print(StringEqual(str1, str2), StringEqual(str3, str4))