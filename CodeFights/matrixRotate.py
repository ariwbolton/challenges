mat = [
	[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12],
	[13,14,15,16]
]


def printMat(m):
	for i in m:
		print i

def transpose(m):
	for row in range(len(m)):
		for col in range(row, len(m)):
			temp = m[row][col]
			m[row][col] = m[col][row]
			m[col][row] = temp

def flipVert(m):
	for row in range(len(m) / 2):
		temp = m[row]
		m[row] = m[len(m) - row - 1]
		m[len(m) - row - 1] = temp

def rotateClockwise(m):
	flipVert(m)
	transpose(m)

rotateClockwise(mat)
printMat(mat)
