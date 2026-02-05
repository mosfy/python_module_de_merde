def check_temperature(temp_str):
    try:
        temp_int = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return

    if temp_int < 0:
        print(f"Error: {temp_int}°C is too cold for plants (min 0°C)")
    elif temp_int > 40:
        print(f"Error: {temp_int}°C is too hot for plants (max 40°C)")
    else:
        print(f"Temperature {temp_int}°C is perfect for plants!")

def test_temperature_input():
    print("=== Garden Temperature Checker ===")

    tests = ["25", "abc", "100", "-50"]

    for value in tests:
        print(f"Testing temperature: {value}")
        check_temperature(value)
        print()

    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature_input()
