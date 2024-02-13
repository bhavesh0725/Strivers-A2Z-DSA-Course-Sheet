def rotateLeft(arr, k):
  k = k % len(arr)  
  arr2 = []
  for i in range(len(arr)):
    arr2.append(arr[(i + k) % len(arr)])  
  print(arr2)


if __name__=="__main__":
  arr = list(map(int, input("Enter the arr : ").split()))
  k = int(input("Enter the rotation : "))
  rotateLeft(arr, k)

