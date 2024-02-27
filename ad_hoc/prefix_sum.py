def prefix_sum(nums):
    n = len(nums)
    prefix_sum_list = [nums[0]]
    for i in range(1, n):
        prefix_sum_list.append(prefix_sum_list[-1] + nums[i])
    return prefix_sum_list
