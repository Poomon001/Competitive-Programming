import math

def gcd(a, b):
    while b:
        temp = a
        a = b
        b = temp % b
    return a

if __name__ == '__main__':
    print(gcd(100, 33), gcd(100, 33) == math.gcd(100, 33))
    print(gcd(33, 100), gcd(33, 100) == math.gcd(33, 100))
    print(gcd(25, 100), gcd(25, 100) == math.gcd(25, 100))
    print(gcd(13, 143), gcd(13, 143) == math.gcd(13, 143))
    print(gcd(108, 60), gcd(108, 60) == math.gcd(108, 60))