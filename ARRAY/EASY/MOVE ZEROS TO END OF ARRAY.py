def move_zeros_to_end(arr):

  i = -1 # i is used for pointing to 0 
         # j is used for iterating over the loop, it finds if element is non zero then it swaps
  
  
  for j in range(len(arr)):
    if arr[j] ==0:
      i=j # it finds the first element as zero and point i to it.
      break

  
  for j in range(i+1,len(arr)):
    if arr[j] != 0:
      arr[i], arr[j] = arr[j], arr[i]
      i +=1
  
      
      


if __name__ == "__main__":
  arr = [1,2,8,0,3,5,0,2,0]
  move_zeros_to_end(arr)
  print(arr)  