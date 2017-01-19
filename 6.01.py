my_dictionary = {
 'cat': 'a domestic feline', 
 'dog': 'a domestic canine', 
 'chair': 'furniture piece for sitting', 
 'car': 'automobile'
 }
print(my_dictionary)
print(my_dictionary['dog'])
print(my_dictionary.get('dog'))
print('cat' in my_dictionary)
print('monkey' in my_dictionary)

my_dictionary['tbd'] = 'to be decided'
my_dictionary['nbd'] = 'no big deal'

print('what do you want to lookup?')
abb = input()
print(abb)

if (abb in my_dictionary):
    print(my_dictionary[abb])
else:
    my_dictionary[abb]='default value'

print(my_dictionary)
