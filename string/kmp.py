# 3008. Find Beautiful Indices in the Given Array II
# https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-ii/description/
def kmp(search, target):
    ret = []
    if not target:
        return ret

    n = len(target)
    lps = [0 for i in range(n)]
    i, j = 0, 1
    while j < n:
        if target[i] == target[j]:
            lps[j] = lps[i] + 1
            i, j = i + 1, j + 1
        else:
            if i == 0:
                j += 1
            else:
                i = lps[i - 1]
    i, j = 0, 0
    while i < len(search):
        if search[i] == target[j]:
            i, j = i + 1, j + 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]
        if j == len(target):
            ret.append(i - j)
            j = lps[j - 1]
    return ret
