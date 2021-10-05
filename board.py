#https://en.m.wikipedia.org/wiki/Box_Drawing

class Board:

	def __init__(self, size):
		self.size = size
		self.board_data = self.create_board(self.size)
		self.turn = True


	def create_board(self, size):
		board_data = []
		for x in range(size):
			row = []
			for y in range(size):
				row.append("   ")
			board_data.append(row)
		return board_data


	def internal_board(self):
		internal_board = ""
		for x in range(len(self.board_data)):
			drawn_line = ""
			for y in range(len(self.board_data)):
				drawn_line += self.board_data[x][y]
				if y != len(self.board_data) -1 :
					drawn_line += "│"
			internal_board += drawn_line + "\n"
			if x < len(self.board_data) - 1:
				internal_board += "───┼" * (len(self.board_data) - 1) + "───" + "\n"
		return internal_board


	def draw_board(self):
		internal_board = self.internal_board()
		drawn_board = ""

		#drawing the boarder around the internal board
		internal_board = internal_board.split("\n")
		drawn_board += "╔═══" + "╤═══" * (self.size - 1) + "╗" + "\n"
		for x in range(0, self.size * 2, 2):
			drawn_board += "║" + internal_board[x] + "║" + f" :{int(x/2 +1)}" + "\n"
			if x != (self.size * 2) - 2:
				drawn_board += "╟" + internal_board[x + 1] + "╢" + "\n"
		drawn_board += "╚═══" + "╧═══" * (self.size - 1) + "╝" + "\n"

		for x in range(self.size):
			drawn_board += f" :{x + 1} "
		return drawn_board


	def update_board(self, position):
		x = position[0] - 1
		y = position[1] - 1

		#checking that the position is clear
		if self.board_data[x][y] != "   ":
			return False
		else:
			#update who's turn it is
			if self.turn == True:
				player = " X "
				self.turn = False
			else:
				player = " O "
				self.turn = True
			
			#adding the player icon to the board
			self.board_data[x][y] = player

		return self.draw_board()


#temp
a= Board(7)
print(a.draw_board())

print(a.update_board([1,2]))
