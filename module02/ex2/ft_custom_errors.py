class GardenError(Exception):
    """Base exception for garden-related problems."""
    pass


class PlantError(GardenError):
    """Exception for plant-related problems."""
    pass


class WaterError(GardenError):
    """Exception for watering-related problems."""
    pass


def test_plant_problem():
    raise PlantError("The tomato plant is wilting!")


def test_water_problem():
    raise WaterError("Not enough water in the tank!")


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        test_plant_problem()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("Testing WaterError...")
    try:
        test_water_problem()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("Testing catching all garden errors...")
    for test in (test_plant_problem, test_water_problem):
        try:
            test()
        except GardenError as e:
            print(f"Caught a garden error: {e}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
