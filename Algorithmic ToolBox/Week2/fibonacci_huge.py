
import time

def fibonacci_huge_naive(n):
    if n <= 1:
        return n
    else:
        a,b = 0,1
        for i in range(2, n+1):
            a,b = b, (b+a)
        return b%m




def fibonacci_huge_naive1(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))


    start = time.time()
    print(fibonacci_huge_naive(n, m))
    end = time.time()
    print((end - start)*1000)
    
    start = time.time()
    print(fibonacci_huge_naive1(n, m))
    end = time.time()
    print((end - start)*1000)