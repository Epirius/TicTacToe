from board import Board
import random


def main():
	run = True
	# game loop
	while run:
		board = Board(3)
		screen_whipe()
		print(board.draw_board())
		while check_winning(board) is not True:
			board.update_board(xy_input(board))  # players turn

			if check_winning(board) is True:  # check if player won
				screen_whipe()
				print(board.draw_board())
				print("You Won!")
				input()
				continue

			screen_whipe()
			print(board.update_board(ai_turn(board)))  # ai turn

			if check_winning(board) is True:  # chek if ai won
				screen_whipe()
				print(board.draw_board())
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

		if len(coordinates) != 2:
			print("Invalid input: expected 2 numbers")
			continue

		coordinates[0] = int(coordinates[0])
		coordinates[1] = int(coordinates[1])

		if coordinates[0] not in range(1, 4) or coordinates[1] not in range(1, 4):
			print("Invalid input: x and y need to be between 1 and 3")
			continue
		if board.check_pos(coordinates) is not True:
			print("Invalid position: occupied square")
			continue
		return coordinates


def ai_turn(board):  # TODO:
	while True:
		x = random.choice(range(1, 4))
		y = random.choice(range(1, 4))
		pos = [x, y]
		if board.check_pos(pos):
			return pos


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


def screen_whipe(n=75):
	print("\n" * n)


if __name__ == "__main__":
	main()
