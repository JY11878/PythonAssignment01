#Prompt the user to enter a number for pattern generation.
number = int(input("Enter a number to generate its pattern = "))
#Outer loop: Iterates from 1 to the entered number (inclusive).
for x in range(1, number + 1):
    #Inner loop: Iterates from 1 to the current value of the outer loop (inclusive).
    for y in range(1, x + 1):
        # Print the current value of the inner loop followed by a space.
        print(y, end=" ")
    #After the inner loop finishes, print a new line to start a new row for the pattern.
    print()
