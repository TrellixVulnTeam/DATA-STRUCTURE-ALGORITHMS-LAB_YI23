values = [25,36,69,420,1008,2020,88,9,1,55]
sorted_values = values.copy()
sorted_values.sort()
starting_point = 0
print(sorted_values)
search_value = int(input("Insert value to search for: "))
minimum_value = sorted_values[0]
maximum_value = sorted_values[len(sorted_values) - 1]
middle_value = sorted_values[len(sorted_values)//2]
#middle_value = len(sorted_values)//2 = 5
#middle_value = len(sorted_values - 1) // 2 = 4
print("MinVal = ",minimum_value, "MidVal = ",middle_value,"MaxVal = ",maximum_value)

diff_bet_min_and_search_val = [abs(search_value - minimum_value), abs(search_value - middle_value), abs(search_value - maximum_value)]
print ("lower the number the closer",diff_bet_min_and_search_val)
smallest = diff_bet_min_and_search_val[0]
if (diff_bet_min_and_search_val[1]) < (diff_bet_min_and_search_val[0]) and (diff_bet_min_and_search_val[2]):
    smallest = diff_bet_min_and_search_val [1]
    starting_point = 1
elif (diff_bet_min_and_search_val[2]) < (diff_bet_min_and_search_val[0]):
    smallest = diff_bet_min_and_search_val [2]
    starting_point = 2
print("Starting point is", starting_point)
## ADD BINARY OR LINEAR ALGO