# Task 1
s = 0
for number in range(10,100):
    if number % 4 == 1:
        s = s + number
print(s)


# Task 2
t = int(input("input a tempreture:\t"))
if t <= 18:
    print("curte")
elif 18 < t < 24:
    print("hachelie")
elif t > 24:
    print("shoge")



# Task 3.1
x = 0
while x < 40:
    x = x + 1
    if x % 4 == 0:
        print('Number', x)


# Task 3.2
sum = 0
for i in range (7, 30):
    if i % 2 == 0:
        sum += i
        print(sum)




# Task 4
for num in range(100, 601):
    if num % 3 == 0 and num % 11 == 0 and num % 7 != 0:
        print(num)




# Task 5
a = int(input(" enter number:\t"))
b = int(input(" enter number:\t"))
for i in range(a, b+1):
    if i % 7 == 0:
        print(i)