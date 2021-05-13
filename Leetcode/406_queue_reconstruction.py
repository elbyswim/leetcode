class Solution:
    def reconstructQueue(self, people):
        people.sort(key=lambda x: x[0])
        queue = [None] * len(people)
        for person in people:
            i = j = 0
            while j < person[1]:
                j += 1 if queue[i] is None or queue[i][0] >= person[0] else 0
                i += 1
            while queue[i] is not None:
                i += 1
            queue[i] = person
        return queue


test = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
soln = Solution()
print(soln.reconstructQueue(test))

segments = [[[0, 1], [1.0, 1.0]],
            [[0, 0, 0], [1.0, 0.5, 0.0]],
            [[0, 0.75], [0.5, 0.5]],
            [[0, 1], [0.0, 0.0]],
            [[1.5, 1.5, 1.5], [1.0, 0.5, 0.0]],
            [[2, 2, 2], [1.0, 0.5, 0.0]],
            [[2, 2.1, 2.5, 2.9, 2.9, 2.5, 2], [0.0, 0.25, 0.425, 0.35, 0.15, 0.05, 0.0]],
            [[3.25, 3.75, 4.25], [0.25, 0.25, 0.25]],
            [[4.25, 4, 3.75, 3.4, 3.25, 3.4, 3.75, 4], [0.25, 0.4, 0.5, 0.4, 0.25, 0.075, 0.0, 0.05]],
            [[4.5, 4.5, 4.5], [0.5, 0.25, 0.0]],
            [[4.5, 4.5, 4.6, 5, 5.3], [0.0, 0.25, 0.375, 0.425, 0.4]],
            [[5.6, 6, 6.4], [0.5, 0.5, 0.5]],
            [[6, 6, 6], [1.0, 0.5, 0.0]]]
