def union(arr1,arr2):
  set1=set()
  for i in range(len(arr1)):
    set1.add(arr1[i])

  for j in range(len(arr1)):
    set1.add(arr2[j])

  return list(set1)

if __name__=="__main__":
  arr1=[1,2,3,4,4,4,4,5]
  arr2=[1,2,6,7,8,9,0,3]
  print(union(arr1,arr2))