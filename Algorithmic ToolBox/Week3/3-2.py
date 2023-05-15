from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    
    val = []
    n = len(weights)
    for i in range(n):
        val.append((values[i]/weights[i], weights[i]))
    val.sort(reverse=True) #index 0 will be the highest cost firstD is cost, secondD is weights
    
    i = 0
    while capacity>0 and i<n:
        if capacity> val[i][1]:
            value += val[i][0]*val[i][1]
            capacity -= val[i][1]


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
    
    
    
