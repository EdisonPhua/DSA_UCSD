

def fibonacci_huge_naive(n,m):
    if n <= 1:
        return n
    else:
        a,b = 0,1
        for i in range(2, n+1):
            a,b = b%10, (b+a)%10
        return b%m

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
