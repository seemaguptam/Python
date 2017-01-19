#6.02
para = "It was a beautiful day in New York City. Our hero Ariana Grande was on a walk from the Standard to Duane Reade. Ariana Grande was walking rather quickly because she had lived in New York for a few months. All of a sudden a slimy donut appeared out of nowhere. Ariana Grande decided to prance foolishly instead of dealing with the situation. Thrown off from Duane Reade Ariana Grande decides to go to Times Square instead. What a beautiful day in New York."


# lowecase
para_l = para.lower()

# remove period
para_nodot = para_l.replace('.','')

para_list = para_nodot.split(" ")

print(para_list)
print("\n")

i=0
d = dict()
while(i<len(para_list)):
    if (para_list[i] in d):
         d[para_list[i]] += 1
    else:
        d[para_list[i]] = 1
    i = i+1
       

print(d)
print("\n")

print("type the word to get its frequency")
word = input()

if (word in d):
    print('frequency of %s is %s' % (word, d[word]))
    print('frequency of ' + str(word) + ' is ' + str(d[word]))
    print("'%s' occurs %d times" % (word, d[word]))
    print("'" + str(word) + "' occurs " + str(d[word]) + " times") 
else:
    print("word not in dictionary")
    
         
    
