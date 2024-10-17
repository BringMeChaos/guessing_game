## try to write a program that palyes a guessing game
## using binary search, a randint() in a while loop

#==============================================
# Current issues and todo:
# line 54, in the checker loop, the number of guesses is not incrementing, 
# I think that's because we go in and out of the loop and the function so the number of tries keeps re-setting.
#
# Cleen up the code with meaningfull comments
#
# choose how to name x, n, and other passable variables.
#
# check how to edit a variable name in multiple (all) places at once 
#
# When user guessed the number and chooses to quit, need to quit properly, it doesnt work rn
#==============================================

from random import *

def guessingGame():
    print("Hey there! This is a guessing game!\nThe game is between 1 and 100. \nYou can let the PC guess your number, or you can guess a number!")
    user_chooses_game_mode()


#=================================================
#  defining game modes:
#=================================================

def gameMode1():
    # Game mode 1, user guesses the number!
    pcNumberToGuess = randint(1, 100) #Called x when passed to functions
    userGuessInit = 0 #re-setting guess to 0

    #calling func to loop thru the user guessing the number while passing the randint():
    userGuessingLoop(userGuessInit,pcNumberToGuess)

#=================================================
#  defining victory text for user
#=================================================

def userGussedNumber():
    print("#######################\nYou guessed it! Nice job!\n#######################\n")
    while True:
        try:
            userQuitOrContinue = int(input("What would you like to do?\n 1) continue to main menu?\n 2) quit the game?\n"))
        except ValueError:
            print("Choise has to be 1 or 2, please try again.")
        else:
            if(userQuitOrContinue == 1):
                guessingGame()
            if(userQuitOrContinue == 2):
                print("Quitting the game, Goodbye.")
                exit()


        

#=================================================
#  defining user input guessing loop
#=================================================

def userGuessingLoop(userGuess, x):
    while True:
        userGuess = 0
        print("Try to guess what number the PC has choosen!")
        try:
            userGuess = int(input("What is your guess?\n")) # is called n when passing to functions
        except ValueError:
            print("your guess must be a number, please type an integer.")
        else:
            if (userGuess > 100 or userGuess < 1):
                print("Number must be between 1 and 100 (including both). \n please try again\n")
            else:
                # input is a number, lets check if user guessed it!
                if guessCheker(userGuess, x):
                    # guessCheker is reaturning True or False, 
                    # only if we recieve a True, the code will continue to the next function userGussedNumber()
                    # when guessCheker gets False we continue the while loop
                    userGussedNumber()


# This function is the lpgic for the guessing loop. 
# it recieves n as the user input guess, and x is the random number the script choose.
def guessCheker(n, x):
    
    numOfTrys = 0

    if (x == n):
        print(f"Number of tries is: {numOfTrys}")
        return True
    else:
        if (x > n):
            print("nope, the number  is higher!")
            numOfTrys=+1
            ######## testing ########
            print(f"Num of Tries is: {numOfTrys}")
            ######## testing ########
            return False
            # userGuessingLoop(n,x) no need to call guessing loop again, since we return False
        if(x < n):
            print("nope, the number is smaller!")
            # print("The PC's number is: ",x)
            # print("Your guess is:", n)
            numOfTrys=+1
            return False
            # userGuessingLoop(n,x) no need to call guessing loop again, since we return False

    #if (x == n), broke of the while loop.
    ## add number of tries
    # print("You guessed it! Nice job!")


#=================================================
#  end of defining game modes.
#=================================================




#=================================================
#  user chooses game mode
#=================================================

def user_chooses_game_mode():
    # while loop to get correct user input:
    while True:
        try:
            typeOfGame = int(input("Do you want to\n 1) Guess the number? or\n 2) Let the PC guess your number?\n"))
        except ValueError or UnboundLocalError:
            print("Please type 1 or 2 to choose a game mode.")
        ## else? let's see what else can we catch before the ifs
        else: 
            if (typeOfGame > 2 or typeOfGame < 1):
                print("Please type 1 or 2 to choose a game mode.")
            else:
                break

    if (typeOfGame == 1):
        # Game mode 1, user guesses the number!
        print("Game mode 1 is choosen! Can you guess the number??")

        gameMode1() 

    if (typeOfGame == 2):
        # Game mode 2, user guesses the number!
        print("Game mode 2 is choosen! will you guess the PC's number??")

        #gameMode2()
       


if __name__ == "__main__":
    guessingGame()

    
    

