def appearOnes(arr1):
  result=0
  for i in range(len(arr1)):
    result ^= arr1[i]
  
  return result




if __name__=="__main__":
  arr1=[1,2,3,4,3,2,1]
  print("The number that appears once, and the other numbers twice : ", appearOnes(arr1))




  