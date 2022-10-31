import sys

BOARD_LENGTH = 9


def check_for_win(board):
	# returns string of winner, "draw" if draw, or false if moves still possible
	# would need to be rewritten for larger board_length
	if board[0] == board[3] == board[6]:
		return board[0]
	elif board[1] == board[4] == board[7]:
		return board[1]
	elif board[2] == board[5] == board[8]:
		return board[2]
	elif board[0] == board[1] == board[2]:
		return board[0]
	elif board[3] == board[4] == board[5]:
		return board[3]
	elif board[6] == board[7] == board[8]:
		return board[6]
	elif board[0] == board[4] == board[8]:
		return board[0]
	elif board[2] == board[4] == board[6]:
		return board[2]
	elif " " not in board:
		return "draw"
	else:
		return False


def check_if_equivalent(board1, board2):
	# rotates, flips, etc board1 and checks against board2
	if board1 == board2:
		return True
	if board1 in State.boards_to_states.keys():
		return True
	return False


def remove_equivalent_boards(boardslist):
	# takes list of boards, eliminates repeats
	boards_no_duplicates = []
	boards_no_duplicates.append(boardslist[0])
	for board1 in boardslist[1:]:
		board_good = True
		for board2 in boards_no_duplicates:
			if check_if_equivalent(board1, board2):
				board_good = False
		if board_good:
			boards_no_duplicates.append(board1)
	return boards_no_duplicates


def get_other_player(player):
	if player == "X":
		return "O"
	else:
		return "X"


class State(object):
	boards_to_states = {}

	def __init__(self, board, player):
		self.board = board
		self.player = player
		win = check_for_win(board)
		# get value (if end state)
		self.value = "undefined"
		if win:
			if win == "O":
				self.value = -1
			elif win == "X":
				self.value = 1
			else:
				self.value = 0
		if " " in self.board:
			# think of board children for each space
			self.child_boards = []
			for i in range(BOARD_LENGTH):
				if self.board[i] == " ":
					self.child_boards.append(self.board[:i] + self.player + self.board[i+1:])
			# check if repeat in children
			self.child_boards = remove_equivalent_boards(self.child_boards)
			# create non-repeated board children with player opposite of current, append those to child_nodes
			self.child_nodes = []
			for child_board in self.child_boards:
				self.child_nodes.append(State(child_board, get_other_player(self.player)))
		State.boards_to_states[self.board] = self

	def get_value(self):
		if self.value == "undefined":
			child_values = []
			for child in self.child_nodes:
				child_values.append(child.get_value())
			if self.player == "X":
				self.value = max(child_values)
			else:
				self.value = min(child_values)
		return self.value

	def get_best_move(self):
		# check self.value
		# iterate through children and return their values
		# see which is the first to have self.value
		# return that child's board
		for child_node in self.child_nodes:
			if child_node.get_value() == self.value:
				return child_node.board  # there's a problem here


def main():
    state0 = State(" " * BOARD_LENGTH, "X")
    # get the state from the user
    user_board = input("Enter board state (with X as you, X plays first, formatted 123456789): ")
    try:
        user_state = State.boards_to_states[user_board]
    except KeyError:
        print("Error: invalid board")
        sys.exit(1)
    value = user_state.get_value()
    if value == -1:
        print("Player will lose")
    elif value == 0:
        print("Player can draw")
    elif value == 1:
        print("Player can win")
    print("Ideal next move: " + user_state.get_best_move())


if __name__ == "__main__":
	main()