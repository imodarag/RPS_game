
#Here is a simple rock paper scissor game for begginers to practice
#The challenge here is to find out the all the possible cases and address all thoese from this code


import random 
choices = ["r","p","s"]

while True:
    guess = random.choice(choices)
    user_guess=input("Rock, paper or scissors? (r/p/s):").lower()

    if user_guess=="r" or user_guess=="p" or user_guess=="s":

        if user_guess == "r" and guess == "s":
            print("You win!!! I guess: Sissor ✂️")
            
        elif user_guess == "p" and guess == "r":
            print("You win!!! I guess: 🪨")
            
        elif user_guess == "s" and guess == "p":
            print("You win!!! I guess: 📄")
        elif user_guess == guess:
            print("It's a draw!! Let's try again")
        else:
            if guess == "r":
                temp = "🪨"
                print("I won!!!!: I guess Rock"+ temp)
            elif guess == "p":
                temp = "📄"
                print("I won!!!!: I guess Paper"+ temp)
            else:
                temp = "✂️"
                print("I won!!!!: I guess Scissor"+ temp)
    else:
        print("Invalid Argument")



