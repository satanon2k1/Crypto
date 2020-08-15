# r = num * x + mod * y

def EGCD(number, modulo):
    number %= modulo
    x0, y0, x1, y1 = 0, 1, 1, 0
    while True:
        q, r = modulo // number, modulo % number
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
        
        if r == 0:
            break
            
        modulo, number = number, r
        
    return (x0, y0)

print(EGCD(26513, 32321))