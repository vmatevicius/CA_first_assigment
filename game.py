from game_helpers import introduction
from random import randint
import logging
import pyfiglet


logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

class Game:

    game_board = ["[ ]","[ ]","[ ]",
                  "[ ]","[ ]","[ ]",
                  "[ ]","[ ]","[ ]"]

    def __init__(self, player_one_name: str, player_two_name: str) -> None:
        try:
            self.assign_signs_to_players(player_one_name, player_two_name)
            self.__player_x: str = ""
            self.__player_o: str = ""
            logging.info(f"Game succesfully inicialized between players {player_one_name} and {player_two_name}!")
        except Exception as e:
            logging.error(f"Program raised an error: {e}")
    
    def show_board(self) -> None:

        # Shows the game board and numbers corresponding to each square
        print(self.game_board[0] + "|" + self.game_board[1] + "|" + self.game_board[2] + "      " +  "0|1|2")
        print(self.game_board[3] + "|" + self.game_board[4] + "|" + self.game_board[5] + "      " +  "3|4|5")
        print(self.game_board[6] + "|" + self.game_board[7] + "|" + self.game_board[8] + "      " +  "6|7|8")
    
    # Assigns signs to players randomly
    def assign_signs_to_players(self, player_one_name:str, player_two_name: str) -> None:
        
        print("Before starting the game")
        print("Players must choose between X and O signs")
        
        # If the random number is 1 then the player_one chooses first
        if randint(1,2) == 1:
            
            # Try to get correct input from user
            while True:
            
                # Get sign from player
                player_one_sign = input(f"{player_one_name} chooses: ").strip().upper()
                
                # Check if sign is valid
                if player_one_sign not in ["X", "O"]:
                    print("Must choose between X and O!!")
                    continue
                else:
                    # If input is correct break the loop
                    break
            
            # Assign what sign is left to the other player
            if player_one_sign == "X":
                self.player_x = player_one_name  
                print(f"{player_two_name} is left with O sign")
                self.player_o = player_two_name
                    
            else:
                self.player_o = player_one_name
                print(f"{player_two_name} is left with X sign")
                self.player_x = player_two_name
        
        # If random number is 2 then the player_two chooses first
        else:
            
            while True:
                
                player_two_sign = input(f"{player_two_name} chooses: ").strip().upper()
                    
                if player_two_sign not in ["X", "O"]:
                    print("Must choose between X and O!!")
                    continue
                else:
                    break
            
            if player_two_sign == "X":
                self.player_x = player_two_name
                print(f"{player_one_name} is left with O sign")
                self.player_o = player_one_name
                    
            else:
                self.player_o = player_two_name
                print(f"{player_one_name} is left with X sign")
                self.player_x = player_one_name
            
        print("\n")

    def get_location(self) -> int:
        
        while True:
            try:
                    
                # Ask first player for a location 
                location = int(input("Choose a valid location: "))
                
                # Check if user input is valid
                if location not in [0,1,2,3,4,5,6,7,8]:
                    print("Number must be between 0 and 8")
                    continue
                # Check if square in the board is empty and not occupied
                elif self.game_board[location] != "[ ]":
                    print("Choose only empty squares!!!")
                    continue
                else:
                    return location
            except Exception as e:
                logging.error(f"Error recieved : {e}")
                continue
        
    def start_match(self) -> None:
        
        max_turns = 9
        # Set turn counter to 0
        turns = 0
        
            # Show the board before the match
        self.show_board()

            # While turns does not = 9 or there is no winner, continue the match
        while True:
            
            # Ask first player for a location 
            print(f"{self.player_x} turn")
            location = self.get_location()

            self.game_board[location] = "[X]"
            turns += 1
            self.show_board()
                
            # Check if there is a winner
            if self.check_if_winner_exists():
                logging.info("Game succesfully ended with a winner")
                break
            
            # If turns = 9, stop the match and declare that there was no winner
            if turns == max_turns:
                winner = pyfiglet.figlet_format("No one won :( ", font = "big")
                print(winner)
                logging.info("Game succesfully ended without a winner")
                break

            # Ask second player for a location
            print(f"{self.player_o} turn")
            location = self.get_location()

            self.game_board[location] = "[O]"
            turns += 1
            self.show_board()
                
            if self.check_if_winner_exists():
                logging.info("Game succesfully ended with a winner")
                break
            
            if turns == max_turns:
                winner = pyfiglet.figlet_format("No one won :( ", font = "big")
                print(winner)
                logging.info("Game succesfully ended without a winner")
                break

    def check_if_winner_exists(self) -> bool:
        
        # Check all possible winning conditions, if any of them are met, declare the winner
        
        if self.game_board[0] == self.game_board[1] == self.game_board[2] != "[ ]":
            
            if self.game_board[0].replace('[','').replace(']','') == "X":
                winner = pyfiglet.figlet_format(f"{self.player_x} Wins!!" , font = "big")
                print(winner)
                
            else:
                winner = pyfiglet.figlet_format(f"{self.player_o} Wins!!" , font = "big")
                print(winner)
                
            return True
            
        elif self.game_board[3] == self.game_board[4] == self.game_board[5] != "[ ]":
            
            if self.game_board[3].replace('[','').replace(']','') == "X":
                winner = pyfiglet.figlet_format(f"{self.player_x} Wins!!" , font = "big")
                print(winner)
                
            else:
                winner = pyfiglet.figlet_format(f"{self.player_o} Wins!!" , font = "big")
                print(winner)
                
            return True
            
        elif self.game_board[6] == self.game_board[7] == self.game_board[8] != "[ ]":
            
            if self.game_board[6].replace('[','').replace(']','') == "X":
                winner = pyfiglet.figlet_format(f"{self.player_x} Wins!!" , font = "big")
                print(winner)
                
            else:
                winner = pyfiglet.figlet_format(f"{self.player_o} Wins!!" , font = "big")
                print(winner)
            return True
            
        elif self.game_board[0] == self.game_board[3] == self.game_board[6] != "[ ]":
            
            if self.game_board[0].replace('[','').replace(']','') == "X":
                winner = pyfiglet.figlet_format(f"{self.player_x} Wins!!" , font = "big")
                print(winner)
                
            else:
                winner = pyfiglet.figlet_format(f"{self.player_o} Wins!!" , font = "big")
                print(winner)
                
            return True
            
        elif self.game_board[1] == self.game_board[4] == self.game_board[7] != "[ ]":
            
            if self.game_board[1].replace('[','').replace(']','') == "X":
                winner = pyfiglet.figlet_format(f"{self.player_x} Wins!!" , font = "big")
                print(winner)
                
            else:
                winner = pyfiglet.figlet_format(f"{self.player_o} Wins!!" , font = "big")
                print(winner)
                
            return True
        
        elif self.game_board[2] == self.game_board[5] == self.game_board[8] != "[ ]":
            
            if self.game_board[2].replace('[','').replace(']','') == "X":
                winner = pyfiglet.figlet_format(f"{self.player_x} Wins!!" , font = "big")
                print(winner)
                
            else:
                winner = pyfiglet.figlet_format(f"{self.player_o} Wins!!" , font = "big")
                print(winner)
                
            return True
        
        elif self.game_board[0] == self.game_board[4] == self.game_board[8] != "[ ]":
            
            if self.game_board[0].replace('[','').replace(']','') == "X":
                winner = pyfiglet.figlet_format(f"{self.player_x} Wins!!" , font = "big")
                print(winner)
                
            else:
                winner = pyfiglet.figlet_format(f"{self.player_o} Wins!!" , font = "big")
                print(winner)
                
            return True
        
        elif self.game_board[2] == self.game_board[4] == self.game_board[6] != "[ ]":
            
            if self.game_board[2].replace('[','').replace(']','') == "X":
                winner = pyfiglet.figlet_format(f"{self.player_x} Wins!!" , font = "big")
                print(winner)
                
            else:
                winner = pyfiglet.figlet_format(f"{self.player_o} Wins!!" , font = "big")
                print(winner)
                
            return True
        
        return False
               
    def start_game(self) -> None:
        
        introduction()
        print(f"{self.player_x} is X and {self.player_o} is O")
        self.start_match()

game = Game("Mindaugas", "Vytautas")
game.start_game()