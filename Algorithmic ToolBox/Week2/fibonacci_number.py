import time

def fibonacci_number(n):
    if n <= 1:
        return n
    else:
        a,b = 0,1
        for _ in range(2, n+2):
            a,b = b, (b+a)
        return b
            



def fibonacci_number1(n):
    if n <= 1:
        return n

    return fibonacci_number(n - 1) + fibonacci_number(n - 2)


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
