def optimal_summands(n):
    summands = []
    # write your code here
    current_numer = 1
    while n > (2 * current_numer):
        summands.append(current_numer)
        
        n -= current_numer
        current_numer += 1    
        
        
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
