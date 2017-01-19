#6.04

para = "It was a beautiful day in New York City. Our hero Ariana Grande was on a walk from the Standard to Duane Reade. Ariana Grande was walking rather quickly because she had lived in New York for a few months. All of a sudden a slimy donut appeared out of nowhere. Ariana Grande decided to prance foolishly instead of dealing with the situation. Thrown off from Duane Reade Ariana Grande decides to go to Times Square instead. What a beautiful day in New York."
d = dict()
#para = "It was a beautiful day in New York City day day was."

def create_dict_from_para():
    global para
    global d
 
    # lowecase
    para_l = para.lower()

    # remove period
    para_nodot = para_l.replace('.','')

    para_list = para_nodot.split(" ")

    print(para_list)
    print("\n")

    i=0

    while(i<len(para_list)):
        if (para_list[i] in d):
             d[para_list[i]] += 1
        else:
            d[para_list[i]] = 1
        i = i+1
            
# end of function create_dict_from_para

create_dict_from_para()
       
print(d)


#reverse lookup
def reverse_lookup(d,v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()

# inverse dictionary
def inverse_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

inverse_d = inverse_dict(d)
print(inverse_d)

# sort vals
freqs = inverse_d.keys()

def find_max_value(fqs):
    max = 0
    for f in fqs:
        if f>max:
            max = f
    return f

"""
# easy version
v1 = find_max_value(freqs)
print("max1 is " + str(v1))

del inverse_d[v1]

v2 = find_max_value(freqs)
print("max2 is " + str(v2))

del inverse_d[v2]
"""

#Bonus
# sort by values
vals = list(d.values())
print(vals)

vals.sort()
vals.reverse()
print("vals is ")
print(vals)

# print most frequent words
i=0
while (i<len(vals)):
    print(str(inverse_d[vals[i]]) + " occurs " +  str(vals[i]) + " times")
    i += 1


i=0
sorted_vals = []
while (i<len(vals)):
    max = vals[0]
    max_ind = 0
    j = 0
    while (j<len(vals)):
        if (vals[j] > max):
            max = vals[j]
            max_ind = j
        j += 1
    sorted_vals.append(max)
    vals.pop(max_ind)
    i += 1

print(sorted_vals)

         




         
    
