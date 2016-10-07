# 4.05

def my_nested_looping_function(a_list): 
     for i in range(0, len(a_list)): 
         value = a_list[i]
         for j in range(0, i): 
             value += j 
         print(value)

basic_list = [1, 2, 3, 4]
my_nested_looping_function(basic_list)
