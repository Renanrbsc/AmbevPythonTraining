def solution(A):
    A.sort()
    if len(A) == 1:
        return A[0]
    
    size = len(A)
    for i in range(0,size,2):
        if i == size - 1:
            return A[i]
        if A[i] != A[i + 1]:
            return A[i]

    # list_count = []
    # for i in A:
    #     list_count.append(A.count(i))
    # min_value = min(list_count)
    # index_list = list_count.index(min_value)
    # return A[index_list]

print(solution([9,3,9,3,9,7,9]))