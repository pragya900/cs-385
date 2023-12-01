def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("Division successful.")
    finally:
        print("This block always executes, whether there's an exception or not.")

# Example usage
if __name__ == "__main__":
    try:
        # Example 1: Divide numbers
        divide_numbers(10, 2)

        print("\n")

        # Example 2: Attempt to divide by zero
        divide_numbers(5, 0)

        print("\n")

        # Example 3: Attempt to divide incompatible types
        divide_numbers(8, "2")

    except Exception as e:
        print(f"Caught an exception in the main block: {e}")
