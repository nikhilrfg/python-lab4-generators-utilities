
# Task 2: Multiplier Closure

# Outer function
def make_multiplier(factor):

    # Inner function
    def multiply(x):
        return x * factor

    # Return the inner function
    return multiply


# Test the multiplier closure
if __name__ == "__main__":

    # Create multiplier functions
    times3 = make_multiplier(3)
    times10 = make_multiplier(10)

    # Test the functions
    print("Multiplier Closure Results:")

    print("7 multiplied by 3 = " + str(times3(7)))
    print("7 multiplied by 10 = " + str(times10(7)))
