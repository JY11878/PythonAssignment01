# Define the constant value of pi.
pi = 3.14
# Define a function to calculate the area of a circle.
def circle():
    # Prompt the user to input the radius of the circle.
    r = eval(input("What is the radius?(in cm)"))
    # Calculate the area using the formula: pi * r^2.
    acircle = float(pi * r * r)
    # Display the calculated area to the user.
    print("The area of this circle is", acircle, "cm^2")
# Define a function to calculate the surface area of a cube.
def cube():
    # Prompt the user to input the side length of the cube.
    a = eval(input("What is the length?(in cm)"))
    # Calculate the surface area using the formula: 6 * a^2.
    acube = float(6 * a * a)
    # Display the calculated surface area to the user.
    print("The area of this cube is", acube, "cm^2")
# Define a function to calculate the surface area of a cylinder.
def cylinder():
    # Prompt the user to input the radius of the cylinder.
    r = eval(input("What is the radius?(in cm)"))
    # Prompt the user to input the height of the cylinder.
    h = eval(input("What is the height?(in cm)"))
    # Calculate the surface area using the formula: 2 * pi * r * h + 2 * pi * r^2.
    acylinder = float((2 * pi * r * h) + (2 * pi * r * r))
    # Display the calculated surface area to the user.
    print("The area of this cylinder is", acylinder, "cm^2")
# Define a function to calculate the surface area of a sphere.
def sphere():
    # Prompt the user to input the radius of the sphere.
    r = eval(input("What is the radius?(in cm)"))
    # Calculate the surface area using the formula: 4 * pi * r^2.
    asphere = float(4 * pi * r * r)
    # Display the calculated surface area to the user.
    print("The area of this sphere is", asphere, "cm^2")
# List out the available shape options to the user.
print("circle, cube, cylinder, sphere")
# Ask the user to specify which shape they want to calculate the surface area for.
type = input("What kind of shape you want to calculate?")
# Based on the user's choice, call the appropriate function to perform the calculations.
if type == "circle":
    circle()
elif type == "cube":
    cube()
elif type == "cylinder":
    cylinder()
elif type == "sphere":
    sphere()

