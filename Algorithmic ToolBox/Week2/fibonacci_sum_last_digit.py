
def fibonacci_sum(n):
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
    print(fibonacci_sum(n))

    


