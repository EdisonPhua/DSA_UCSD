def optimal_summands(n):
    summands = []
    # write your code here
    for i in range( 1, 4):
        if i == 3:
            summands.append(n)
            return summands
        summands.append(i)
        n -= i
        
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
