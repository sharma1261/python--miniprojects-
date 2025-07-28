# Random Multiplication Table Game

import random 
value = random.randint(1, 10)  
print("Welcome to the Random Multiplication Table Game!")


number =random.randint(1,10)


result =number*value
score =0
negative_marks =0


range=int(input("Select the range in which you want to play the game : "))

choice="yes"
while choice=="yes":

    
    while score <5:
        value = random.randint(1, 10)  

        number =random.randint(1,range)
        result =number*value
        print("what is the answer of : ",number,"*",value,"?")

        user_output = int(input("Enter your answer: "))

        if user_output==result:
            print("Correct Answer!")

            score += 1
        else:
            print("Wrong Answer! The correct answer is:", result)
            negative_marks += 1


        if negative_marks==3:
            print("You have lost the game due to 3 wrong answers.")
            choice = "no"
            break

        if score<5:
            choice="yes"

        if score==5:
            print("You have scored 5 points! You win!")
    
        break