#Define the main function where the logic of the program resides.
def main():
    #Prompt the user to enter a year to test.
    nyear = int(input("Which year you want to test?"))
    #Calculate the remainder when the year is divided by 4.
    x = nyear % 4
    #Check if the year is divisible by 4.
    if x == 0:
        #If yes, print that it's a leap year.
        print("This year is a leap year!")
    else:
        #Otherwise, print that it's not a leap year.
        print("This year is NOT a leap year!")
#Call the main function to execute the program.
main()
