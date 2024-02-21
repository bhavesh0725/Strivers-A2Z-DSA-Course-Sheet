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
