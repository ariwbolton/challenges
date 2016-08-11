# Unsolved

with open('p059_cipher.txt') as f:
	nums = f.readlines()

nums = [int(x) for x in nums[0].strip().split(',')]

print len(nums), len(nums) / 3

perms = []
validPerms = []

def populatePerms(perms):
	for first in xrange(97, 122 + 1):
		for second in xrange(97, 122 + 1):
			for third in xrange(97, 122 + 1):
				tup = (first, second, third)
				perms.append(tup)
				validPerms.append(1)

populatePerms(perms)

def solve(perms, validPerms):
	for i in xrange(0, 1197 + 1, 3):
		if i % 100 == 0:
			print "At index: ", i

		for perm in enumerate(perms):

			# check if permutation of keys is a valid permutation
			if validPerms[perm[0]] == 0:
				continue
			
			# unpack permutation
			first, second, third = perm[1]

			isValid = decryptString(i, first, second, third)

			if not isValid:
				#print first, second, third, "Not valid at index: ", i	
				validPerms[perm[0]] = 0

def decryptString(i, first, second, third):
	# retrieve chars to be decrypted (in sets of 3, per instructions)
	nFirst, nSecond, nThird = nums[i], nums[i+1], nums[i+2]
	
	# reverse XOR using first, second, and third as keys
	dFirst, dSecond, dThird = nFirst^first, nSecond^second, nThird^third

	# convert to string
	dFirst, dSecond, dThird = chr(dFirst), chr(dSecond), chr(dThird)

	if i == 0 and first == 97 and second == 97 and third == 97:
		print chr(first) + chr(second) + chr(third) + ": ", dFirst, dSecond, dThird

	dFirstValid = dFirst.isalpha() or dFirst == " " or dFirst == "'"
	dSecondValid = dSecond.isalpha() or dSecond == " " or dSecond == "'"
	dThirdValid = dThird.isalpha() or dThird == " " or dThird == "'"

	if dFirstValid and dSecondValid and dThirdValid:
		return True
	else:
		print chr(first) + chr(second) + chr(third) + ": ", dFirst, dSecond, dThird
		return False

	return True

solve(perms, validPerms)
perms = [x for x in perms if validPerms[perms.index(x)]]

print len(perms)
	

