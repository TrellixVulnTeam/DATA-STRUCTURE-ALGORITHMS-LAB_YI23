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
for iteration in range(start_point ,end_point+1):
    if sorted_given[iteration] == search_value:
        print("Element at Index :",iteration)
        flag = True
        break

    else: flag = False

if flag == False:
    print("search is unsuccessful")

