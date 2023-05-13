import time
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def gcd1(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


if __name__ == "__main__":
    a, b = map(int, input().split())
    
    
    start = time.time()
    print(gcd(a, b))
    end = time.time()
    print((end - start)*1000)
    
    start = time.time()
    print(gcd1(a, b))
    end = time.time()
    print((end - start)*1000)