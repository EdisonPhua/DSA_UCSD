def max_pairwise_product(numbers):
    sort = sorted(numbers, reverse=False)
    product = sort[0] * sort[1]
    return product
    

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
