from board import Board


run = True
# game loop


def main():
	while run:
		# inputs:
		size = int(input("Board size: "))
		n_to_win = 0
		while n_to_win <= 2 or n_to_win > size:
			n_to_win = int(input(f"How many in a row to win? [3-{size}]: "))

		board = Board(size)
		print(board.update_board([1, 2]))
		input()


def check_winning():
	pass


def screen_whipe(n=25):
	return "\n" * n


if __name__ == "__main__":
	main()
