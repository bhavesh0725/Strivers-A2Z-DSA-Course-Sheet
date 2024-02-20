def longest_subarray_with_sum(arr, k):
    max_len = 0
    cumulative_sum = 0
    sum_indices = {0: -1}  # Initialize with a sum of 0 at index -1
    
    for i in range(len(arr)):
        cumulative_sum += arr[i]
        
        # If cumulative sum - k is already in the hashmap, it means there's a subarray with sum k
        if cumulative_sum - k in sum_indices:
            max_len = max(max_len, i - sum_indices[cumulative_sum - k])
        
        # If cumulative sum is not in the hashmap, add it with current index
        if cumulative_sum not in sum_indices:
            sum_indices[cumulative_sum] = i
    
    return max_len

# Example usage:
arr = [10, 5, 2, 7, 1, 9]
k = 15
print("Length of the longest subarray with sum", k, "is:", longest_subarray_with_sum(arr, k))
