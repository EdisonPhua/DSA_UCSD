
import time
def fibonacci_sum(n):
    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10


def fibonacci_sum1(n):
    if n <= 1:
        return n
    else:
        a,b, sum = 0,1,1
        for i in range(2, n+1):
            a,b = b%10, (b+a)%10
            sum += b
        return sum%10

if __name__ == '__main__':
    n = int(input())
    
    
    start = time.time()
    print(fibonacci_sum(n))
    end = time.time()
    print((end - start)*1000)
    
    
    start = time.time()
    print(fibonacci_sum1(n))
    end = time.time()
    print((end - start)*1000)
    


