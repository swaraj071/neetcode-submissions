class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses
        res = []

        def dfs(course):
            if state[course] == 1:
                return False      # cycle

            if state[course] == 2:
                return True       # already processed

            state[course] = 1

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            state[course] = 2
            res.append(course)    # append after processing all neighbors
            return True

        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(course):
                    return []

        return res[::-1]