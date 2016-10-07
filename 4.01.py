# 4.1

# contract goes here
def de_vowel(a_string): 
    vowels = ['a', 'e', 'i', 'o','u']
    new_str = ''
    num=0
    for i in range(len(a_string)):
        if (a_string[i] not in vowels):
            new_str += a_string[i]
        else:
            num +=1
    print("there were " + str(num) + " vowels")
    return new_str


no_vowels = de_vowel("This sentence has no vowels")
print(no_vowels)
# examples go here
