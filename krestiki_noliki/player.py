from consts import Consts
from field import Field


class Player:
    def __init__(self, player_symbol: str):
        self.player_symbol = player_symbol
        self.opponent_symbol = Consts.PLAYER1 if player_symbol == Consts.PLAYER2 else Consts.PLAYER2

    def next_turn(self, field: Field) -> (int, int):
        pass


class HumanPlayer(Player):
    def __init__(self, player_symbol: str):
        super(HumanPlayer, self).__init__(player_symbol)

    def next_turn(self, field: Field) -> (int, int):
        while True:
            coordinates = input(f"Ход игрока {self.player_symbol} (координаты по вертикали и через пробел координаты "
                                f"по горизонтали): ").split();

            if len(coordinates) != 2:
                print("ОШИБКА! Должно быть две координаты!")
                continue

            if not coordinates[0].isdigit() or not coordinates[1].isdigit():
                print("ОШИБКА! Координаты должны быть числами!")
                continue

            x, y = map(int, coordinates)
            if x < 0 or x > 2 or y < 0 or y > 2:
                print("ОШИБКА! Координаты должны быть в диапазоне 0-2!")
                continue

            if field[x][y] != Consts.EMPTY:
                print("ОШИБКА! Ячейка не пустая!")
                continue

            return x, y


class ComputerPlayer(Player):
    def __init__(self, player_symbol: str):
        super(ComputerPlayer, self).__init__(player_symbol)

        self.turn_priorities = {(0, 0): 1, (0, 1): 6, (0, 2): 2,
                                (1, 0): 5, (1, 1): 0, (1, 2): 7,
                                (2, 0): 4, (2, 1): 8, (2, 2): 3}

    def next_turn(self, field: Field) -> (int, int):
        result_x, result_y, result_priority = None, None, None

        for x in range(3):
            for y in range(3):
                if field[x][y] == Consts.EMPTY:
                    if field.get_winner_if_next_turn(self.player_symbol, x, y) == self.player_symbol:
                        return x, y
                    elif field.get_winner_if_next_turn(self.opponent_symbol, x, y) == self.opponent_symbol:
                        result_x, result_y, result_priority = x, y, -1  # we need to prevent the opponent from winning
                    elif result_priority is None:
                        result_x, result_y, result_priority = x, y, self.turn_priorities[(x, y)]
                    elif result_priority > self.turn_priorities[(x, y)]:
                        result_x, result_y, result_priority = x, y, self.turn_priorities[(x, y)]

        print(f"Ход игрока {self.player_symbol}: {x} {y}")
        return result_x, result_y
