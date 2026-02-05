def garden_operations():
    print("\nTesting ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print("\nTesting ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    print("\nTesting FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: file does not exist")

    print("\nTesting KeyError...")
    try:
        plants = {"tomato": 5,"women": 67}
        print(plants["lettuce"])
    except KeyError:
        print("Caught KeyError: missing plant")

def test_error_types():
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("\nTesting multiple errors together...")
    try:
        int("abc")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")

if __name__ == "__main__":
    test_error_types()
