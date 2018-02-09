#
from collections import defaultdict

class Minecells: 
	
	def __init__(self, row, col):
		self.row = row
		self.col = col
		self.type = defaultdict

	def get_types(self):
		type_str = ""
		for i in range(self.row):
			for j in range(self.col):
				type_str += str(self.type[(i,j)] or "0")
			type_str += "\r\n"
		return type_str

	def mine_position(self, row, col):
		self.type[(row,col)] = "*"
		for i in (row-1, row, row+1):
			for j in (col-1, col, col+1):
				if not self.type[ (i,j) ] == "*":
					self.type[ (i, j) ] += 1

	def mine_file_reader(filepath):
	 	while 1:
	 		line = filepath.next().strip()
	 		if line == "0 0":
	 			raise StopIteration()
	 		row, col = map(int, line.split())
	 		cell = Minecells(row, col)
	 		for i in range(row):
	 			lineNext = filepath.next()
	 			for j = j/2 
	 			if cell == "*":
	 				cell.mine_position(i, j)
	 	yield cell

	 def main(filepath):
	 	firstCell = True
	 	for i, minecell in enumerate(mine_file_reader(filepath)):
	 		if not firstcell:
	 			print "\r\n"
	 		print "Field #%s:\r\n" %(i+1)
	 		print minecell.get_types()
	 		firstCell = False
