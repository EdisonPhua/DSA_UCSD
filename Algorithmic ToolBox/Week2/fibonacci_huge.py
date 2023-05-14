
import time
def fibonacci_huge_naive(n,m):
    if n <= 1:
        return n
    else:
        a,b = 0,1
        for i in range(2, n+1):
            a,b = b%m, (b+a)%m
        return b%m


def fibonacci_huge_naive1(n,m):
    if n <= 1:
        return n
    else:
        a,b = 0,1
        for i in range(2, n+1):
            a,b = b%10, (b+a)%10
        return b%m

if __name__ == '__main__':
    n, m = map(int, input().split())
    
    
    
    start = time.time()
    print(fibonacci_huge_naive(n, m))
    end = time.time()
    print((end - start)*1000)

    start = time.time()
    print(fibonacci_huge_naive1(n, m))
    print((end - start)*1000)
