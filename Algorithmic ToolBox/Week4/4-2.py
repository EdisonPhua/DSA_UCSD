
def binary_search(keys, query):
    # write your code here
    minIndex = 0
    maxIndex = len(keys) - 1
    last_occurance = None
    
    while maxIndex >= minIndex:
        mid =  (minIndex +maxIndex)//2
        if keys[mid] == query:
            last_occurance = mid
            minIndex = mid + 1           
        elif keys[mid] <  query:
            minIndex = mid + 1
        elif keys[mid] > query:
            maxIndex = mid - 1
    if not last_occurance:
         return -1
    else:      
        return last_occurance
if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
