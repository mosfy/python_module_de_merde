class Plant:
    """
    Base class representing a generic plant.

    Attributes:
        name (str): Name of the plant.
        height (int): Height of the plant in centimeters.
        age (int): Age of the plant in days.
    """

    def __init__(self, name, height, age):
        """
        Initialize a Plant instance.

        Args:
            name (str): Name of the plant.
            height (int): Height in centimeters.
            age (int): Age in days.
        """
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        """
        Return a formatted string containing basic plant information.

        Returns:
            str: Plant description including name, height, and age.
        """
        return f"{self.name}: {self.height}cm, {self.age} days"


class Flower(Plant):
    """
    Represents a flower plant.

    Inherits from:
        Plant

    Attributes:
        color (str): Color of the flower.
    """

    def __init__(self, name, height, age, color):
        """
        Initialize a Flower instance.

        Args:
            name (str): Name of the flower.
            height (int): Height in centimeters.
            age (int): Age in days.
            color (str): Flower color.
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """
        Print a message indicating that the flower is blooming.
        """
        print(f"{self.name} is blooming beautifully!")

    def get_info(self):
        """
        Return a formatted string containing flower information.

        Returns:
            str: Flower description including name, height, age, and color.
        """
        return (f"{self.name} (Flower): {self.height}cm, "
                f"{self.age} days, {self.color} color")


class Tree(Plant):
    """
    Represents a tree plant.

    Inherits from:
        Plant

    Attributes:
        trunk_diameter (int): Diameter of the tree trunk in centimeters.
    """

    def __init__(self, name, height, age, trunk_diameter):
        """
        Initialize a Tree instance.

        Args:
            name (str): Name of the tree.
            height (int): Height in centimeters.
            age (int): Age in days.
            trunk_diameter (int): Diameter of the trunk in centimeters.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """
        Print a message indicating the shade produced by the tree.
        """
        shade_area = int(self.trunk_diameter * 1.56)
        print(f"{self.name} provides {shade_area} square meters of shade")

    def get_info(self):
        """
        Return a formatted string containing tree information.

        Returns:
            str: Tree description including name, height, age,
            and trunk diameter.
        """
        return (f"{self.name} (Tree): {self.height}cm, {self.age} days,"
                f"{self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """
    Represents a vegetable plant.

    Inherits from:
        Plant

    Attributes:
        harvest_season (str): Season when the vegetable is harvested.
        nutritional_value (str): Main nutritional value of the vegetable.
    """

    def __init__(self, name, height, age, harvest_season, nutritional_value):
        """
        Initialize a Vegetable instance.

        Args:
            name (str): Name of the vegetable.
            height (int): Height in centimeters.
            age (int): Age in days.
            harvest_season (str): Season of harvest.
            nutritional_value (str): Nutritional content.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        """
        Return a formatted string containing vegetable information.

        Returns:
            str: Vegetable description including name, height,
            age, and harvest season.
        """
        return (f"{self.name} (Vegetable): {self.height}cm, {self.age} days,"
                f"{self.harvest_season} harvest")

    def show_nutrition(self):
        """
        Print the nutritional value of the vegetable.
        """
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 30, "red")
    lilac = Flower("Lilac", 20, 25, "purpel")

    oak = Tree("Oak", 500, 1825, 50)
    orange_tree = Tree("Orange_tree", 600, 1460, 60)

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 69, 67, "autumn", "carotite")

    for plant in [rose, lilac, oak, orange_tree, tomato, carrot]:
        print(plant.get_info())
        if isinstance(plant, Flower):
            plant.bloom()
            print()
        elif isinstance(plant, Tree):
            plant.produce_shade()
            print()
        elif isinstance(plant, Vegetable):
            plant.show_nutrition()
            print()
