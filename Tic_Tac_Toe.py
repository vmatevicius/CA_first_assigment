from game_helpers import introduction
from random import randint
import logging
import pyfiglet


logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

class Game:

    GAME_STATUS = True
    
    game_board = ["[ ]","[ ]","[ ]",
                  "[ ]","[ ]","[ ]",
                  "[ ]","[ ]","[ ]"]

    def __init__(self, player_one_name: str, player_two_name: str) -> None:
        if type(player_one_name) and type(player_two_name) != str:
            logging.critical("Program raised type error because one or more inputs were not strings")
            raise TypeError("Name must be a string")
        self.player_one: str = player_one_name
        self.player_two: str = player_two_name
        self.player_one_sign: str = ""
        self.player_two_sign: str = ""
        logging.info(f"Game succesfully inicialized between players {self.player_one} and {self.player_two}!")
    
    def show_board(self) -> None:

        print(self.game_board[0] + "|" + self.game_board[1] + "|" + self.game_board[2] + "      " +  "0|1|2")
        print(self.game_board[3] + "|" + self.game_board[4] + "|" + self.game_board[5] + "      " +  "3|4|5")
        print(self.game_board[6] + "|" + self.game_board[7] + "|" + self.game_board[8] + "      " +  "6|7|8")
    
    def assign_signs_to_players(self) -> str:
        
        print("\n")
        print("Before starting the game")
        print("Players must choose between X and O signs")
        
        if randint(1,2) == 1:
            
            while True:
            
                self.player_one_sign = input(f"{self.player_one} chooses: ").strip().upper()
                
                if self.player_one_sign not in ["X", "O"]:
                    print("Must choose between X and O!!")
                    continue
                else:
                    break
                
            if self.player_one_sign == "X":   
                print(f"{self.player_two} is left with O sign")
                self.player_two_sign = "O"
                    
            else:
                print(f"{self.player_two} is left with X sign")
                self.player_two_sign = "X"

        else:
            
            while True:
                
                self.player_two_sign = input(f"{self.player_two} chooses: ").strip().upper()
                    
                if self.player_two_sign not in ["X", "O"]:
                    print("Must choose between X and O!!")
                    continue
                else:
                    break
                
            if self.player_two_sign == "X":
                print(f"{self.player_one} is left with O sign")
                self.player_one_sign = "O"
                    
            else:
                print(f"{self.player_one} is left with X sign")
                self.player_one_sign = "X"

        
    def start_match(self) -> None:
        
        turns = 0
        
        if self.player_one_sign == "X":
            
            self.show_board()

            while self.GAME_STATUS:
                
                location = int(input(f"{self.player_one} turn, choose a valid location: "))
                
                if location not in [0,1,2,3,4,5,6,7,8]:
                    print("Number must be between 0 and 8")
                    continue
                
                elif self.game_board[location] != "[ ]":
                    print("Choose only empty squares!!!")
                    continue
                
                else:
                    self.game_board[location] = "[X]"
                    turns += 1
                    self.show_board()
                    
                    if self.check_if_winner_exists():
                        logging.info("Game succesfully ended with a winner")
                        break
                    
                    if turns == 9:
                        print("No one won!")
                        self.GAME_STATUS = False
                        logging.info("Game succesfully ended without a winner")
                    
                location = int(input(f"{self.player_two} turn, choose a valid location: "))
                
                if location not in [0,1,2,3,4,5,6,7,8]:
                    print("Number must be between 0 and 8")
                    continue
                
                elif self.game_board[location] != "[ ]":
                    print("Choose only empty squares!!!")
                    continue
                
                else:
                    self.game_board[location] = "[O]"
                    turns += 1
                    self.show_board()
                    
                    if self.check_if_winner_exists():
                        logging.info("Game succesfully ended with a winner")
                        break
                    
                    if turns == 9:
                        print("No one won!")
                        self.GAME_STATUS = False
                        logging.info("Game succesfully ended without a winner")
        else:
            
            self.show_board()
            
            while self.GAME_STATUS:

                location = int(input(f"{self.player_two} turn, choose a valid location: "))
                
                if location not in [0,1,2,3,4,5,6,7,8]:
                    print("Number must be between 0 and 8")
                    continue
                
                elif self.game_board[location] != "[ ]":
                    print("Choose only empty squares!!!")
                    continue
                
                else:
                    self.game_board[location] = "[X]"
                    turns += 1
                    self.show_board()
                    
                    if self.check_if_winner_exists():
                        logging.info("Game succesfully ended with a winner")
                        break
                    
                    if turns == 9:
                        print("No one won!")
                        self.GAME_STATUS = False
                        logging.info("Game succesfully ended without a winner")
                    
                location = int(input(f"{self.player_one} turn, choose a valid location: "))
                
                if location not in [0,1,2,3,4,5,6,7,8]: 
                    print("Number must be between 0 and 8")
                    continue
                
                elif self.game_board[location] != "[ ]":
                    print("Choose only empty squares!!!")
                    continue
                
                else:
                    self.game_board[location] = "[O]"
                    turns += 1
                    self.show_board()
                    
                    if self.check_if_winner_exists():
                        logging.info("Game succesfully ended with a winner")
                        break
                    
                    if turns == 9:  
                        print("No one won!")
                        self.GAME_STATUS = False
                        logging.info("Game succesfully ended without a winner")
                
    def check_if_winner_exists(self) -> bool:
        
        if self.game_board[0] == self.game_board[1] == self.game_board[2] != "[ ]":
            
            if self.game_board[0].replace('[','').replace(']','') == self.player_one_sign:
                winner = pyfiglet.figlet_format(f"{self.player_one} Wins!!" , font = "big")
                print(winner)
                
            else:
                winner = pyfiglet.figlet_format(f"{self.player_two} Wins!!" , font = "big")
                print(winner)
                
            return True
            
        elif self.game_board[3] == self.game_board[4] == self.game_board[5] != "[ ]":
            
            if self.game_board[3].replace('[','').replace(']','') == self.player_one_sign:
                winner = pyfiglet.figlet_format(f"{self.player_one} Wins!!" , font = "big")
                print(winner)
                
            else:
                winner = pyfiglet.figlet_format(f"{self.player_two} Wins!!" , font = "big")
                print(winner)
                
            return True
            
        elif self.game_board[6] == self.game_board[7] == self.game_board[8] != "[ ]":
            
            if self.game_board[6].replace('[','').replace(']','') == self.player_one_sign:
                winner = pyfiglet.figlet_format(f"{self.player_one} Wins!!" , font = "big")
                print(winner)
                
            else:
                winner = pyfiglet.figlet_format(f"{self.player_two} Wins!!" , font = "big")
                print(winner)
            return True
            
        elif self.game_board[0] == self.game_board[3] == self.game_board[6] != "[ ]":
            
            if self.game_board[0].replace('[','').replace(']','') == self.player_one_sign:
                winner = pyfiglet.figlet_format(f"{self.player_one} Wins!!" , font = "big")
                print(winner)
                
            else:
                winner = pyfiglet.figlet_format(f"{self.player_two} Wins!!" , font = "big")
                print(winner)
                
            return True
            
        elif self.game_board[1] == self.game_board[4] == self.game_board[7] != "[ ]":
            
            if self.game_board[1].replace('[','').replace(']','') == self.player_one_sign:
                winner = pyfiglet.figlet_format(f"{self.player_one} Wins!!" , font = "big")
                print(winner)
                
            else:
                winner = pyfiglet.figlet_format(f"{self.player_two} Wins!!" , font = "big")
                print(winner)
                
            return True
        
        elif self.game_board[2] == self.game_board[5] == self.game_board[8] != "[ ]":
            
            if self.game_board[2].replace('[','').replace(']','') == self.player_one_sign:
                winner = pyfiglet.figlet_format(f"{self.player_one} Wins!!" , font = "big")
                print(winner)
                
            else:
                winner = pyfiglet.figlet_format(f"{self.player_two} Wins!!" , font = "big")
                print(winner)
                
            return True
        
        elif self.game_board[0] == self.game_board[4] == self.game_board[8] != "[ ]":
            
            if self.game_board[0].replace('[','').replace(']','') == self.player_one_sign:
                winner = pyfiglet.figlet_format(f"{self.player_one} Wins!!" , font = "big")
                print(winner)
                
            else:
                winner = pyfiglet.figlet_format(f"{self.player_two} Wins!!" , font = "big")
                print(winner)
                
            return True
        
        elif self.game_board[2] == self.game_board[4] == self.game_board[6] != "[ ]":
            
            if self.game_board[2].replace('[','').replace(']','') == self.player_one_sign:
                winner = pyfiglet.figlet_format(f"{self.player_one} Wins!!" , font = "big")
                print(winner)
                
            else:
                winner = pyfiglet.figlet_format(f"{self.player_two} Wins!!" , font = "big")
                print(winner)
                
            return True
               
    def start_game(self) -> None:
          
        introduction()
        self.show_board()
        self.assign_signs_to_players()
        print(f"{self.player_one} is {self.player_one_sign} and {self.player_two} is {self.player_two_sign}")
        self.start_match()