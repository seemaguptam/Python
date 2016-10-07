#4.02

# contract goes here
def fruit_pluralizer(l): 
    # your code goes here
    for i in range(0, len(l)):
        str = l[i]
        if (l[i][len(str)-1] == 'y'):
            l[i] = l[i][0:-1]
            l[i] += 'ies'
        else:
            l[i] += 's'

    return l


fruit_list = ['apple', 'berry', 'melon', 'cranberry', 'strawberrey']
#fruit_list = []
print("Single Fruit: " + str(fruit_list))
fruit_pluralizer(fruit_list)
print("No longer single Fruit: " + str(fruit_list))
# examples go here


# contract goes here
def my_reverse(s):
    rs=""
    for i in range(0, len(s)):
        rs += s[(-1*(i+1))]

    return rs

    
reversed = my_reverse("apples")
print(reversed)

def rev_str_in_list(l):
    new_list = []
    for i in range(0,len(l)):
        rs=my_reverse(l[i])
        new_list.append(rs)

    return new_list

print(rev_str_in_list(fruit_list))
