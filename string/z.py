# https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/
def compute_z(s):
    Z = [0] * len(s)
    l, r, k = 0, 0, 0
    for i in range(1, len(s)):
        if i > r:
            l, r = i, i
            while r < len(s) and s[r] == s[r - l]:
                r += 1
            Z[i] = r - l
            r -= 1
        else:
            k = i - l
            if Z[k] < r - i + 1:
                Z[i] = Z[k]
            else:
                l = i
                while r < len(s) and s[r] == s[r - l]:
                    r += 1
                Z[i] = r - l
                r -= 1
    return Z
