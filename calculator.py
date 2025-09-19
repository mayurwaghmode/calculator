# calculator.py

def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def main():
    print("Welcome to the Collaborative Calculator!")
    print("Currently, only the ADD operation is available.")
    print("---------------------------------------------")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    result = add(num1, num2)
    print(f"Result of addition: {result}")

    # Future operations:
    # def subtract(a, b): pass
    # def multiply(a, b): pass
    # def divide(a, b): pass
    # Contributors are welcome to implement these!

if __name__ == "__main__":
    main()

