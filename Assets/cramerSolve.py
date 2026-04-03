# x1 + y1 + z1 = c1
# x2 + y2 + z2 = c2
# x3 + y3 + z3 = c3

#   Dx = c1((y2 * z3) - (z2 * y3)) - y1((c2 * z3) - (z2 * c3)) + z1((c2 * y3) - (y2 * c3))
#   Dy = x1((c2 * z3) - (z2 * c3)) - c1((c2 * z3) - (z2 * x3)) + z1((x2 * c3) - (c2 * x3))
#   Dz = x1((y2 * c3) - (c2 * y3)) - y1((x2 * c3) - (c2 * x3)) + c1((x2 * y3) - (y2 * x3))

#   D = x1((y2 * z3) - (z2 * y3)) - y1((x2 * z3) - (z2 * x3)) + z1((x2 * y3) - (y2 * x3))

#   x = Dx / D 
#   y = Dy / D
#   z = Dz = D

def solve(x1, y1, z1, c1, x2, y2, z2, c2, x3, y3, z3, c3):
    try:
        D = x1 * ((y2 * z3) - (z2 * y3)) - y1 * ((x2 * z3) - (z2 * x3)) + z1 * ((x2 * y3) - (y2 * x3))

        Dx = c1 * ((y2 * z3) - (z2 * y3)) - y1 * ((c2 * z3) - (z2 * c3)) + z1 * ((c2 * y3) - (y2 * c3))

        Dy = x1 * ((c2 * z3) - (z2 * c3)) - c1 * ((x2 * z3) - (z2 * x3)) + z1 * ((x2 * c3) - (c2 * x3))

        Dz = x1 * ((y2 * c3) - (c2 * y3)) - y1 * ((x2 * c3) - (c2 * x3)) + c1 * ((x2 * y3) - (y2 * x3))

        x =  Dx / D
    
        y = Dy / D

        z = Dz / D
    
        return D, Dx, Dy, Dz, x, y, z
    
    except:
        
        D = -9999
        Dx = 0
        Dy = 0
        Dz = 0
        x = 0
        y = 0
        z = 0
        
        return D, Dx, Dy, Dz, x, y, z
    
    
    
