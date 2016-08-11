field = """O O O O X O O O O O
X X O O O O O O X O
O O O O O O O O O O
O O O O O O O O O O
O O O O O X O O O O"""

field = [row.split(" ") for row in field.split("\n")]

for row in enumerate(field):
	field[row[0]] = " ".join(row[1])

print field
