def lcm(a,b):
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
    return larg_number 
        

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))