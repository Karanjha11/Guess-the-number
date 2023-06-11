import random
randnumber = random.randint(1,100)
userguess = None
guesses=0
   
while(userguess != randnumber):
    userguess = int(input("Enter your guess:"))
    guesses +=1
    if(userguess==randnumber):
        print("you guessed it right!")
    else:
        if(userguess>randnumber):
            print("you guessed it wrong! enter a smaller no.")
        else:
            print("you guessed it wrong! enter a larger no.")

    print(f"you guessed the number in {guesses} guesses")


