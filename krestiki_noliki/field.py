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
        winner = None
        for victory in self.victories:
            for x, y in victory:
                if self.field[x][y] == Consts.EMPTY:
                    winner = None
                    break
                elif winner is None:
                    winner = self.field[x][y]
                elif winner != self.field[x][y]:
                    winner = None
                    break
            if winner is not None:
                return winner
        return None
