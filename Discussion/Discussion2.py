#TASK1
numeric_patterns = int(input("enter numeric patterns:\t"))
for i in range(numeric_patterns + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()


#TASK2
Given_Numbers = [12, 75, 150, 180, 145, 525, 50]
Numbers = []
for i in Given_Numbers:
    if i % 5 == 0:
        Numbers.append(i)
        if i > 150:
            if i > 500:
                break

print(Numbers)



#TASK3
numbers = int(input("input your random number:\t"))
print(numbers)
count = 0
while numbers != 0:
    numbers //= 10
    count += 1

print("Digits are: ", count)


#Task4
start = int(input("Enter your point:\t"))
end = int(input("Enter ending point:\t"))
prime_numbers = []
for number in range(start, end):
    if number > 1:
        if number % 2 == 0:
            continue
        for i in range(3, (number//2)+1):
            if number % i == 0:
                print("number:\t", number)
                print("i:\t", i)
                break
        else:
            prime_numbers.append(number)
print(prime_numbers)




#TASK5
number = int(input("enter upper patterns:\t"))
for i in range(0, number):
      for j in range(0, i + 1):
        print("* ", end="")
      print()

number2 = int(input(" enter Lower patterns:\t"))
for i in range(number2 + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")


#TASK6
new_dict = {1: 'red',
            2: 'green',
            3: 'black',
            4: 'white',
            5: 'black'
            }
print("Original Dictionary:")
print(new_dict)
print("Length of dictionary values:", (len(new_dict.values())))
new_dict2 = {'1': 'Austin Little',
             '2': 'Natasha Howard',
             '3': 'Alfred Mullins',
             '4': 'Jamie Rowe'
             }
print("Original Dictionary2:")
print(new_dict2)
print("Length of dictionary values:", (len(new_dict2.values())))



#TASK7
sentence = input("Input sentence for count the occurances:\t").split()
print(sentence)
words = sentence
word_counts = {}
for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1
print(word_counts)
for key, value in word_counts.items():
    print(f'word: {key}, count: {value}')


#Task8
#  find Perfect Number
Perfect_Number = int(input(" Please Enter any Number: "))
Sum = 0
for i in range(1, Perfect_Number):
    if(Perfect_Number % i == 0):
        Sum = Sum + i
if (Sum == Perfect_Number):
    print(" %d is a Perfect Number" %Perfect_Number)
else:
    print(" %d is not a Perfect Number" %Perfect_Number)


#TASK9
List = [5, 6, -20, -12, 8, 9, -30];
x = sum(1 for i in List if i >= 0)
print("Length of Positive numbers is:", x)
print("Length of Negative numbers is:", len(List) - x)

Separated_List = list(map(int, input("enter negative and positive numbers:\t")))
print(Separated_List)
map(int, Separated_List)
positive, negative = 0, 0
for num in Separated_List:
    if num >= 0:
        positive += 1
    else:
        negative += 1
print("Positive numbers in the list: ", positive)
print("Negative numbers in the list: ", negative)

Givenlist = [5, 6, -20, -12, 8, 9, -30]
positive_count, negative_count = 0, 0
for num in Givenlist:
    if num >= 0:
        positive_count += 1
    else:
        negative_count += 1
print("Positive numbers in the list: ", positive_count)
print("Negative numbers in the list: ", negative_count)


#Task10
#swaping  numbers in list
Swap_List = []
Number = int(input("How many elements in list :\t"))
for i in range(1, Number + 1):
    Number2 = int(input("Please enter the Value of %d  Element:\t" %i))
    Swap_List.append(Number2)
print("List of elements :\t", Swap_List)
# Swap list
ele = Swap_List[0]
Swap_List[0] = Swap_List[Number - 1]
Swap_List[Number - 1] = ele
print("List after swapping of elements :\n", Swap_List)