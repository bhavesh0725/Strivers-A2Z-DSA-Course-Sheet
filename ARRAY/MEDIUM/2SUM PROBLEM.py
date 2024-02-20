def twoSum(list1, target):
  list1.sort()
  left= 0
  right=len(list1)-1
  while left <right:
    if list1[left]+ list1[right]== target:
      return (left, right)
    elif list1[left]+ list1[right]>target:
      right -=1
    elif list1[left]+ list1[right]<target:
      left +=1
  else:
    return(-1,-1)


if __name__=="__main__":
  list1=[2,6,5,8,11]
  target=15
  print("Two sum: ",twoSum(list1,target))
