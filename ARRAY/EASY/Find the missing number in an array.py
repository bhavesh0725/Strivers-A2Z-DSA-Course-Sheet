


def missingNumber(a, N):
    # Summation of first N numbers:
    summation = (N * (N + 1)) // 2

    # Summation of all array elements:
    s2 = sum(a)

    missingNum = summation - s2
    return missingNum

def main():
    N = 5
    a = [1, 2, 4, 5]
    ans = missingNumber(a, N)
    print("The missing number is:", ans)

if __name__ == '__main__':
    main()






#approach 2:
def missingNumber(a, N):
  xor1 = 0
  xor2 = 0

  for i in range(N - 1):
      xor2 = xor2 ^ a[i]  # XOR of array elements

  for i in range(1,N+1):
    xor1 = xor1 ^ (i)  # XOR up to [1...N-1]

  

  return xor1 ^ xor2  # the missing number


def main():
  N = 5
  a = [1, 2, 4, 5]
  ans = missingNumber(a, N)
  print("The missing number is:", ans)


if __name__ == '__main__':
  main()


