from itertools import combinations


def inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions

def count_inversions(array):
    if len(array) <= 1:
        return array, 0
    
    mid = len(array) // 2
    left, inv_left = count_inversions(array[:mid])
    right, inv_right = count_inversions(array[mid:])
    merged, inv_merge = merge_and_count(left, right)

    return merged, inv_left + inv_right + inv_merge


def merge_and_count(left, right):
    merged = []
    inversions = 0
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inversions += len(left) - i

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inversions

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(inversions_naive(elements))
    print(count_inversions(elements))
