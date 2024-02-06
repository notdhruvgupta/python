# Simple Python program to add two numbers

def add_numbers():
    # Get user input for the first number
    num1 = float(input("Enter the first number: "))
    
    # Get user input for the second number
    num2 = float(input("Enter the second number: "))
    
    # Perform the addition
    result = num1 + num2
    
    # Print the result
    print(f"The sum of {num1} and {num2} is: {result}")

# Call the function to run the program
add_numbers()
