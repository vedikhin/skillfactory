from consts import Consts
from player import Player, HumanPlayer, ComputerPlayer


class PlayerFactory:
    HUMAN_PLAYER = 1
    COMPUTER_PLAYER = 2

    def create(self, player_type: int, player_symbol: str) -> Player:
        if player_symbol != Consts.PLAYER1 and player_symbol != Consts.PLAYER2:
            print("ОШИБКА! Данный символ игрока не поддерживается!")
            return None
        elif player_type == PlayerFactory.HUMAN_PLAYER:
            return HumanPlayer(player_symbol)
        elif player_type == PlayerFactory.COMPUTER_PLAYER:
            return ComputerPlayer(player_symbol)
        else:
            print("ОШИБКА! Данный тип игрока не поддерживается!")
            return None
