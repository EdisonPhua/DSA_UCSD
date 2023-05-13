def lcm(a,b):
    mult = 1
    list = [a,b]
    list.sort()
    while True:       
        larg_number = list[1] * mult
        if larg_number % list[0] ==0:
            return larg_number 
            break
        else:
            mult += 1
            continue
        
        
def lcm1(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    assert False
            
        


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))