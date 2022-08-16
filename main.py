#Andy and Haesol for SPIS22
def rec_product(a, b):

 '''Calculate product a * b 
 recursively'''

 product = 0
 if (a == 0 or b == 0):
    return product
 elif(b < 0):
    abs(b)
    return a + a*(b-1)
 else:
    return a + a*(b-1)

 print(rec_product(a, b))
        
        