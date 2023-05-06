#TASK1  ուղղանկյան պարագիծ
length = int(input("Enter you length:\t"))
width = int(input("Input your width:\t"))
# Perimeter of a rectangle = 2*(Length + Width)


def rectnagle_perimeter(length, width):
    perimeter = 2*(length + width)
    return perimeter


perimeter = rectnagle_perimeter(length, width)
print("perimeter of Rectangle: ", end="",)
print(perimeter)


#Task2 քառակուսու պարագիծ
side = int(input("Enter you side:\t"))
# Perimeter of a square = Length * 4


def sqaure_perimeter(side):
    perimeter = side * 4
    return perimeter


perimeter = sqaure_perimeter(side)
print("perimeter of Square: ", end="",)
print(perimeter)


#Task3 մակերես ուղղանկյան
# area of rectangle
length = int(input("Enter you length:\t"))
width = int(input("Input your width:\t"))
# area of rectangle = length * width

def rectangle_area(length, width):
    square = length * width
    return square


square = rectangle_area(length, width)
print("area of rectangle: ", end="",)
print(square)



#TASK4 մակերես
# area of square
side = int(input("Enter you SIDE:\t"))
# area of square = side * side


def square_area(side):
    square = side ** 2
    return square


square = square_area(side)
print("area of square: ", end="",)
print(square)