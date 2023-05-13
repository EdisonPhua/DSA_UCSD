def lcm(a,b):
    mult = 1
    list = [a,b]
    while True:
        list.sort()
        larg_number = list[1] * mult
        if large_number % list[0] ==0:
            return larg_number 
            continue
        else:
            break
            
        


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))