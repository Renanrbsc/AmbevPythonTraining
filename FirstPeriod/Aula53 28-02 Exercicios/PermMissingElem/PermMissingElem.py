def solution(A):
    size = len(A)
    counter = 0
 
    for index in range(size):
        counter += A[index]
        size += index + 1
 
    return size - counter + 1
    
print(solution([1,2,3,5]))