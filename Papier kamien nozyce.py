import random

users_wins=0
computer_wins=0
print("Hello in Paper,Rock,Sicssors GAME")
options = ["rock", "paper", "scissors"]


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit.").lower()
    if user_input == "q":
        break
        
    if user_input not in ["rock","paper","scissors"]:
            continue
        
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2,
    computer_pick = options[random_number]
    print("Computer picked", computer_pick+".")
    
    if user_input == "rock" and computer_pick == "scissors":
       print("You are win!")
       users_wins += 1 
            
    elif user_input == "paper" and computer_pick == "rock":
       print("You are win!")
       users_wins += 1
       
    elif user_input == "sissors" and computer_pick == "paper":
       print("You are win!")
       users_wins += 1
    else:
         print("You are lose!")
         computer_wins += 1
       
    
print("You won", users_wins, "times.")     
print("The computer wons", computer_wins,"times.")  
print("Goodbye")
