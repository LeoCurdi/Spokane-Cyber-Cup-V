# Given parameters
p = 61
a = 37
G = (11, 12)
P = (60, 59)

# Function to calculate the modular inverse
def modinv(a, p):
    return pow(a, -1, p)

# Function to add two points on the elliptic curve
def ec_add(p1, p2, p):
    x1, y1 = p1
    x2, y2 = p2
    
    if p1 == (0, 0):
        return p2
    if p2 == (0, 0):
        return p1
    
    if p1 != p2:
        m = ((y2 - y1) * modinv(x2 - x1, p)) % p
    else:
        m = ((3 * x1**2 + 43) * modinv(2 * y1, p)) % p
    
    x3 = (m**2 - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    
    return (x3, y3)

# Perform scalar multiplication
result = (0, 0)
for bit in bin(a)[2:]:
    result = ec_add(result, result, p)
    if bit == '1':
        result = ec_add(result, G, p)

# Reflect the result over the x-axis
shared_secret = (result[0], -result[1] % p)

print("Shared Secret:", shared_secret)