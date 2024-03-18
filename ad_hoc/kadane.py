# https://leetcode.com/problems/maximum-subarray/
# Fun variant https://leetcode.com/problems/partition-array-for-maximum-sum/description/
def kadane_max_subarray_sum(nums):
	n = len(nums)
    max_current = max_global = nums[0]

    for i in range(1, n):
        max_current = max(nums[i], max_current + nums[i])
        if max_current > max_global:
            max_global = max_current

    return max_global

# https://leetcode.com/problems/maximum-product-subarray/
def kadane_max_subarray_product(nums):
    n = len(nums)
    max_so_far, max_ending, min_ending = nums[0], nums[0], nums[0]
    for i in range(1, n):
        current = max(nums[i], max_ending * nums[i], min_ending * nums[i])
        min_ending = min(nums[i], max_ending * nums[i], min_ending * nums[i])
        max_ending = current
        max_so_far = max(max_so_far, max_ending)
    return max_so_far
