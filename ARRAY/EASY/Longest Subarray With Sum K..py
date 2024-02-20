def longest_subarray_with_sum(arr, k):
  max_len = 0
  sum_indices = {}  # Dictionary to store cumulative sum and corresponding indices
  cumulative_sum = 0

  for i in range(len(arr)):
      cumulative_sum += arr[i]

      # If the cumulative sum equals k, update max_len
      if cumulative_sum == k:
          max_len = i + 1

      # If cumulative_sum - k is present in sum_indices, update max_len
      if cumulative_sum - k in sum_indices:
          max_len = max(max_len, i - sum_indices[cumulative_sum - k])

      # If cumulative_sum is not present in sum_indices, add it
      if cumulative_sum not in sum_indices:
          sum_indices[cumulative_sum] = i

  return max_len, sum_indices

# Example usage:
arr = [10, 5, 2, 7, 1, 9]
k = 15
print("Length of the longest subarray with sum", k, "is:", longest_subarray_with_sum(arr, k))
