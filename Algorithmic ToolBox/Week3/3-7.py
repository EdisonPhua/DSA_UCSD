from itertools import permutations
def IsBetter(a,b):
    a,b = str(a) , str(b)
    
    if int((a+b)) > int(b+a):
        return int((a+b))
    else:
        return int(b+a)

def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, IsBetter(permutation))

    return largest


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
