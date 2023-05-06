#Առաջադրանք7
english_armeniandict = {
    "English": "Հայերեն",
    "Variable": "Փոփոխական",
    "Declaration": "Հայտարարում",
    "Assignment": "Վերագրում",
    "Datatypes": "Տվյալների տիպեր",
    "Integer": "Թվային տիպ",
    "String": "Տողային տիպ",
    "Boolean": "Բուլյան տիպ",
    "true": "Ճշմարիտ",
    "else": "Հակառակ դեպքում",
    "array": "Զանգված",
    "if": "Եթե",
    "false": "Կեղծ",
}
Բառը = str(input("Մուտքագրել բառերը՝:\t"))
if Բառը in english_armeniandict:
    print(Բառը, "translation of ", english_armeniandict[Բառը])
else:
    print("Տվյալ բառը բացակայում է բառարանում")