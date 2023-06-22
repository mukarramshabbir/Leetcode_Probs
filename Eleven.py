def maxArea(height):
    n = len(height)
    left = 0
    right = n - 1
    max_area = 0
    
    while left < right:
        # Calculate the area of the container
        area = min(height[left], height[right]) * (right - left)
        
        # Update the maximum area if necessary
        max_area = max(max_area, area)
        
        # Move the pointer corresponding to the shorter line inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

            
if __name__=="__main__":
    s = [1,8,6,2,5,4,8,3,7]
    result = maxArea(s)
    print(result) 