


def dnf(list1):
  low=0
  mid=0
  high=len(list1)-1
  while mid< high:
    if list1[mid]==0:
      list1[low],list1[mid]= list1[mid], list1[low]
      low +=1
      mid +=1

    elif list1[mid] ==1:
      mid +=1
      

    else:
      list1[mid],list1[high] = list1[high], list1[mid]
      high -=1
  return list1





 
if __name__=="__main__":
  list1=[0,2,1,0,1,0,2,0,2,1,0,2]
  print("After sorting: ",dnf(list1))




# left to low =0, right to high =2, low to mid-1= 1
#  0 to low -1 = 0, low to mid - 1= 1, high +1 to n-1 = 2 
# [0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2]
#                  |    |  |
#                 low high mid


