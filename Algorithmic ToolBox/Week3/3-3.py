from sys import stdin


def min_refills(distance, tank, stops):
    stops.append(distance)
    last_refill=0
    dist=0
    num=0
    i=-1
    while(dist<distance):
        while(dist<distance and last_refill+tank>=stops[i+1] ):
            i+=1
            dist=stops[i]
        if dist==last_refill:
            return -1
        num+=1
        last_refill=dist
    num-=1
    return num


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
