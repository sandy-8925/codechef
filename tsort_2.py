number_of_input_values = int(raw_input())

current_input_position = 1
number_list=[]

for current_input_position in range(1, number_of_input_values+1):  
  current_input = int(raw_input())
  number_list.append(current_input)
  
number_list.sort()

for current_number in number_list:
  print current_number