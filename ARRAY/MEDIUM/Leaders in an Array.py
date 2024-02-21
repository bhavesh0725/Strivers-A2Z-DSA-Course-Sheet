

def leader(list1):
  ans=[]
  n=len(list1)
  maxi=list1[n-1]
  ans.append(list1[n-1])

  for i in range(n-1, -1, -1):
    if list1[i]> maxi:
      ans.append(list1[i])
      maxi= list1[i]
  return ans

if __name__ == "__main__":
  list1 = [10, 22, 12, 3, 0, 6]
  print(leader(list1))
