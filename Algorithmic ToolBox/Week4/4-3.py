def majority_element_naive(elements):
    total = len(elements)
    unique = set(elements)
    for num in unique:
        if elements.count(num) > total / 2:
            return 1

    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
