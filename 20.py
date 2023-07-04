def checkStraightLine(coordinates):
    """
    :type coordinates: List[List[int]]
    :rtype: bool
    """
    # Get the coordinates of the first two points
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]

    # Calculate the slope between the first two points
    # Avoiding division by zero, we multiply the numerator and denominator by (x2 - x1)
    slope = (y2 - y1) * 1.0 / (x2 - x1) if (x2 - x1) != 0 else float('inf')

    # Check the slope between each pair of consecutive points
    for i in range(2, len(coordinates)):
        x, y = coordinates[i]

        # If the slope is not the same, return False
        if ((x-x1)*(y2-y1)!=(x2-x1)*(y-y1)):
            return False

    # If all slopes are the same, return True
    return True
            
    

if __name__=="__main__":
    coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    result = checkStraightLine(coordinates)
    print(result)