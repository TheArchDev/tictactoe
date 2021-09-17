import random

NOUGHT = "O"
CROSS = "X"


class Player(object):
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def __str__(self):
        return self.name



class HumanPlayer(Player):
    pass


class AIPlayer(Player):
    pass


class Game(object):

    SPACE = "_"
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
        self.board = self.new_board()
        self.current_player = player_one
        self.waiting_player = player_two
        self.winner = None

    def new_board(self):
        return [
            [self.SPACE, self.SPACE, self.SPACE],
            [self.SPACE, self.SPACE, self.SPACE],
            [self.SPACE, self.SPACE, self.SPACE]
        ]

    def __str__(self):
        return "\n".join([" ".join(row) for row in self.board])

    @staticmethod
    def visual_y_location(y_coordinate):
        return 2-y_coordinate

    def valid_play(self, x_coordinate, y_coordinate):
        return self.board[self.visual_y_location(y_coordinate)][x_coordinate] == self.SPACE

    def play_turn(self, x_coordinate, y_coordinate):
        self.board[self.visual_y_location(y_coordinate)][x_coordinate] = self.current_player.mark
        if self.is_winning_turn():
            self.winner = True
        elif self.is_final_turn():
            self.winner = False
        else:
            self.current_player, self.waiting_player = self.waiting_player, self.current_player

    def is_winning_turn(self):
        scenario_matches = []
        for scenario in self.WINNING_SCENARIOS:
            scenario_match = all([self.board[self.visual_y_location(y)][x] == self.current_player.mark for x, y in scenario])
            scenario_matches.append(scenario_match)

        return any(scenario_matches)

    def is_final_turn(self):
        return not any([self.SPACE in row for row in self.board])

    def available_spaces(self):
        # list of tuples (x, y)
        slots = []
        for x in range(3):
            for y in range(3):
                if self.board[self.visual_y_location(y)][x] == self.SPACE:
                    slots.append((x,y))
        return slots


def valid_coordinate(value):
    valid = False
    try:
        coord = int(value)
        valid = coord in range(3)
    except ValueError:
        pass
    return valid


def prompt_for_y_coordinate():
    return prompt_for_coordinate("y")


def prompt_for_x_coordinate():
    return prompt_for_coordinate("x")


def prompt_for_coordinate(axis):
    return input(f"Enter {axis} coordinate (0, 1 or 2)... ").strip()


def prompt_for_coordinates():
    x_coordinate = prompt_for_x_coordinate()
    while not valid_coordinate(x_coordinate):
        x_coordinate = prompt_for_x_coordinate()

    y_coordinate = prompt_for_y_coordinate()
    while not valid_coordinate(y_coordinate):
        y_coordinate = prompt_for_y_coordinate()

    return int(x_coordinate), int(y_coordinate)


def main():
    print("Welcome to this game of Tic-Tac-Toe!")
    player_one = HumanPlayer(input("Name of player one: ").strip(), NOUGHT)
    player_two = AIPlayer("COMPUTER", CROSS)

    game = Game(player_one, player_two)

    while game.winner is None:
        print(f"\n{game.current_player} to play...")
        print(game)

        # # human specific
        # if type(game.current_player) == HumanPlayer:
        #     x_coordinate, y_coordinate = prompt_for_coordinates()
        #     while not game.valid_play(x_coordinate, y_coordinate):
        #         print(f"({x_coordinate}, {y_coordinate}) spot already taken!")
        #         x_coordinate, y_coordinate = prompt_for_coordinates()
        # else:
        #     # do some AI logic; random available slot
        #     available_spaces = game.available_spaces()
        #     x_coordinate, y_coordinate = random.choice(available_spaces)

        game.play_turn(x_coordinate, y_coordinate)
        game.current_player.play_turn
        print(game.available_spaces())

    print(game)
    if game.winner is True:
        print(f"\n{game.current_player} wins!")
    elif game.winner is False:
        print("\nNo spaces left - the game is a draw!")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
