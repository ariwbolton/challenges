def double_base_palindromes(up_to):
    return sum(i for i in range(up_to + 1) if is_palindrome(str(i)) and is_palindrome("{0:b}".format(i)))

def is_palindrome(s):
    return s == s[::-1]

print((double_base_palindromes(10 ** 6)))