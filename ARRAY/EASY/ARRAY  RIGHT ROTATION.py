def rotateRight(arr,k):
    k = k % len(arr)
    arr2 = []
    for i in range(len(arr)):
        arr2.append(arr[i-k])
    print(arr2)

arr = list(map(int, input("Enter the arr : ").split()))
k = int(input("Enter the rotation : "))
rotateRight(arr,k)
