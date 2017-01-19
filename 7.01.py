class Color(object): 
    """Represents a Color"""
    def __init__(self, r=0, g=0, b=0):
        self.r = r
        self.g = g
        self.b = b
        
    def __str__(self):
        return 'RGB: %d %d %d' % (self.r, self.g, self.b)

# red
c1 = Color() 
c1.r = 191
c1.g = 84
c1.b = 46

#green
c2 = Color()
c1.r = 144
c2.g = 178
c2.b = 71

#yellow
c3 = Color()
c3.r = 240
c3.g = 239
c3.b = 136


def add_color(cx, cy):
    ret = Color()
    ret.r = (cx.r + cy.r)//2
    ret.g = (cx.g + cy.g)//2
    ret.b = (cx.b + cy.b)//2
    return ret

mix1 = add_color(c1,c2)
print(mix1)
mix2 = add_color(c2,c3)
print(mix2)
mix3 = add_color(c1,c3)
print(mix3)


