def GCD(A, B):
    R = A % B
    if(R == 0):
        return B
    else:
        return GCD(B, R)
    

print(GCD(192, 162))

