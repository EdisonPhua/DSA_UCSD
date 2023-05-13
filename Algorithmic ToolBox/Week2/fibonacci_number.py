import time

def fibonacci_number(n):
    if n <= 1:
        return n
    else:
        a,b = 0,1
        for _ in range(2, n+1):
            a,b = b, (b+a)
        return b
            



def fibonacci_number1(n):
    if n <= 1:
        return n

    return fibonacci_number(n - 1) + fibonacci_number(n - 2)


if __name__ == '__main__':
    input_n = int(input())
    
    
    start = time.time()
    print(fibonacci_number(input_n))
    end = time.time()
    print((end-start)*1000)
    
    start = time.time()
    print(fibonacci_number1(input_n))
    end = time.time()
    print((end-start)*1000)
