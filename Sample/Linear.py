values = list()
searchValue = 0
searchFlag = False
print("Input 10 numbers")
for ittereation in range(10):
    answer = input("Insert value number " + str(ittereation+1) + ":") #Cant use "," only "+" when adding argument in input
    values.append(answer)
searchValue = input("Insert value to search for: ")
# Linear Search
for ittereation in range(len(values)):
    if (values[ittereation] == searchValue):
        print("Search is successfull")
        print("the location is on index", ittereation)
        searchFlag = False
        break
    else:
        searchFlag = True

if searchFlag == True:
    print("search is unsuccessful")