#Առաջադրանք1 read and display
def read_file():
    file = open("poem.txt","r")
    for line in file:
        print(line, end="")
    file.close()


read_file()



# Առաջադրանք2 append display
file = open("poem.txt", "rt")
data = file.read()
words = data.split()

print('Number of words in text file :', len(words))

# Առաջադրանք3 count and displaying file
file3 = open("sample.txt", "a")
file3.write('welcome our new world:\t cutie')
file3.close()


# Առաջադրանք5 read a file and write it to aother file
with open("a.txt") as file:
    with open("b.txt", "w") as file1:
        for line in file:
            file1.write(line)



# Առաջադրանք4 words less than 4 characters
def DISPLAYWORDS():
    file = open("STORY.TXT", "r")
    line = file.readlines()
    for i in line:
        if len(i) <= 4:
            print(i)
    file.close()


print("word that have less than 4 characters:\n")
DISPLAYWORDS()
