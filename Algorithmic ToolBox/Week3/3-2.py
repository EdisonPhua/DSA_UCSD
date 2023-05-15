from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    
    
    # write your code here
    if capacity==0 or weights == None:
        return 0
    max_index = values.index(max(values))
    amount = min(capacity, weights[max_index])
    value = values[max_index] * ( amount/weights[max_index] )
    del values[max_index]
    value += value + optimal_value(capacity, weights, values)
    
    
    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
    
    
    
