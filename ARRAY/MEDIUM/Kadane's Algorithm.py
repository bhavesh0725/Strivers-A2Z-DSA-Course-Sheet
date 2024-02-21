def kadanesAlgo(list1):
  sum = 0
  maxi = 0
  for i in range(len(list1)):
    sum += list1[i]
    maxi = max(maxi, sum)

    if sum < 0:
      sum = 0
  return maxi


if __name__ == "__main__":
  list1 = [-7 ,- 8, - 16, - 4, - 8, - 5, - 7, - 11, - 10, - 12, - 4, - 6, - 4, - 16, - 10]
  ans = kadanesAlgo(list1)
  print(ans)



#Link: https://takeuforward.org/data-structure/kadanes-algorithm-maximum-subarray-sum-in-an-array/


#for printing the subarray with the largest sum
def kadanesAlgo(list1):
  current_sum = 0
  max_sum = 0
  start = 0  # Initialize starting index of max subarray
  end = 0  # Initialize ending index of max subarray

  for i in range(len(list1)):
      # Update current_sum and max_sum
      current_sum += list1[i]
      max_sum = max(max_sum, current_sum)

      # Track start and end indices of max subarray
      if current_sum == max_sum:
          end = i  # Update end index if current_sum equals max_sum

      # Handle negative current_sum by resetting it and start index
      if current_sum < 0:
          current_sum = 0
          start = i + 1  # Reset start index if current_sum becomes negative

  # Print the subarray with maximum sum
  print(f"Subarray with maximum sum: {list1[start:end+1]}")
  return max_sum

# Example usage
list1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = kadanesAlgo(list1)
print(f"Maximum contiguous sum: {result}")
