def hamming(s1, s2):
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

def find_swap(s1, s2, n):
    found = False
    i_f, j_f = 0, 0
    
    for i in xrange(n):
        if s1[i] == s2[i]:
            pass
        else:               # characters are not equal
            for j in xrange(n):
                if i != j and s1[i] == s2[j] and s1[j] == s2[i]:    # change == 2
                    S = swap_str(i, j, s1)
                    print hamming(S, s2)
                    first, last = min(i, j), max(i, j)
                    print str(first + 1), str(last + 1)
                    return
                elif i != j and s1[i] == s2[j] and not found: # and s1[i] != s2[i]
                    i_f, j_f = i, j
                    found = True

    if not found:
        print hamming(s1, s2)
        print "-1 -1"
    else:
        S = swap_str(i_f, j_f, s1)
        print hamming(S, s2)
        first, last = min(i_f, j_f), max(i_f, j_f)
        print str(first + 1), str(last + 1)
                            
def swap_str(i, j, s):
    first, last = min(i, j), max(i, j)

    return s[:first] + s[last] + s[first+1:last] + s[first] + s[last+1:]

n = int(raw_input())
s1 = raw_input()
s2 = raw_input()

find_swap(s1, s2,n)
'''
s = "nice"
print s
print swap_str(1, 3, s)'''
