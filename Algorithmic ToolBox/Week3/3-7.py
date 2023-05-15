

import sys

def largest_number(a,n):
    #write your code here
    res = ""
    while(a):
        maxi=a[0]
        maxindex=0
        for i,each in enumerate(a):
            if IsGreaterOrEqual_v2(each,maxi):
                maxi=each
                maxindex=i
        res += maxi
        del a[maxindex]
    return res

def IsGreaterOrEqual_v2(A,B):
    return int(A+B)>int(B+A)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    n=int(data[0])
    a = data[1:]
    print(largest_number(a,n))
    