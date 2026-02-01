class Plant:
    """
    Base class representing a generic plant.

    Attributes:
        name (str): Name of the plant.
        height (float): Height of the plant in centimeters.
    """

    def __init__(self, name, height):
        """
        Initialize a Plant instance.

        Args:
            name (str): The plant name.
            height (float): Height in centimeters.
        """
        self.name = name
        self.height = height

    def grow(self):
        """
        Increase the height of the plant by 1 cm.
        """
        print(f"{self.name} grew 1cm")
        self.height += 1

    def get_info(self):
        """
        Return a formatted string containing plant information.

        Returns:
            str: Plant description.
        """
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """
    Represents a flowering plant.

    Inherits from:
        Plant

    Attributes:
        color (str): Color of the flower.
    """

    def __init__(self, name, height, color):
        """
        Initialize a FloweringPlant instance.

        Args:
            name (str): Flower name.
            height (float): Height in centimeters.
            color (str): Color of the flower.
        """
        super().__init__(name, height)
        self.color = color

    def get_info(self):
        """
        Return a formatted string containing flowering plant information.

        Returns:
            str: Flowering plant description.
        """
        return (f"- {self.name}: {self.height}cm, {self.color}"
                "flowers (blooming)")


class PrizeFlower(FloweringPlant):
    """
    Represents a prize-winning flower.

    Inherits from:
        FloweringPlant

    Attributes:
        prize_points (int): Points awarded for the prize flower.
    """

    def __init__(self, name, height, color, prize_points):
        """
        Initialize a PrizeFlower instance.

        Args:
            name (str): Flower name.
            height (float): Height in centimeters.
            color (str): Color of the flower.
            prize_points (int): Prize points awarded.
        """
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def get_info(self):
        """
        Return a formatted string containing prize flower information.

        Returns:
            str: Prize flower description.
        """
        return (f"- {self.name}: {self.height}cm, {self.color} flowers"
                f" (blooming), Prize points: {self.prize_points}")


class Garden:
    """
    Represents a garden containing multiple plants.

    Attributes:
        owner (str): Name of the garden owner.
        plants (list): List of Plant objects in the garden.
        nb_grew (int): Total growth applied to plants in the garden.
    """

    def __init__(self, owner):
        """
        Initialize a Garden instance.

        Args:
            owner (str): Name of the garden owner.
        """

        self.owner = owner
        self.plants = []
        self.nb_grew = 0

    def add_plant(self, plant: Plant):
        """
        Add a plant to the garden.

        Args:
            plant (Plant): Plant instance to add.
        """

        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def helping_plants(self):
        """
        Help all plants in the garden grow by increasing their height.
        """
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.nb_grew += 1


