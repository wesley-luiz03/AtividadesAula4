A = 4
B = 20
C = A + B

if (A < 10) and (B > 1):
    X = B + C
    Y = B % A
    Z = A + B + C / 3
else:
    X = C - B
    Y = C % B
    Z = A + B + C / 3
    
print(f"Algoritmo 2 -> {X}, Y: {Y}, Z: {Z:.2f}")