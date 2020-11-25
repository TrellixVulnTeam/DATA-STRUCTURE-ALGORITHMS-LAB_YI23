values = list()
searchValue = 0
searchFlag = False
print("Input 10 numbers")
for ittereation in range(10):
    answer = int(input("Insert value number " + str(ittereation+1) + ":")) #Cant use "," only "+" when adding argument in input
    values.append(answer)
searchValue = int(input("Insert value to search for: "))

#Binary search
tempValueList = values
tempValueList.sort()
sizeOfList = len(tempValueList)
middleValue = sizeOfList // 2 # for float "/" for whole "//"
minimumValue = 0
maximumValue = sizeOfList
indexLocation = minimumValue
print("List",tempValueList," And there MinVal = {0}, MaxVal = {1}, M1idVal = {2} ".format(minimumValue,maximumValue,middleValue))
for iteration in range( 1 + sizeOfList // 2):
    if (tempValueList[middleValue] == searchValue):
        print("Search is successfull")
        print("the location is on index", indexLocation)
        searchFlag = False
        break

    elif searchValue < tempValueList[middleValue]:                     #Moving to the left
        tempValueList = tempValueList[0 : middleValue]
        middleValue = len(tempValueList) // 2
        maximumValue = len(tempValueList)
        indexLocation += middleValue
        # maximumValue = middleValue - 1
        # middleValue = (minimumValue + middleValue) // 2
        # minimumValue = minimumValue
        print("MinVal = {0}, MaxVal = {1}, MidVal = {2} ".format(minimumValue,maximumValue,middleValue))
        print(tempValueList)
        searchFlag = True


    elif searchValue > tempValueList[middleValue]:                     #Moving to the right
        tempValueList = tempValueList[middleValue + 1 : len(tempValueList)]
        middleValue = len(tempValueList) // 2
        maximumValue = len(tempValueList)
        indexLocation += middleValue
        # minimumValue= middleValue + 1
        # middleValue = (minimumValue + middleValue) // 2
        # maximumValue = maximumValue
        print("MinVal = {0}, MaxVal = {1}, MidVal = {2} ".format(minimumValue,maximumValue,middleValue))
        print(tempValueList)
        searchFlag = True


    else:
        searchFlag = True

if searchFlag:
    print("search is unsuccessful")