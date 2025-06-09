def is_palindrome(word: str) -> bool:
    """문자열 word가 회문(palindrome)인지 검사한다.
    Arguments:
        word (str): 회문인지 검사할 문자열
    Return:
        bool: 회문이면 True, 그렇지 않으면 False를 반환
    """
    # we use two-pointers approach
    left = 0
    right = len(word) - 1

    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

words = ["racecar", "rotor", "tomato", "별똥별", "코끼리"]
for word in words:
    print(f"Is '{word}' palindrome?  {is_palindrome(word)}")