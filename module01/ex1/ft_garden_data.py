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
            height_cm (float): Height in centimeters
            day (int): Age in day
        """
        self.name = name
        self.height = height
        self.day = day


if __name__ == "__main__":
    names = ["Rose","Sunflower","Cactus"]
    heights = [25,80,15]
    days = [30,45,120]
    
    i = 0
    for name in names:
        plant_tmp = Plant(names[i], heights[i], days[i])
        print(f"{plant_tmp.name}: {plant_tmp.height}cm, {plant_tmp.day} days old")
        i = i + 1