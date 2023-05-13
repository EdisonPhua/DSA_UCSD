import time
def gcd(a, b):
    list = [a,b]
    list.sort()
    while b:
        list[1], b = b, a % b
    return a

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
    
    
