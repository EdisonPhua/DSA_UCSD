def optimal_summands(n):
    summands = []
    # write your code here
    current_summand = 1
    while n > 0:
        if n <= 2 * current_summand:
            summands.append(n)
            break

        summands.append(current_summand)
        n -= current_summand
        current_summand += 1
        
        
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
