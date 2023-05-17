def count_occurrences(list, element):
    return sum(1 for num in list if num == element)

def check_majority(list, left, right):
    if left == right:
        return list[left]

    mid = (left + right) // 2
    left_majority = check_majority(list, left, mid)
    right_majority = check_majority(list, mid + 1, right)

    if left_majority == right_majority:
        return left_majority
    elif left_majority is None:
        return right_majority
    elif right_majority is None:
        return left_majority

    left_count = count_occurrences(list[left:right+1], left_majority)
    right_count = count_occurrences(list[left:right+1], right_majority)

    if left_count > (right - left + 1) // 2:
        return left_majority
    elif right_count > (right - left + 1) // 2:
        return right_majority
    else:
        return None

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
