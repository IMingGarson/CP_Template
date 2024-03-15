def prefix_sum(nums):
    n = len(nums)
    prefix_sum_list = [nums[0]]
    for i in range(1, n):
        prefix_sum_list.append(prefix_sum_list[-1] + nums[i])
    return prefix_sum_list

# More Pythonic
# https://leetcode.com/problems/find-the-pivot-integer/description/

# NOTE: itertools.accumulate won't work on negative numbers
# https://leetcode.com/problems/range-sum-query-immutable/
n = len(nums)
prefix_sum_list = list(accumulate(range(1,n + 1),lambda x, y : x + y))
suffix_sum_list = list(accumulate(range(1,n + 1)[::-1],lambda x, y : x + y))[::-1]
