# Task 1

text = "JohnDipPeta"
length = len(text)
middle = int(length // 2)
print("3 middle letters: ", text[middle -1:middle +2])


text1 = "JaSonAy"
length = len(text1)
middle = int(length // 2)
print("3 middle letters: ", text1[middle -1:middle +2])


# TASK 2

text = "day"
length = len(text)
if len(text) < 3:
    print(text)
elif text[-3:] == 'ing':
    print(text + "ing")
else:
    print(text + "ly")



# TASK 3
str1= input(("Enter a letter:\t"))
if (str1 == str1[::-1]):
      print("The letter is a palindrome")
else:
      print("The letter is not a palindrome")



# Task 5
user_text = input("mutqagrel bary:\t ")
print("anush " + user_text.upper())
print("anush " + user_text.lower())


# Voch partadir1
num = int(input("Enter a number:\t"))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print("The factorial of", num, "is", factorial)


# remove one of the  nth characters, which will enter user
str = " Armenia is beautiful"
n = int(input("enter a number:\t"))
str = str.replace(str[n],"", 1)
print(str)
