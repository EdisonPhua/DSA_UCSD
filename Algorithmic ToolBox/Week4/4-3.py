def majority_element_naive(elements):
    count = 0 
    candidate = None
    
    for number in elements:
        if count == 0:
            candidate == number
            count += 1
        elif number == candidate:
            count += 1
        else:
            count -= 1
            
    if count >0:
        return 1 
    else:
        return 0
        


if __name__ == '__main__':
    input_n = float(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
