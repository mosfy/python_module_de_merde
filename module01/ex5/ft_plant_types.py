class Plant:
    """
    a Plant blueprint that can represent any plant with its attributes.
    
    Attributes:
        name (str): The name of the plant
        height (float): Height of the plant in centimeters
        day (int): Age of the plant in day
    """
    
    def __init__(self, name, height, day):
        """
        Initialize a Plant with its attributes.
        
        Args:
            name (str): The name of the plant
            height (float): Height in centimeters
            day (int): Age in day
        """
        self.name = name
        self.height = height
        self.day = day

    def get_info(self):
        """
        write all the information about the plant
        """
        return f"Created: {self.name} ({self.height}cm, {self.day} days)"
        
class Flower(Plant):
    """
    A class that represents a flower type plant.
    Currently, it does not add any specific behavior.
    """

    
    


if __name__ == "__main__":
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]

    plants = []
    count = 0

    for i in range(0, 5):
        name = plant_data[i][0]
        height = plant_data[i][1]
        day = plant_data[i][2]

        p = Plant(name, height, day)
        plants.append(p)
        count += 1

    print("=== Plant Factory Output ===")
    for i in range(0, count):
        print("Created:", plants[i].get_info())

    print("\nTotal plants created:", count)