class GardenManager:
    """
    Manages multiple gardens and provides statistics on plants.

    Attributes:
        all_gardens (list): List of Garden instances managed.
    """

    def __init__(self):
        """
        Initialize a GardenManager instance.
        """
        self.all_gardens = []

    def add_garden(self, garden: Garden):
        """
        Add a garden to the manager.

        Args:
            garden (Garden): Garden instance to add.
        """
        self.all_gardens.append(garden)

    def size(self):
        """
        Return the total number of gardens managed.

        Returns:
            int: Number of gardens.
        """
        return len(self.all_gardens)

    def total_score(self):
        """
        Compute the total score of all gardens.

        Returns:
            str: Formatted string listing each garden's score.
        """
        s_ret = "Garden scores - "
        for garden in self.all_gardens:
            s_ret += (f"{garden.owner}: "
                      f"{GardenManager.GardenStats.get_score(garden)}, ")
        s_ret = s_ret[:-2]
        return (s_ret)

    @classmethod
    def create_garden_network(cls):
        """
        Create a default garden network with two gardens: Alice and Bob.

        Returns:
            GardenManager: Manager instance with two gardens added.
        """
        manager = cls()
        alice_garden = Garden("Alice")
        bob_garden = Garden("Bob")
        manager.add_garden(alice_garden)
        manager.add_garden(bob_garden)
        return manager

    class GardenStats:
        """
        Provides static methods to calculate statistics for a garden.
        """
        @staticmethod
        def count_plants(garden: Garden):
            """
            Count the number of plants in a garden.

            Args:
                garden (Garden): Garden instance.

            Returns:
                int: Number of plants.
            """
            return len(garden.plants)

        @staticmethod
        def total_height(garden: Garden):
            """
            Calculate total height of all plants in a garden.

            Args:
                garden (Garden): Garden instance.

            Returns:
                int: Sum of plant heights.
            """
            size = 0
            for plant in garden.plants:
                size += plant.height
            return (size)

        @staticmethod
        def total_prize(garden: Garden):
            """
            Calculate total prize points for PrizeFlowers in the garden.

            Args:
                garden (Garden): Garden instance.

            Returns:
                int: Sum of prize points.
            """
            prize = 0
            for plant in garden.plants:
                if (isinstance(plant, PrizeFlower)):
                    prize += plant.prize_points
            return (prize)

        @staticmethod
        def plant_type(garden: Garden):
            """
            Count the number of each plant type in the garden.

            Args:
                garden (Garden): Garden instance.

            Returns:
                str: Formatted string with counts of each plant type.
            """
            nb_plant = 0
            nb_floweringPlant = 0
            nb_prizeFlower = 0
            for plant in garden.plants:
                if (isinstance(plant, PrizeFlower)):
                    nb_prizeFlower += 1
                elif (isinstance(plant, FloweringPlant)):
                    nb_floweringPlant += 1
                else:
                    nb_plant += 1
            return (f"Plant types: {nb_plant} regular, {nb_floweringPlant} "
                    f"flowering, {nb_prizeFlower} prize flowers")

        @staticmethod
        def get_score(garden: Garden):
            """
            Calculate a score for the garden based on plant types and height.

            Args:
                garden (Garden): Garden instance.

            Returns:
                int: Total score.
            """
            score_plant = 0
            score_floweringPlant = 0
            score_prizeFlower = 0
            for plant in garden.plants:
                if (isinstance(plant, PrizeFlower)):
                    score_prizeFlower += 15 + plant.height + plant.prize_points
                elif (isinstance(plant, FloweringPlant)):
                    score_floweringPlant += 15 + plant.height
                else:
                    score_plant += plant.height
            return (score_plant + score_floweringPlant + score_prizeFlower)

        @staticmethod
        def Height_validation(garden: Garden):
            """
            Check if total height of plants meets a threshold (100 cm).

            Args:
                garden (Garden): Garden instance.

            Returns:
                bool: True if total height >= 100, else False.
            """
            return GardenManager.GardenStats.total_height(garden) >= 100

        @staticmethod
        def get_info(garden: Garden, garden_manager):
            """
            Print a detailed report for a garden.

            Args:
                garden (Garden): Garden instance.
                garden_manager (GardenManager): Manager managing the gardens.
            """
            print(f"=== {garden.owner}'s Garden Report ===")
            print("Plants in garden:")
            for plant in garden.plants:
                print(plant.get_info())
            print()
            print("Plants added: "
                  f"{GardenManager.GardenStats.count_plants(garden)},"
                  f" Total growth: {garden.nb_grew}cm")
            print(f"{GardenManager.GardenStats.plant_type(garden)}")
            print()
            print(f"Height validation test: "
                  f"{GardenManager.GardenStats.Height_validation(garden)}")
            print(garden_manager.total_score())
            print(f"Total gardens managed: {garden_manager.size()}")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print()

    manager = GardenManager.create_garden_network()

    alice_garden = manager.all_gardens[0]
    bob_garden = manager.all_gardens[1]

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    print()
    alice_garden.helping_plants()
    print()
    GardenManager.GardenStats.get_info(alice_garden, manager)
    print()

    little_orange_tree = Plant("Little Orange Tree", 5)
    little_tree = Plant("Little Tree", 4)
    lilac = FloweringPlant("Lilac", 30, "purple")
    Moonflower = PrizeFlower("Moonflower", 14, "yellow", 5)

    bob_garden.add_plant(little_orange_tree)
    bob_garden.add_plant(little_tree)
    bob_garden.add_plant(lilac)
    bob_garden.add_plant(Moonflower)

    print()
    bob_garden.helping_plants()
    print()
    GardenManager.GardenStats.get_info(bob_garden, manager)
