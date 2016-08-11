
def insertAtCorrectPlace(n, arr):
	lastSeen = -1
	i = len(arr)

	for current in arr:
		if current > n:
			i = arr.index(current)
			break

	arr.insert(i, n)

def lexOrderings(arr):
	# arr must be sorted in ascending order

	if len(arr) == 1:
		n = list()
		n.append([arr[0]])
		return n

	lex = []

	for num in arr:
		first = [num]

		arr.remove(num)

		l = lexOrderings(arr)

		insertAtCorrectPlace(num,arr)

		l = [first + perm for perm in l]

		lex = lex + l

	return lex

def stringToMappedArray(s):
	sortedS = sorted(s)

	a = []
	d = dict()

	for c in s:
		if c not in d:
			d[c] = 0

		

		i = sortedS.index(c) + d[c]

		a.append(i)

		d[c] += 1

	return a

def findLexIndexBrute(s):
	l = lexOrderings(range(len(s)))

	return l.index(stringToMappedArray(s)) + 1


s = "abcd"
n = "bacd"
n1 = "abdc"
n2 = "badc"

print findLexIndexBrute(s)
print findLexIndexBrute(n)
print findLexIndexBrute(n1)
print findLexIndexBrute(n2)
