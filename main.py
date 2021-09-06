class Player(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

class Game(object):

	NOUGHT = "O"
	CROSS = "X"
	WINNING_SCENARIOS = (
		((0, 0), (0, 1), (0, 2)),
		((1, 0), (1, 1), (1, 2)),
		((2, 0), (2, 1), (2, 2)),
		((0, 0), (1, 0), (2, 0)),
		((0, 1), (1, 1), (2, 1)),
		((0, 2), (1, 2), (2, 2)),
		((0, 0), (1, 1), (2, 2)),
		((0, 2), (1, 1), (2, 0)),
	)

	def __init__(self, player_one, player_two):
		self.board = [
			["_", "_", "_"],
			["_", "_", "_"],
			["_", "_", "_"]
		]
		self.player_one = player_one
		self.player_two = player_two
		self.mark_types = {self.player_one: self.NOUGHT, self.player_two: self.CROSS}
		self.finished = False

	def check_for_winner(self, player):
		scenario_results = []
		for scenario in self.WINNING_SCENARIOS:
			scenario_result = all([self.board[x][y] == self.mark_types[player] for x, y in scenario])
			scenario_results.append(scenario_result)

		return any(scenario_results)

	def make_play(self, player, x_coord, y_coord):
		mark_type = self.mark_types[player]
		self.board[x_coord][y_coord] = mark_type
		print(self)
		if self.check_for_winner(player):
			self.finished = True
			print(f'{player} wins!')

	def __str__(self):
		return '\n'.join([' '.join(row) for row in self.board])


def main():
	print("Welcome to this game of Tic-Tac-Toe!")
	current_player = player_one = Player(input("Name of player one: ").strip())
	next_player = player_two = Player(input("Name of player two: ").strip())
	game = Game(player_one, player_two)
	print(game)
	while not game.finished:
		print(f"\n{current_player} to play...")
		x_coord = int(input("x coordinate? ").strip())
		y_coord = int(input("y coordinate? ").strip())
		game.make_play(current_player, x_coord, y_coord)
		current_player, next_player = next_player, current_player


if __name__ == "__main__":
	main()

# no more possible moves; ie board is full
# sort out coordinates
# don't allow an already-chosen location
# handle out of range coordinates