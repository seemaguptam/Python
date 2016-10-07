# lab 2.05

l = ['prize1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10']
inp = input("which door")
ind = int(inp)
if (ind <= 10):
    print("you get prize ", l[ind-1])
else:
    print("num out of bounds")
    
          
