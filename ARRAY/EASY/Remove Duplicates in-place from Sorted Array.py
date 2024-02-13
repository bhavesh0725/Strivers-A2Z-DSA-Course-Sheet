def duplicate(list1):
  i=0
  for j in range(1,len(list1)):
    if list1[i] != list1[j]:
      i +=1
      list1[i]= list1[j]
  return i+1

if __name__=="__main__":
  list1=list(map(int, input("Enter the elements in the list: ").split()))
  print("After removing duplicate-")
  newListIndex=duplicate(list1)
  print(list1[:newListIndex])





# Solution 2: Two pointers
# Intuition: We can think of using two pointers ‘i’ and ‘j’, we move ‘j’ till we don’t get a number arr[j] which is different from arr[i]. As we got a unique number we will increase the i pointer and update its value by arr[j]. 

# Approach:
# Take a variable i as 0;
# Use a for loop by using a variable ‘j’ from 1 to length of the array.
# If arr[j] != arr[i], increase ‘i’ and update arr[i] == arr[j].
#  After completion of the loop return i+1, i.e size of the array of unique elements.
