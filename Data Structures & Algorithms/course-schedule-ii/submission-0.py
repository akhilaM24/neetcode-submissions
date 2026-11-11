from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Script: Build the graph. Each course points to the courses that depend on it.
        adj = [[] for _ in range(numCourses)]
        # Script: Track how many unmet prerequisites each course still has.
        in_degree = [0] * numCourses

        # Script: For each pair [a, b], course b must come before course a.
        for course, prereq in prerequisites:
            # Script: Add an edge from prereq to course.
            adj[prereq].append(course)
            # Script: course has one more unmet prerequisite.
            in_degree[course] += 1

        # Script: Start the queue with courses that have no prerequisites.
        queue = deque(i for i in range(numCourses) if in_degree[i] == 0)
        # Script: This list records the order we can take courses in.
        order = []

        # Script: Process courses in BFS order.
        while queue:
            # Script: Take a course that is ready to be taken.
            node = queue.popleft()
            order.append(node)
            # Script: Taking this course satisfies one prerequisite for each dependent.
            for nxt in adj[node]:
                in_degree[nxt] -= 1
                # Script: If a dependent has no remaining prerequisites, it is ready.
                if in_degree[nxt] == 0:
                    queue.append(nxt)

        # Script: If we could not order every course, a cycle blocks some of them.
        if len(order) != numCourses:
            return []
        return order