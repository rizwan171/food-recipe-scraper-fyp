foodClassesFile = open('classes.txt', 'r')
foodClassesList = foodClassesFile.readlines()

# note: first line in file is not a class
foodClassesList = foodClassesList[1 : len(foodClassesList)]
print("Number of food classes: " + str(len(foodClassesList)))

# cleaning up the class names
foodClassesListClean = []
for foodClass in foodClassesList:
    foodClass = foodClass.strip("\n")
    foodClass = foodClass.replace("_", "+")
    foodClassesListClean.append(foodClass)

