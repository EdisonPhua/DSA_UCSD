import time
def fibonacci_sum_squares(n):
    if n <= 1:
        return n

    previous, current, sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current ** 2

    return sum % 10

def fibonacci_sum_squares1(n):
    if n <= 1:
        return n
    else:
        a,b, sum = 0,1,1
        for i in range(n-1):
            a,b = b%10, (b+a)%10
            sum += b**2
        return sum%10

if __name__ == '__main__':
    n = int(input())
    
    
    start = time.time()
    print(fibonacci_sum_squares(n))
    end = time.time()
    print((end - start)*1000)

    start = time.time()
    print(fibonacci_sum_squares1(n))
    end = time.time()
    print((end - start)*1000)
