class SecurePlant:
    """
    A secure version of a Plant that protects its internal data.

    This class ensures that plant attributes cannot be set
    to invalid values (negative height or age).
    Direct access to sensitive data is discouraged
    """

    def __init__(self, name):
        """
        Initialize a SecurePlant with a name.
        Height and age start at 0.
        """
        self.name = name
        self._height = 0
        self._day = 0

    def set_height(self, height):
        """
        Safely set the height of the plant.

        Args:
            height (int): New height value

        Prints an error if the value is invalid.
        """
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm [OK]")

    def set_age(self, day):
        """
        Safely set the age of the plant

        Args:
            age (int): New age value in days

        Prints an error if the value is invalid.
        """
        if day < 0:
            print(f"Invalid operation attempted: age {day} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._day = day
            print(f"Age updated: {self._day} days [OK]")

    def get_height(self):
        """
        Get the current height of the plant.

        Returns:
            int: Plant height
        """
        return self._height

    def get_age(self):
        """
        Get the current age of the plant.

        Returns:
            int: Plant age in days
        """
        return self._day

    def get_info(self):
        """
        Return current plant information.
        """
        return f"{self.name} ({self._height}cm, {self._day} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose")
    print("Plant created: Rose")

    plant.set_height(25)
    plant.set_age(30)

    plant.set_height(-5)
    plant.set_age(-1)

    print("Current plant:", plant.get_info())
