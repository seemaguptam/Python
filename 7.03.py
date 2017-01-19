#7.03
class Kangaroo(object): 
    def __init__(self, pc=0): 
        if (pc):
           self.pouch_contents = pc
        else:
           self.pouch_contents = []         
        
    def __str__(self):
        return 'pouch contents: %s' % (str(self.pouch_contents))
    
    def put_in_pouch(self, x):
        self.pouch_contents.append(x)

kanga = Kangaroo()
roo = Kangaroo()

kanga.put_in_pouch(roo)
print(kanga)
