# https://leetcode.com/problems/longest-increasing-subsequence/description/
def lengthOfLIS(self, nums: List[int]) -> int:
    stack = []
    for n in nums:
        if len(stack) == 0 or stack[-1] < n:
            stack.append(n)
        else:
            idx = bisect_left(stack, n)
            stack[idx] = n

    return len(stack)
