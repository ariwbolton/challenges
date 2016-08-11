# n > 0 : rotate left
def rotate(s, n):
    return s[n:] + s[:n]

# n > 0
def rotate_left(s, n):
    return rotate(s, n)
# n > 0
def rotate_right(s, n):
    return rotate(s, (-1)*n)


def isValid(s):
    n = 0
    
    for c in s:
        if c == '(':
            n = n + 1
        elif c == ')':
            n = n - 1

        if n < 0:
            return False

    return True

def find_lex_min(s):
    min_str = s
    
    for i in xrange(len(s)):
        temp = rotate(s, i)
        if temp < s and isValid(temp):
            min_str = temp

    return min_str

def find_lex_min_2(s):
    index, max_streak, current_streak = 0, 0, 0

    for i in xrange(len(s)):
        if s[i] == '(':
            current_streak = current_streak + 1
            if current_streak > max_streak:
                max_streak, index = current_streak, i
        elif s[i] == ')':
            current_streak = 0

    return rotate(s, index - (max_streak - 1))


print find_lex_min("((()(((())))))")
