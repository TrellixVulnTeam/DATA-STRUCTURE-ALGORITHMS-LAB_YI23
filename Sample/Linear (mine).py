given = list()
flag = False
for iteration in range(10):
    answer = int(input("Enter an Integer: "))
    given.append(answer)

search_value = int(input("Enter an Integer to be Search: "))

for iteration in range(len(given)):
    if given[iteration] == search_value:
        print("Element at Index :",iteration)
        flag = True
        break

    else: flag = False

if flag == False:
    print("search is unsuccessful")



