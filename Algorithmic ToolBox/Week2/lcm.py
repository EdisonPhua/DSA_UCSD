def lcm(a,b):
    mult = 1
    while True:
        number = max(a,b)
        number_mult = number * mult
        if number % 
        


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))