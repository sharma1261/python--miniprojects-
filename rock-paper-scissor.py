# rock paper scissor game 
import random

choice = "yes"
user_count = 0
comp_count = 0

while choice == "yes":
    user_inp = input("Enter your option (rock/paper/scissor): ").lower()
    computer_values = ["rock", "paper", "scissor"]
    comp_choice = random.choice(computer_values)

    print("Computer chooses:", comp_choice)

    if user_inp == comp_choice:
        print("It's a draw! Choose again.")
    
    elif user_inp == "rock":
        if comp_choice == "scissor":
            user_count += 1
            print("You win! Your score is:", user_count)
        else:
            comp_count += 1
            print("Computer wins! Computer's score is:", comp_count)

    elif user_inp == "paper":
        if comp_choice == "rock":
            user_count += 1
            print("You win! Your score is:", user_count)
        else:
            comp_count += 1
            print("Computer wins! Computer's score is:", comp_count)

    elif user_inp == "scissor":
        if comp_choice == "paper":
            user_count += 1
            print("You win! Your score is:", user_count)
        else:
            comp_count += 1
            print("Computer wins! Computer's score is:", comp_count)

    else:
        print("Invalid input. Please choose rock, paper, or scissor.")
        continue

    # Check for game-ending condition
    if user_count == 5:
        print("\n Game Over! You Win!")
        print("Final Score -> You:", user_count, "| Computer:", comp_count)
        break
    elif comp_count == 5:
        print("\n Game Over! Computer Wins!")
        print("Final Score -> Computer:", comp_count, "| You:", user_count)
        break

    choice = input("Do you want to play again (yes/no)? ").lower()

print("Thanks for playing the game with me! ")
