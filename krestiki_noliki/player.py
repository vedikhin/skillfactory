from consts import Consts
from field import Field


class Player:
    def next_turn(self, field: Field) -> (int, int):
        pass


class HumanPlayer(Player):
    def next_turn(self, field: Field) -> (int, int):
        while True:
            coordinates = input("Ваш ход:").split();

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
    def next_turn(self, field: Field) -> (int, int):
        pass
