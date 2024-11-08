# The len() function returns the number of items in an object (like a list, string, tuple, etc.)
# Example: Finding the length of a list using len()
my_list = [10, 20, 30, 40]
print("Length of my_list:", len(my_list))

# Function greet(name): This function takes a person's name as input and prints a greeting message.
def greet(name="Sree"):
    print(f"Hello, {name}!")

# Call the function
greet("Sree")


# Function find_maximum(numbers): This function takes a list of integers and returns the maximum value.
# It does not use the built-in max() function but uses a loop to find the max.
def find_maximum(numbers):
    # Assume the first number is the largest for now
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

# Example usage
numbers = [3, 5, 9, 2, 8]
print("Maximum value:", find_maximum(numbers)) 

# Local and Global Variables Explanation:
# A global variable is defined outside any function and can be accessed anywhere in the code.
# A local variable is defined inside a function and can only be accessed within that function.
# If a global and a local variable have the same name, the function uses the local variable.

x = 10  # This is a global variable

def example():
    x = 5  # This is a local variable with the same name as the global variable
    print("Local x:", x)  # Prints the local variable value (5)

example()
# Function definition
def calculate_area(length, width=5):
    return length * width

# 1: Providing both length and width
print("Area with length 10 and width 7:", calculate_area(10, 7))  


# Testing the calculate_area function
print("Area with length 10 and width 7:", calculate_area(10, 7))
print("Area with only length 10:", calculate_area(10))
