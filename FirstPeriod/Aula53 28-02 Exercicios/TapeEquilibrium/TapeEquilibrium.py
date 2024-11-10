
# Codility test 15% Performance
def solution(A):          
    sum_list = sum(A)
    list_that_ignores_the_last_value = A[:-1]
    sum_with_next_element = A[0]
    absolute_values_list = []
    for index, element in enumerate(list_that_ignores_the_last_value):
        if index != 0:
            sum_with_next_element += A[index]
        print(sum_with_next_element)
        sum_list_without_element = sum_list - element
        absolute_values_list.append(abs(sum_with_next_element - sum_list_without_element))       
        min_value = min(absolute_values_list)
    return min_value

print(solution([3,1,2,4,3]))

# Codility test 53% Performance
def solution(A):          
    sum_list = sum(A)
    list_that_ignores_the_last_value = A[:-1]
    sum_with_next_element = 0
    absolute_values_list = []
    for element in list_that_ignores_the_last_value:
        sum_with_next_element += element
        absolute_values_list.append(abs(sum_list - 2*sum_with_next_element))       
        min_value = min(absolute_values_list)
    return min_value

print(solution([3,1,2,4,3]))

# Codility test 100% Performance
def solution(A):          
    sum_list = sum(A)
    infinity_number = float('inf')
    sum_with_next_element = 0
    for i in A[:-1]:
        sum_with_next_element += i
        infinity_number = min(abs(sum_list - 2*sum_with_next_element), infinity_number)
    return infinity_number

print(solution([3,1,2,4,3]))
