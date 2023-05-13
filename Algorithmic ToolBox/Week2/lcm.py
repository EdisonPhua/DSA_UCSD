import time
def lcm(a,b):
    start_time = time.time()
    
    mult = 1
    list = [a,b]
    list.sort()
    while True:       
        larg_number = list[1] * mult
        if larg_number % list[0] ==0:
            break
        else:
            mult += 1
            continue
        
    end_time = time.time()
    return (end_time -start_time), larg_number 
        
def lcm1(a, b):
    start_time = time.time()
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    assert False
    end_time = time.time()
    return (end_time -start_time), l
        


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))
    print(lcm1(a, b))