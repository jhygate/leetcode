import copy

def minZeroArray(nums, queries):
    diffrence_arrays = get_differnce_arrays(nums, queries)
    print(diffrence_arrays)
    return binary_search(nums,diffrence_arrays)



def get_differnce_arrays(nums, queries):
    start_array = [0] * len(nums)

    difference_arrays = [start_array]
    total_sum = start_array

    for index1, index2, value in queries:
        new_array = [0] * len(nums)
        new_array[index1:index2+1] = [value] * ((index2+1)-index1)
        total_sum = [sum(x) for x in zip(total_sum,new_array)]

        difference_arrays.append(total_sum)

    return difference_arrays

def binary_search(nums, differnece_arrays):
    k = -1

    bottom = 0
    top = len(differnece_arrays)-1
    

    while bottom <= top:

        midpoint = (top+bottom)//2
        print(bottom,top, midpoint)

        print(sums(nums, differnece_arrays[midpoint]))
        

        if all_zeros(nums, differnece_arrays[midpoint]):
            top = midpoint -1
            k = midpoint
        else:
            bottom = midpoint + 1

    return k

    

    
def all_zeros(nums, difference):
    print(difference, nums)
    for num, val in zip(nums,difference):
        print(num, val, "v")
        if num > val:
            return False
    print("ITS TRUE")
    return True

def sums(nums, differnece):
    return [x[0] - x[1] for x in zip(nums,differnece)]


print(minZeroArray(nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]
))

