# Task 1
# create an empty list
List = []
number = int(input("Enter user elements of list:\t"))
for i in range(0, number):
    element = int(input())
    List.append(element)
print(List)
# EACH ELEMENT CHANGE INTO ITS SQUARE
# output elements [20, 3, 10, 5]
List = list(map(lambda x: x*x,List))
print(List)
# my given output is [400, 9, 100, 25]


#Task 2
input_list = input("Enter a list of elements:\t ")
# enter elements by splitting them
list  = input_list.split()
sum = 0
for i in list:
    sum += int(i)
print("Sum = ",sum)


# Task 3
list = []
list1 = int(input("Enter element:\t"))
for i in range(0, list1):
    element = int(input())
    list.append(element)
#Given output is [10, 30, 4, 8]
print(list)
product = 1
for num in list:
    product = product * num
print("Product of elements ", 'is', product)



# Task 4

list = [5, 10, 20, 20, 25, 50, 20]
print(list)
index1 = 20
index2 = 200
for i in range(len(list)):
    if list[i] == index1:
        list[i] = index2
        break
print("new list is ", list)