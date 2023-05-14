

def fibonacci_sum_squares(n):
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
    print(fibonacci_sum_squares(n))
