
# Task 1: Fibonacci Generator

# Generator function to produce Fibonacci numbers
def gen_fibonacci(n):

    # Initialize the first two Fibonacci numbers
    a = 0
    b = 1

    # Generate the first n Fibonacci numbers
    for i in range(n):

        # Return the current Fibonacci number
        yield a

        # Calculate the next Fibonacci numbers
        a, b = b, a + b


# Test the Fibonacci generator
if __name__ == "__main__":

    n = 10

    print("First " + str(n) + " Fibonacci Numbers:")

    for number in gen_fibonacci(n):
        print("Fibonacci Number: " + str(number))
