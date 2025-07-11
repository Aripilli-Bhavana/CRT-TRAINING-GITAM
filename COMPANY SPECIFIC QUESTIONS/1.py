'''you are given an array of n strings, you have to find out the number of balanced strings from the given array.
 The string is said to be balanced if and only if its middle character has equal non-zero count in the left substring and right substring.
 note: while checking the balance consider the middle character exclusively.
 input : 5
 output : 3
 '''
def is_balanced(s):
    n = len(s)
    if n % 2 == 0:
        return False
    mid = n // 2
    left = s[:mid]
    right = s[mid + 1:]
    
    left_count = {}
    right_count = {}
    
    for char in left:
        left_count[char] = left_count.get(char, 0) + 1
    
    for char in right:
        right_count[char] = right_count.get(char, 0) + 1
    
    return left_count == right_count
def count_balanced_strings(arr):
    count = 0
    for s in arr:
        if is_balanced(s):
            count += 1
    return count
