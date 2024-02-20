def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # Write your code here.
    if len(a) < 2:
        return None  # Edge case: array has less than 2 elements
    
    max1, max2 = float('-inf'), float('-inf')
    min1, min2 = float('inf'), float('inf')

    for num in a:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
        
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    # Return the second largest and second smallest elements
    return max2, min2
  # Example usage:
n = 5
a = [3, 1, 5, 2, 4]
print(getSecondOrderElements(n, a))  # Output should be (4, 2)
