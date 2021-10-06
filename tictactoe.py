from board import Board


def main():
	run = True
	# game loop
	while run:
		board = Board(3)
		print(board.draw_board())
		while check_winning(board) is not True:
			board.update_board(xy_input(board))  # players turn

			if check_winning(board) is True:  # check if player won
				print("You Won!")
				input()
				continue

			print(board.update_board(ai_turn()))  # ai turn

			if check_winning(board) is True:  # chek if ai won
				print("AI Won!")
				input()
				continue

		run = False  # end the game, if the game should continue you might need to delete the board, and set run to true


def xy_input(board):
	"""Returns x,y from user input
	"""
	while True:
		coordinates = input("Position (x,y): ")
		coordinates = coordinates.split(",")
		coordinates[0] = int(coordinates[0])
		coordinates[1] = int(coordinates[1])

		if coordinates[0] not in range(1, 4) or coordinates[1] not in range(1, 4):
			print("Invalid input: x and y need to be between 1 and 3")
			continue
		if len(coordinates) > 2:
			print("Invalid input: only expected 2 numbers")
			continue
		if len(coordinates) < 1:
			print("Invalid input: no input given")
			continue
		if board.check_pos(coordinates) is not True:
			print("Invalid position: occupied square")
			continue
		return coordinates


def ai_turn():  # TODO:
	return[1, 2]


def check_winning(board):
	data = board.board_data
	for icon in [" X ", " O "]:
		for row in data:
			if row[0] == row[1] == row[2] and row[0] == icon:
				return True

		for column in zip(*data):
			if column[0] == column[1] == column[2] == icon:
				return True

		if data[0][0] == data[1][1] == data[2][2] == icon:
			return True

		if data[0][2] == data[1][1] == data[2][0] == icon:
			return True
	return False


def screen_whipe(n=25):
	return "\n" * n


if __name__ == "__main__":
	main()
