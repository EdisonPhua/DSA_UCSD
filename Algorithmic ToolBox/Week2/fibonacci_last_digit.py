import time
def fibonacci_number(n):
    if n <= 1:
        return n
    else:
        a,b = 0,1
        for i in range(2, n+1):
            a,b = b%10, (b+a)%10
        return b%10
    
def calc_fib_fast(n):
   f = []
   f.append(0)
   f.append(1)
   for i in range(2,n+1):
       f.append((f[i-1]%10+f[i-2]%10))
   return f[-1]%10


if __name__ == '__main__':
    input_n = int(input())
    
    start = time.time()
    print(fibonacci_number(input_n))
    end = time.time()
    print((end - start)*1000)

    start = time.time()
    print(calc_fib_fast(input_n))
    end = time.time()
    print((end - start)*1000)