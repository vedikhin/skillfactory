from consts import Consts


class Field:
    def __init__(self):
        self.field = [[Consts.EMPTY for i in range(3)] for j in range(3)]
        self.victories = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
                          [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
                          [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]

    def __str__(self):
        result = "\n  0 1 2\n"
        for i in range(3):
            result += str(i) + ' ' + ' '.join(self.field[i]) + '\n'
        return result

    def __getitem__(self, i):
        return self.field[i]

    def get_winner(self):
        for victory in self.victories:
            symbols = [self.field[x][y] for x, y in victory]
            if symbols == [Consts.PLAYER1, Consts.PLAYER1, Consts.PLAYER1]:
                return Consts.PLAYER1
            elif symbols == [Consts.PLAYER2, Consts.PLAYER2, Consts.PLAYER2]:
                return Consts.PLAYER2
        return None

    def get_winner_if_next_turn(self, player_symbol: str, x: int, y: int):
        if x < 0 or x > 2 or y < 0 or y > 2:
            print("ОШИБКА! Неправильный индекс!")
            return None

        old_value = self.field[x][y]
        if old_value != Consts.EMPTY:
            print("ОШИБКА! Ячейка не пуста!")
            return None

        self.field[x][y] = player_symbol
        winner = self.get_winner()

        self.field[x][y] = old_value
        return winner
