#------------------------------------------------------------------------------------
# Assignment #5 - Account Number Generator Validator
# Author: Erik Floyd
# Date: April 17th 2020
# Description: Program inputs 10 numbers from a text document, the first 5 are base numbers
#              that will have their verification number calculated and then verified if its
#              valid and can be used. The next 5 numbers have a verification number and must
#              be verified if the base number and verification number are valid.
# Input: A text document with 10 numbers that the program will use as inputs. User does
#        not have to enter anything.
#--------------------------------------------------------------------------------------
#Open the required files
accountData = open(r'input.txt', 'r')

#dedicated function for 
def splitNumbers(number): 
    return [char for char in number]

#The function to generate the base number
def baseNumberGenerator():
    #Counter to keep track of how many numbers have been processed
    firstfivenumbersCounter = 0
    #main loop that runs 5 times, for the first five numbers
    while firstfivenumbersCounter != 5:
        #import and then store the numbers as strings from the text document
        accountNumbersRaw = accountData.readline()

        #Remove the /n from the list so its only numbers (still strings)
        accountNumbersList = splitNumbers(accountNumbersRaw)
        accountNumbersList.remove('\n')

        #Join the numbers that have been separated into a list back into a string to be checked for a valid input
        checkNUMBERS = ''.join([str(elem) for elem in accountNumbersList])

        #Serparating the different use cases of the same list,
        #Final numbers used in the end, where reversed numbers used in the math portion
        finalNumbersList = accountNumbersList
        reversedNumbersList = accountNumbersList

        #List that stores the multiplication constant
        multiplyNumbers = [2,3,4,5,6,7,2,3,4,5,6,7,2,3,4,5,6,7,2,3,4,5,6,7]
        
        #reset the variables to zero before starting the loop
        numbersMultiplyTotal = 0
        indexNumber = 0

        #reverse the order of the list so that all the numbers are multiplied by the right constant
        reversedNumbersList.reverse()
        
        #Check to make sure that the number taken from the document only contains numbers, 
        #Otherwise it skips the math for that number and prints that its not valid
        if checkNUMBERS.isdigit() == False:
            print('Not a valid Input!')
            firstfivenumbersCounter += 1  
            continue
        #If the number is valid, calculate the sum of all the digits
        else:
            for numbers in reversedNumbersList:
                #index and use the number from the constant list to calculate the sums
                multiplyBy = multiplyNumbers[indexNumber]
                #The sum of the numbers is calculated by adding the result of multiplying the digits and constant 
                numbersMultiplyTotal += (int(reversedNumbersList[indexNumber]) * multiplyBy)
                #Counter to track how many digits have been calculated,
                #This helps us determine what constant and digit should be multiplied together
                indexNumber += 1
        
        #math to solve the find the verification number
        #First find the remainder from dividing the sum of the numbers divided by 11
        #Then find the verification number by subtracting 11 by the remainder
        remainder = numbersMultiplyTotal % 11
        verificationNumber = 11 - remainder

        #Logic to determine if the account number can be used and what the verification number should be
        if remainder == 1:
            print('NONE')
        elif remainder == 0:
            #set the verification number to be zero
            verificationNumber = 0
            #reverse the list back to its original order
            finalNumbersList.reverse()
            #add to the list in the final position the number 0
            finalNumbersList.append(0)
            #turn the list back into a string to be printed
            final = ''.join([str(elem) for elem in finalNumbersList])
            #print the final number
            print(final)
        else:
            #reverse the list back to its original order
            finalNumbersList.reverse()
            #add the verification number to the end of the original base number
            finalNumbersList.append(verificationNumber)
            #turn the list back into a string to be printed
            final = ''.join([str(elem) for elem in finalNumbersList])
            #print the final number
            print(final)

        #counter to stop the loop once the first five numbers have been calculated
        firstfivenumbersCounter += 1

def accountChecker():
    #Counter to keep track of how many numbers have been processed
    lastfivenumbersCounter = 0

    while lastfivenumbersCounter != 5:
        #import and then store the numbers as strings from the text document    
        accountNumbersRaw = accountData.readline()

        #Remove the /n from the list so its only numbers (still strings)
        accountNumbersList = splitNumbers(accountNumbersRaw)
        accountNumbersList.remove('\n')

        #Join the numbers that have been separated into a list back into a string to be checked for a valid input
        checkNUMBERS = ''.join([str(elem) for elem in accountNumbersList])
        
        #reset the account length after every loop
        #determine the account length based on the numbers in a list and store that information
        accountLength = 0
        accountLength = len(accountNumbersList)

        #reset the last number after every loop
        #determine the position of the last number to be referenced later
        lastNumber = 0
        lastNumber = accountLength - 1

        #determine and store the last number (verification number) to be verified later
        verificationNumberListed = accountNumbersList[lastNumber]

        #remove the last number in the account number list, leaving only the base number
        accountNumbersList.pop()

        #Serparating the different use cases of the same list,
        #reversed numbers used in the math portion
        reversedNumbersList = accountNumbersList

        #List that stores the multiplication constant
        multiplyNumbers = [2,3,4,5,6,7,2,3,4,5,6,7,2,3,4,5,6,7,2,3,4,5,6,7]
        
        #reset the variables to zero before starting the loop
        numbersMultiplyTotal = 0
        indexNumber = 0

        #reverse the list of numbers to multiply the numbers by the constant in the right order
        reversedNumbersList.reverse()

        #Check to make sure that the number taken from the text document only contains numbers, 
        #Otherwise it skips the math for that number and prints that its not valid
        if checkNUMBERS.isdigit() == False:
            print('NO')
            lastfivenumbersCounter += 1  
            continue
        #If the number is valid, calculate the sum of all the digits
        else:
            for numbers in reversedNumbersList:
                #index and use the number from the constant list to calculate the sums
                multiplyBy = multiplyNumbers[indexNumber]
                #The sum of the numbers is calculated by adding the result of multiplying the digits and constant
                numbersMultiplyTotal += (int(reversedNumbersList[indexNumber]) * multiplyBy)
                #Counter to track how many digits have been calculated,
                #This helps us determine what constant and digit should be multiplied together
                indexNumber += 1
        
        #math to solve the find the verification number
        #First find the remainder from dividing the sum of the numbers divided by 11
        #Then find the verification number by subtracting 11 by the remainder
        remainder = numbersMultiplyTotal % 11
        verificationNumber = 11 - remainder


        #Structure to check if the base number has a correct and properly assigned verification number
        if remainder == 1 and str(verificationNumber) == '10' and str(verificationNumberListed) == '1':
            print('NO')
        elif remainder == 0 and str(verificationNumberListed) == '0':
            print('YES')
        elif str(verificationNumber) == verificationNumberListed:
            print('YES')
        elif verificationNumber != verificationNumberListed:
            print('NO')
        else:
            print('YES')
        #counter to stop the loop once the last five numbers have been calculated
        lastfivenumbersCounter += 1   

#function to organize the main script all in one place
def main():
    #Run the first half of the program - The Generator
    baseNumberGenerator()
    print('\n')
    #Run the second half of the program - The Validator
    accountChecker()
    #Close the File
    accountData.close()
#Run the main function
main()