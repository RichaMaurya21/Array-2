'''Given an array of numbers of length N, find both the minimum and maximum. Follow up : 
Can you do it using less than 2 * (N - 2) comparison
'''
def findMinMax(nums):
    if not nums:
        raise ValueError("Array cannot be empty")
    
    n = len(nums)
    if n == 1:
        return nums[0], nums[0]
    
    # Initialize max_element and min_element with the first two elements
    if n % 2 == 0:
        if nums[0] > nums[1]:
            max_element = nums[0]
            min_element = nums[1]
        else:
            max_element = nums[1]
            min_element = nums[0]
        i = 2
    else:
        max_element = min_element = nums[0]
        i = 1
    
    # Iterate over the array in pairs
    while i < n - 1:
        if nums[i] > nums[i + 1]:
            larger = nums[i]
            smaller = nums[i + 1]
        else:
            larger = nums[i + 1]
            smaller = nums[i]
        
        if larger > max_element:
            max_element = larger
        if smaller < min_element:
            min_element = smaller
        
        i += 2
    
    # If the length of array is odd, last element needs to be compared separately
    if n % 2 != 0:
        if nums[-1] > max_element:
            max_element = nums[-1]
        if nums[-1] < min_element:
            min_element = nums[-1]
    
    return min_element, max_element

# Test the function
nums = [2, 3, 4, 1, 5, 6, 7,9,100,25]
print(findMinMax(nums))  # Output should be (1, 7)

'''def findMinMax(nums):
    minimum = float('inf')
    maximum = 0
    for i in range(len(nums)):
        minimum = min (minimum, nums[i])
        maximum = max(maximum, nums[i])


    return minimum, maximum'''
