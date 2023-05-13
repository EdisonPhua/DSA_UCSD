import time
def gcd(a, b):
    list = [a,b]
    list.sort()
    while list[0]:
        list[1], list[0] = list[0], list[1] % list[0]
    return list[1]

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
    
    
