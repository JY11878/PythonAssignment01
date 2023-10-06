#Define the main function where the logic of the program resides.
def main():
    # Prompt the user to enter a year to test.
    nyear = int(input("Which year you want to test?"))

    # Check if the year is divisible by 4 and either not divisible by 100 or divisible by 400.
    if (nyear % 4 == 0) and (nyear % 100 != 0 or nyear % 400 == 0):
        print("This year is a leap year!")
         #Otherwise, print that it's not a leap year.
    else:
        print("This year is NOT a leap year!")

# Call the main function to execute the program.
main()
