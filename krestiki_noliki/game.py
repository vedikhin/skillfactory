from consts import Consts
from field import Field
from player import Player
from player_factory import PlayerFactory


class Game:
    def __init__(self, field: Field, player_factory: PlayerFactory):
        self.players = [(i, self.__make_player(i, player_factory)) for i in [Consts.PLAYER1, Consts.PLAYER2]]
        self.field = field

    @staticmethod
    def __make_player(player_symbol: str, player_factory: PlayerFactory) -> Player:
        while True:
            player_type = input(f"Введите тип игрока, играющего за {player_symbol} ({PlayerFactory.HUMAN_PLAYER} - "
                                f"человек, {PlayerFactory.COMPUTER_PLAYER} - компьютер): ")

            if player_type == str(PlayerFactory.HUMAN_PLAYER):
                return player_factory.create(PlayerFactory.HUMAN_PLAYER, player_symbol)
            elif player_type == str(PlayerFactory.COMPUTER_PLAYER):
                return player_factory.create(PlayerFactory.COMPUTER_PLAYER, player_symbol)
            else:
                print(f"ОШИБКА! Введите {PlayerFactory.HUMAN_PLAYER} или {PlayerFactory.COMPUTER_PLAYER}!")
                continue

    def play(self) -> object:
        print(self.field)

        for i in range(9):
            player_symbol, player = self.players[i % 2]

            x, y = player.next_turn(self.field)
            self.field[x][y] = player_symbol
            print(self.field)

            winner = self.field.get_winner()
            if winner is not None:
                print(f"Поздравляем игрока {winner} с победой!")
                return

        print("Ничья!")
