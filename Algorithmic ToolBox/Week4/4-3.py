def majority_element_naive(elements):
    count = 0 
    candidate = None
    
    for number in elements:
        if not candidate:
            candidate == number
        


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
