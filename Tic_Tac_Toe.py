from game_helpers import show_board, introduction

# initialize names for players
# create a board for the game
# at the start of the game initialize the board
# let the user choose whether he wants to be X or O
# make a function thats asks user where he wants to put X or O, then checks if the spot is empty,if empty put the sign in the spot if not asks for the input again
# then after 3 moves are made the program starts checking if 3 signs connect Vertically/Horizontally/Diagonally if not asks the user for the input again if yes then return the winner
# When 9 moves are made and there is no winner programs shuts and declares draw between opponents

class Game:

    def __init__(self, player_one_name: str, player_two_name: str):
        self.player_one: str = player_one_name
        self.player_two: str = player_two_name
        
    def assign_signs_to_players(self) -> str:
        print("Players must choose between X and O signs")
        player_one_sign = input(f"{self.player_one} chooses: ").strip().upper
        player_two_sign = ""
        if player_one_sign == "X":
            print(f"{self.player_two} is left with O sign")
            player_two_sign == "O"
            return player_one_sign, player_two_sign
        print(f"{self.player_two} is left with X sign")
        player_two_sign == "X"
        return player_one_sign, player_two_sign 