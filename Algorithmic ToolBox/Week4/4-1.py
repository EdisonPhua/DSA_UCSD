def binary_search(keys, query):
    # write your code here
    minIndex = 0
    maxIndex = len(keys) - 1
    
    
    while maxIndex >= minIndex:
        mid =  int((minIndex +maxIndex)//2)
        if keys[mid] == query:
            return mid
        elif keys[mid] <  query:
            minIndex = mid + 1
        elif keys[mid] > query:
            maxIndex = mid - 1
    return -1
        
    
        



if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
