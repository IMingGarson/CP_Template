# Topological sort is for cycle detection. Need calculate number of indegress and keep track of nodes where indegress is 0
# https://leetcode.com/problems/parallel-courses/

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # could be -1 => cycle detection
        # courses w/o preq can be taken all at once => topological sort
        indegress = [0 for _ in range(n)]
        graph = defaultdict(list)
        for pre, nex in relations:
            indegress[nex - 1] += 1
            graph[pre - 1].append(nex - 1)

        dq = deque([])
        for i in range(n):
            if indegress[i] == 0:
                dq.append(i)

        res = 0
        while dq:
            for _ in range(len(dq)):
                current_course = dq.popleft()
                n -= 1
                for next_course in graph[current_course]:
                    indegress[next_course] -= 1
                    if indegress[next_course] == 0:
                        dq.append(next_course)
            res += 1
            if n == 0:
                return res
        return -1
