

def alternative(list1):
  pos = 0
  neg = 1
  ans=[0] * len(list1)
  for i in range(len(list1)):
      if list1[i] > 0:
          ans[pos] = list1[i]
          pos += 2
      elif list1[i] < 0:
          ans[neg] = list1[i]
          neg += 2
  return ans

if __name__ == "__main__":
  list1 = [1, 2, -4, -5]
  print(alternative(list1))
