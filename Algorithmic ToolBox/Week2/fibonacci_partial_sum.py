# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10


def fibonacci_partial_sum_naive1(from_, to):
    sum , current, next = 0,0,1
    
    for i in range(to + 1):
        
        
        
        
        a,b = b%10, (b+a)%10
        sum += b
    return sum%10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
