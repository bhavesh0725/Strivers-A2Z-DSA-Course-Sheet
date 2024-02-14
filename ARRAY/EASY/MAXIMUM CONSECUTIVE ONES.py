def max_consecutive_ones(arr1):
  
  count=0
  max_count=0

  for i in range(len(arr1)):
    if arr1[i]==1:
      count+=1
      max_count= max(max_count, count)
    elif arr1[i]==0:
      count =0
  return max_count
    




if __name__=="__main__":
  arr1=[0,0,0,0,0,0]
  print("Max no of consecutive ones : ",max_consecutive_ones(arr1))