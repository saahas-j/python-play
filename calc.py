#python code to perform basic arithmetic operations
def add(x, y):
    """Return the sum of x and y."""
    return x + y    


def subtract(x, y):
    """Return the difference of x and y."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the quotient of x and y."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y


if __name__ == "__main__":
    # Example usage
    print("Addition:", add(5, 3))
    print("Subtraction:", subtract(5, 3))
    print("Multiplication:", multiply(5, 3))
    print("Division:", divide(5, 3))
   