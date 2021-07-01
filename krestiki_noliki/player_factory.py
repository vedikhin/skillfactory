from player import Player, HumanPlayer, ComputerPlayer


class PlayerFactory:
    HUMAN_PLAYER = 1
    COMPUTER_PLAYER = 2

    def create(self, player_type: int) -> Player:
        if player_type == PlayerFactory.HUMAN_PLAYER:
            return HumanPlayer()
        elif player_type == PlayerFactory.COMPUTER_PLAYER:
            return ComputerPlayer()
        else:
            print("ОШИБКА! Данный тип игрока не поддерживается!")
            return None
