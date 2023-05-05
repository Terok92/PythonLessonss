# Առաջադրանք 6
Aset = [input('Enter a value: ') for x in range(10)]
x = int(input())
print(Aset)
Bset = [input('Enter a value: ') for x in range(10)]
x = int(input())
print(Bset)
#converting list into set
mysetA = set(Aset)
mysetB = set(Bset)
print(set(Aset))
print(set(Bset))
# checking condition
if Aset == Bset:
    print("they are equal")
else:
    print("no")
#checking instersection
all_set = mysetA.intersection(mysetB)
print(all_set)
#checking diference
print(mysetA.difference(mysetB))
print(mysetB.difference(mysetA))
# Union
print("mysetA U mysetB:", mysetA.union(mysetB))

#Output from console or user for Aset: ['1', '2', '6', '8', '9', '62', '1', '5', '6', '6']
#Output from consle or user for Bset: ['5', '8', '3', '5', '4', '10', '20', '69', '62', '4']