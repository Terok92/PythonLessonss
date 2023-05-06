# Task 1
num = int(input("enter number even or odd:\t"))
if num % 2 == 0:
    print("even")
else:
    print("odd")

if num % 3 == 0:
    print(" 3 bazmapatik e")
elif num % 2 == 0 and num % 3 == 0:
    print("number divides by both")

# Task 2
data_user = str(input("enter a string:\t"))
print("data user")
x = 15
y = 18
if y > x:
    print("y is greater than x")
elif y > x:
    pass

# Task 3
a = 15
b = 97

if a == b:
    print(a)
elif a > b:
    print("a is greater than b")
elif b > a:
    print("b is greater than a")

# Task 4
num = int(input("number divides by 5:\t"))
if num % 5 == 0:
    print("number divides by 5")
elif num % 7 == 0:
    print("number divides by 7")
elif num % 7 == 0 and num % 5 == 0:
    print("number divides by 5 and 7")