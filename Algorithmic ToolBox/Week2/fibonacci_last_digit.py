
def fibonacci_number(n):
    if n <= 1:
        return n
    else:
        a,b = 0,1
        for i in range(2, n+1):
            a,b = b, (b+a)
        return b%10


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))