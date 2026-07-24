class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Build graph
        graph = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses

        def dfs(course):
            # Cycle found
            if state[course] == 1:
                return False

            # Already checked
            if state[course] == 2:
                return True

            # Mark as visiting
            state[course] = 1

            # Visit all neighbors
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            # Mark as completely processed
            state[course] = 2
            return True

        # Check every course
        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(course):
                    return False

        return True