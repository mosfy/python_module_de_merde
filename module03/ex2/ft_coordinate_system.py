import math

def distanceSpawn(coord: tuple) -> float:
    x,y,z = coord
    return(math.sqrt((x)**2 + (y)**2 + (z)**2))

def parsedSpawn(coord: str) -> None:
    splited = coord.split(",")
    try:
        x = int(splited[0])
        y = int(splited[1])
        z = int(splited[2])
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e)}, Args: {e.args}")
        print(f'# Parsing invalid coordinates: "{coord}"')
        return
    position = (x,y,z)
    print(f'# Parsing coordinates: "{coord}"')
    print(f"# Parsed position: {position}")
    print(f"Distance between (0, 0, 0) and {position}:{distanceSpawn(position):.2f}")
        

def positionSpawn(x:int,y:int,z:int) -> None:
    for i in x,y,z:
        try:
            int(i)
        except ValueError as e:
            print(f"Error parsing coordinates: {e}")
            return
    position = (x,y,z)
    print(f"position created : {position}")
    print(f"Distance between (0, 0, 0) and {position}:{distanceSpawn(position):.2f}")

def unpakingTuple():
    position = (3,4,0)
    x, y, z = position
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")

if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    positionSpawn(10,20,5)
    positionSpawn(10,20,"caca")
    parsedSpawn("3,4,0")
    parsedSpawn("Abc,DPT,KK")
    print("# Unpacking demonstration:")
    unpakingTuple()
