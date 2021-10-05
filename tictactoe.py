from board import Board


run = True
# game loop


def main():
	while run:
		size = int(input("Board size: "))
		board = Board(size)
		print(board.update_board([1, 2]))
		input()


def check_winning():
	pass


def screen_whipe(n=25):
	return "\n" * n


if __name__ == "__main__":
	main()
