#to find largest number
list= []
num= int(input("Enter number of elements in the list:"))
for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    list.append(ele)
print("Largest element is:", max(list))