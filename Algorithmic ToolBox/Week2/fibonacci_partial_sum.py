# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum , current, next = 0,0,1
    
    for i in range(to + 1):
        if i >= from_:
            sum += current
        current,next = next%10, (current+next)%10      
    return sum%10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))