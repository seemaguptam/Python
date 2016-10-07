# lab 2.06
#
#tic tac toe
#1 2 3
#4 5 6
#7 8 9
#   1,2,3,4,5,6,7,8,9
b= [0,0,0,0,0,0,0,0,0]

attempt = 1
while (attempt<=9):
    loc=input("which location")
    l=int(loc)
    if (l>9 or l<0):
        print("out of bounds")
    else:
        if (attempt%2 != 0):
            b[l-1]='X'
        else:
            b[l-1]='Y'
    attempt = attempt + 1
    
print(b[0:3]) # b[0], b[1], b[2]
print(b[3:6]) # b[3], b[4], b[5]
print(b[6:9]) # b[6], b[7], b[8]



    
    
