given = [810, 398, 880, 632, 590, 460, 770, 384, 199, 775]
sorted_given = given.copy()
sorted_given.sort()
print("Sorted List: ", sorted_given)
search_value = int(input("Enter an Integer to be Search: "))

start_point = 0
end_point = 0
first_element = sorted_given[0]
mid_element = sorted_given[len(sorted_given) // 2]
last_element = sorted_given[len(sorted_given) - 1]

difference_values_elements = [
    abs(search_value - first_element ),
    abs(search_value - mid_element ),
    abs(search_value - last_element ),
]
print(difference_values_elements)

if difference_values_elements[0] < difference_values_elements[1] and difference_values_elements[2]:
    start_point = 0
    end_point = len(sorted_given) // 2
elif difference_values_elements[1] < difference_values_elements[2] and difference_values_elements[0]:
    start_point = (len(sorted_given) // 2) - 2
    end_point = (len(sorted_given) - 1) - 1
elif difference_values_elements[2] < difference_values_elements[1] and difference_values_elements[0]:
    start_point = len(sorted_given) // 2
    end_point = len(sorted_given) - 1
print((start_point,end_point))


flag = False
size_of_list = len(sorted_given)
min_index = start_point
mid_index = start_point // end_point
max_index = end_point


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