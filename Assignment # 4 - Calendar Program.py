#------------------------------------------------------------------------------------
# Assignment #4: Calendar Program
# Author: Erik Floyd
# Date: April 5th 2020
# Description: The User enters the amount of days in a month and what day the month
#              starts on. The program then checks to make sure the values are valid
#              and finally it prints the calendar for the user.
# Input: User inputs a number that must be between 30 and 31, this is verified by the
#        program. The user must also input a day of the week in short format, this can
#        be inputted as a lower or upper case string.
#--------------------------------------------------------------------------------------
#import the system module
import sys
#Declares variables that will be used in the rest of the program (Globally)
daysInMonth = 0
dayToStart = 0
startDay = ''
 
 
#Main function calls all the other functions necessary to run the program and keep things organized
def main():
    #print("Running main")
    getInputs()
    checkValues()
    printFunction()
    sys.exit()
 
def getInputs():
    #Use the global Variables
    global daysInMonth
    global startDay
    #Collect the data from the user, both the amount of days in the month and the first day of the month. 
    daysInMonth = int(input('Days in the month: '))
    startDay = input('\nThe first day of the month is a,\nEnter Sun, Mon, Tue, Wed, Thu, Fri or Sat: ').lower()
 
    #DEBUG STUFF
    #print('\n','This was your input',daysInMonth, startDay,'\n')
 
#This function checks to make sure the values the user entered are valid
#The function also assigns a value between 1 to 7, to a day of the week (sun, mon etc)
def checkValues():
    #Make sure that we use the variables already declared elsewhere that store data we need
    global daysInMonth
    global dayToStart
    global startDay
 
    #Checks to make sure the values are valid this means both the day to start and the the amount of days in the month
    if (((daysInMonth < 30) or (daysInMonth > 31)) or (startDay not in ('sun','mon','tue','wed','thu','fri','sat'))):
        print("BAD INPUT")
        print('Please Try again!')
        main()
    elif (((daysInMonth == 30) or (daysInMonth == 31)) and (startDay in ('sun','mon','tue','wed','thu','fri','sat'))):
        print('You entered a valid input. Printing calendar')
    else:
        print('terminal error')
        sys.exit()
    
    #We need to convert the numbers to their assignment as days in the week (int's) so that the program can
    #Calculate where it needs to start printing the days of the week and where to stop
    if startDay == 'sun':
        dayToStart = 1
    elif startDay == 'mon':
        dayToStart = 2
    elif startDay == 'tue':
        dayToStart = 3
    elif startDay == 'wed':
        dayToStart = 4
    elif startDay == 'thr':
        dayToStart = 5
    elif startDay == 'fri':
        dayToStart = 6
    elif startDay == 'sat':
        dayToStart = 7
 
 
def printFunction():   
    #Make sure that we use the variables already declared elsewhere that store data we need
    global dayToStart
    global daysInMonth
    #Variables only used in this function, used to count or temporarily store data 
    passDate = 0 
    daysPrinted = 0
    daysPrintedInWeek = 0
    stringSpaces = '    '
 
    #Print the template for the calendar Only once
    #3 Spaces for each day of the week + the Three Letters for dates
    print('\n   SUN   MON   TUE   WED   THR   FRI   SAT') 
    print('   ---------------------------------------') 
 
    #pass the days that don't have a date in the first week
    while passDate != (dayToStart - 1):
        print('      ', end ='')
        passDate += 1
    #Remove a day that we actually print the day it starts. ex. It is day 7 but we still need a number there
    dayToStart = dayToStart - 1
 
    #The main loop runs if the counter called daysPrinted does not get bigger than the actual days in the month you entered
    while (daysPrinted != daysInMonth):
        daysPrinted += 1
        #The if statement is for a formatting change.
        #This changes the number of spaces after you print a number to 3, because a number is now two characters
        if (daysPrinted == 10):
            stringSpaces = '   '
        
        #This code prints the days in the calendar format. 
        #The if statement first checks if your at the end of the week and are printing the last day
        #If you are not printing the last day of the week it continues to the else
        if (dayToStart + daysPrintedInWeek == 6):
            #Print the last day of the week, with the right amount of spaces for formating
            print(stringSpaces,daysPrinted, end ='')
            #Start the newline for the next week.
            print('\n')
            #Reset the variable (daysPrintedInWeek) that counts and waits if your at the end of the week
            #Reset the variable (dayToStart) this variable controls the first bit of formating to start on the right day
            #It also helps determine in the first line if you have reached the end of the week
            daysPrintedInWeek = 0
            dayToStart = 0
            
        else:
            #If you are printing a day in the middle of the calendar,
            #You add one to the counter that tracks days printed 
            #And then you print the number and the correct amount of spaces for formating
            daysPrintedInWeek += 1
            print(stringSpaces,daysPrinted, end ='')
 
 
main()
