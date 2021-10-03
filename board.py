

class Board:

	def __init__(self, size):
		self.size = size
		print(self.draw_board(self.create_board(self.size)))

	def create_board(self, size):
		board = []
		for x in range(size):
			row = []
			for y in range(size):
				row.append(" ")
			board.append(row)
		return board


	def draw_board(self, board):
		drawn_board = ""
		for x in range(len(board)):
			drawn_line = ""
			for y in range(len(board)):
				drawn_line += board[x][y]
				if y != len(board) -1 :
					drawn_line += " | "
				else: 
					drawn_line += f"   :{y}"
			drawn_board += drawn_line + "\n"
			drawn_board += "- - " * len(board) + "" + "\n"
		return drawn_board




a= Board(7)
