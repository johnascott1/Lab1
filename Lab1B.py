classQty = int(input("How many classes are you taking this semester?"))
#This list will hold the class names entered by the user.
list_of_classes = []
#This loop will iterate once for each class the user is taking.
for c in range(classQty):
    #The user will enter the name of the class
    newClass = input("enter the name of the class")
    #The class name will then be appended to the aforementioned list
    list_of_classes += newClass

for c in list_of_classes:
    print(c)

