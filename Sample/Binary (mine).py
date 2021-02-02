given = [810, 398, 880, 632, 590, 460, 770, 384, 199, 775]
sorted_given = given.copy()
sorted_given.sort()
print("Sorted List: ", sorted_given)
search_value = int(input("Enter an Integer to be Search: "))

flag = False
size_of_list = len(sorted_given)
min_index = 0
mid_index = len(sorted_given) // 2
max_index = len(sorted_given)


for iteration in range(size_of_list):
    if search_value == sorted_given[mid_index]:
        print("Element at Index: ",mid_index)
        flag = True
        break

    elif search_value > sorted_given[mid_index]: # to the Right
        min_index = mid_index + 1
        mid_index = (abs(min_index - max_index) //2) + min_index
        max_index = max_index


    elif search_value < sorted_given[mid_index]: # to the Left
        min_index = min_index
        mid_index = max_index - mid_index //2
        max_index = max_index - 1

    else: flag = False

if flag == False: print("Search Unsuccessful")