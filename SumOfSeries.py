#This is our main function where the primary logic of the program resides.
def main():
    #Declaring 'z' as a global variable so we can use the global instance of it.
    global z
    #Taking an input from the user and converting it to an integer.
    x = int(input("Please enter the number: "))
    #Initializing a variable 'y' with a value of 0.
    y = 0
    #Using a while loop to sum the squares of numbers from 1 to x.
    while x > y:
        #Incrementing 'y' by 1 in each iteration.
        y = y + 1
        #Updating the value of 'z' by adding the square of 'y'.
        z = z + y * y
    #Printing the final sum stored in 'z'.
    print("the sum of series is", z)
#Initializing a global variable 'z' with a value of 0.
z = 0
#Calling the main function to execute the program.
main()
