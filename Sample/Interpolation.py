values_for_interpolation = [25, 36, 69, 420, 1008, 2020, 88, 9, 1, 55]
sorted_values = values_for_interpolation.copy()
sorted_values.sort()
starting_point = 0
ending_point = len(sorted_values)//2
searchFlag = True

print("values before sorting", values_for_interpolation)
print("values after sorting", sorted_values)
search_value = int(input("Insert value to search for: "))
value_at_starting_index= sorted_values[0]
value_at_ending_index = sorted_values[len(sorted_values) - 1]
value_at_middle_index = sorted_values[len(sorted_values)//2]
print("Val at starting index = ", value_at_starting_index,
      "Val at middle index = ", value_at_middle_index,
      "Val at last index = ", value_at_ending_index)
diff_bet_values_and_search_val = [abs(search_value - value_at_starting_index),
                                  abs(search_value - value_at_middle_index),
                                  abs(search_value - value_at_ending_index)]
print(diff_bet_values_and_search_val)


if (diff_bet_values_and_search_val[1] < diff_bet_values_and_search_val[0]) and (diff_bet_values_and_search_val[1] < diff_bet_values_and_search_val[2]):
    starting_point = len(sorted_values)//2
    if sorted_values[len(sorted_values) // 2] <= search_value <= sorted_values[len(sorted_values) - 1]:
        ending_point = len(sorted_values) - 1
    else:
        ending_point = 0

   #ending point?
elif (diff_bet_values_and_search_val[2] < diff_bet_values_and_search_val[0]):
    starting_point = len(sorted_values) - 1

print("starting point is = ", starting_point)
print("ending point is = ", ending_point)
sizeOfList = len(sorted_values)//2
middle_index = (starting_point + ending_point) // 2
for iteration in range( 1 + sizeOfList):
    if sorted_values[middle_index] == search_value:
        print("The search was successful.")
        print("The location is on index" , middle_index)
        searchFlag = False
        break

    elif search_value < sorted_values[middle_index]:
        ending_point = middle_index
        middle_index = (starting_point + ending_point) // 2
        searchFlag = True

    elif search_value > sorted_values[middle_index]:
        starting_point = middle_index
        middle_index = (starting_point + ending_point) // 2
        searchFlag = True


if searchFlag:
    print("The search was unsuccessful.")




