from __future__ import annotations


class GardenError(Exception):
    """Base exception for garden-related problems."""
    pass


class PlantError(GardenError):
    """Exception for plant-related problems."""
    pass


class WaterError(GardenError):
    """Exception for watering-related problems."""
    pass


class GardenManager:
    """Simple garden manager demonstrating robust error handling."""

    def __init__(self) -> None:
        """Initialize an empty garden."""
        self._plants: dict[str, dict[str, int]] = {}

    def add_plant(self, plant_name: str) -> None:
        """Add a plant to the garden or raise PlantError if invalid."""
        if plant_name.strip() == "":
            raise PlantError("Plant name cannot be empty!")
        if plant_name in self._plants:
            raise PlantError(f"Plant '{plant_name}' already exists!")
        self._plants[plant_name] = {"water": 5, "sun": 8}

    def open_watering_system(self) -> None:
        """Simulate opening the watering system."""
        print("Opening watering system")

    def close_watering_system(self) -> None:
        """Simulate closing the watering system."""
        print("Closing watering system (cleanup)")

    def water_all_plants(self, water_in_tank: int) -> None:
        """
        Water all plants with guaranteed cleanup.
        Raises WaterError if there is not enough water.
        """
        self.open_watering_system()
        try:
            if water_in_tank <= 0:
                raise WaterError("Not enough water in tank")

            for name in self._plants:
                print(f"Watering {name} - success")
                water_in_tank -= 1
                if water_in_tank < 0:
                    raise WaterError("Not enough water in tank")

        finally:
            self.close_watering_system()

    def check_plant_health(self, plant_name: str, water_level: int, sunlight_hours: int) -> str:
        """Validate plant health inputs and return a status string, raising errors if invalid."""
        if plant_name.strip() == "":
            raise ValueError("Plant name cannot be empty!")
        if plant_name not in self._plants:
            raise PlantError(f"Unknown plant: '{plant_name}'")

        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")

        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
        if sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours} is too high (max 12)")

        return f"{plant_name}: healthy (water: {water_level}, sun: {sunlight_hours})"


def test_garden_management() -> None:
    """Demonstrate all error-handling techniques together."""
    print("=== Garden Management System ===")
    manager = GardenManager()

    print("Adding plants to garden...")
    for name in ("tomato", "lettuce", ""):
        try:
            manager.add_plant(name)
            print(f"Added {name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    print("Watering plants...")
    try:
        manager.water_all_plants(water_in_tank=5)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("Checking plant health...")
    try:
        print(manager.check_plant_health("tomato", 5, 8))
    except (ValueError, PlantError) as e:
        print(f"Error checking tomato: {e}")

    try:
        print(manager.check_plant_health("lettuce", 15, 8))
    except (ValueError, PlantError) as e:
        print(f"Error checking lettuce: {e}")

    print("Testing error recovery...")
    try:
        manager.water_all_plants(water_in_tank=0)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
