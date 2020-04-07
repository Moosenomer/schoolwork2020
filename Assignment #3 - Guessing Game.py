#------------------------------------------------------------------------------------
# Assignment #3: Guessing Game
# Author: Erik Floyd
# Date: Mar 6th 2020
# Description: User tries to guess a Random number between 1 and 100, if the user
#              Gets the number in lower number of tries the user is rewarded with
#              a non generic answer that is motivational
# Input: User inputs a number that is within the 0 - 100 range, no other values will
#        work, you will get an error messaage. The user also inputs y or n when
#        asked if they want to play again, this value is made lower case.
#--------------------------------------------------------------------------------------
import random,sys

#Main function, stores and runs all the main code for the program.
def main():
    print('==================================================')
    print('TOTALLY SUPER GUESSING GAME BY ERIK FLOYD')

    #makes the counter variable to store the number of times the while loop repeats.
    counter = 0

    #Calculates the random number, and sets correctGuess to False when the program starts
    randomNumber = random.randint(1, 100)
    correctGuess = False

    #While your guess is wrong, this loops repeats
    while (correctGuess == False):
        counter += 1

        #Changes the user prompt depending on the number of guesses for polish
        if counter == 1:
            prompt = int(input('Make your first guess: '))
        else:
            prompt = int(input('Make your next guess: '))
            
        #Calls the getIntInput and sets the conditions so that it can execute
        #These values can be changes to make the game harder or easier.
        getIntInput(prompt, 0, 100)

        #If you guess the number it will decided bassed on the number of tries the message
        #to give you. Otherwise it evaluates if your guess was higher or lower than
        #the random number and returns a message to help you with your next guess
        if(passedGuess == randomNumber):
            if(counter == 1):
                print('You Guessed it first try! Must be a cheater')
                playagain()
            elif (counter >= 2) and (counter <= 6):
                print('Great Job! You Guessed the number in', counter, 'tries')
                playagain()
            elif (counter > 6) and (counter <= 9):
                print('You Guessed the number in', counter, 'tries')
                playagain()
            elif (counter > 9):
                print('You Guessed the number in', counter, 'tries, why so many?')
                playagain()
            passedGuess == True 
        elif(passedGuess < randomNumber):
            print('Too low, try again')
        elif(passedGuess > randomNumber):
            print('Too high, try again')
        else:
            print('Error occured, not sure how you did it but you broke something again!')
            print('Terminating Program')
            sys.exit()
        

#Determines if the number (prompt) the user enterd is valid and can
#be used or the program needs to exit, returns theb good value!
def getIntInput(prompt, low, high):
    global passedGuess
    
    if (prompt >= low ) and (prompt <= high):
        #print('Passed')
        passedGuess = prompt
        
    elif (prompt < low) or (prompt > high):
        #print('BAD VALUE')
        sys.exit()
        
    else:
        print('Thats not even a number, terminating program')
        sys.exit()
            
    return(passedGuess)

#Used at the end of the game to determine if the user wants to play again, 
#takes a input from the user, has to be y or n but capitilization does not matter
def playagain():
    playAgain = input('Do you want to play again? (Answer Must be y or n) : ').lower()
    if playAgain == 'y':
        print('Lets Play Again')
        print('')
        counter = 0
        inputCounter = 0
        main()
    elif playAgain == 'n':
        print('Thanks For playing!')
        sys.exit()
    else:
        print('Unknown Command, please try again!')
        playagain()

#Runs the main function        
main()
 
