# 6.03
l_d = {
 'cat': [1, 3, 4],
 'is': [1, 2, 3, 4]
}
print(l_d['cat'])

print("type of l_d is " + str(type(l_d)))
print("type of key is " + str(type('cat')))
print("type of value is " + str(type(l_d['cat'])))

l_d['is'] = [1, 2, 3, 4, 5]
print(l_d)

not_done = 1
d = dict()
while (not_done):
    print("what action - add or get or done <space> what day <space> action description")
    line = input()
    lis = line.split(" ")
    action = lis[0]
    #print(action)
    
    if (action == 'done'):
        not_done = 0
        break
    else: 
        day = lis[1]
        i=2
        desc = ""
        while (i<len(lis)):
            desc += (lis[i] + " ")
            i += 1
        #print('%s %s %s' % (action, day, desc))
        
        if (action == 'add'):
            if (day not in d):
                d[day] = desc
            else:
                print("you already have an action to perform on " + str(day) + " " + str(d[day]))
        elif (action == 'get'):
            if (day in d):
                print('returning %s %s' % (day, d[day]))
            else:
                print("no action is specified for " + str(day))
        print(d)
