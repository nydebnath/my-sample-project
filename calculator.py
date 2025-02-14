def add(num1, num2):
    """Returns the sum of two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The sum of num1 and num2.
    """
    return num1 + num2

def subtract(num1, num2):
    """Returns the difference between two numbers.

    Args:
        num1 (float): The number from which to subtract.
        num2 (float): The number to subtract from num1.

    Returns:
        float: The result of num1 minus num2.
    """
    return num1 - num2

def multiply(num1, num2):
    """Returns the product of two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The product of num1 and num2.
    """
    return num1 * num2

def divide(num1, num2):
    """Returns the quotient of two numbers.

    Args:
        num1 (float): The numerator.
        num2 (float): The denominator.

    Returns:
        float or str: The result of num1 divided by num2, or an error message if 
                      division by zero is attempted.
    """
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero is not allowed."

# Test the calculator functions
# Output the result of adding 5 and 3
print(add(5, 3))  # Expected output: 8

# Output the result of subtracting 4 from 10
print(subtract(10, 4))  # Expected output: 6

# Output the result of multiplying 6 by 2
print(multiply(6, 2))  # Expected output: 12

# Output the result of dividing 8 by 2
print(divide(8, 2))  # Expected output: 4.0