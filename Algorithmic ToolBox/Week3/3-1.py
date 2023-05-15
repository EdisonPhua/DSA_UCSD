def change(money):
    # write your code here
    numCoins = 0
    
    while True:
        if money >= 10:
            money -= 10
            numCoins += 1
            continue
        elif money >=5:
            money -= 5
            numCoins += 1
            continue
        elif money >= 1:
            money -= 1
            numCoins +=1
            break
        
    return numCoins


if __name__ == '__main__':
    m = int(input())
    print(change(m))


