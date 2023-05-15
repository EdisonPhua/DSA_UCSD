from itertools import permutations
def IsBetter(a,b):
    a,b = str(a) , str(b)
    
    if int((a+b)) > int(b+a):
        return True
    else:
        return False

def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = []

    for permutation in permutations(numbers):
        
        if IsBetter("".join(permutation)):
            largest.append(permutation)

    return largest


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
