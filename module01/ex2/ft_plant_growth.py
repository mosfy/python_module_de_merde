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

    def grow(self):
        """
        +1 for the height
        """
        self.height += 1

    def age(self):
        """
        +1 for the day
        """
        self.day += 1

    def get_info(self):
        """
        write all the information about the plant
        """
        return f"{self.name}: {self.height}cm, {self.day} days old"
        


if __name__ == "__main__":
    rose = Plant("Rose",25,30)

    time = 7
    start = rose.day
    print("=== Day 1 ===")
    print(rose.get_info())
    for i in range(1,time):
        rose.age()
        rose.grow()
    final = rose.day
    print(f"=== Day {time} ===")
    print(rose.get_info())
    print(f"Growth this week: +{final - start}cm")
