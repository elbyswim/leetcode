class Solution:
    def intervalIntersection(self, A, B):
        i = j = 0
        intersections = []
        while i < len(A) and j < len(B):
            if A[i][1] < B[j][0]:
                i += 1
            elif B[j][1] < A[i][0]:
                j += 1
            else:
                intersections.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
                if A[i][1] < B[j][1]:
                    i += 1
                elif B[j][1] < A[i][1]:
                    j += 1
                else:
                    i += 1
                    j += 1
        return intersections


soln = Solution()
print(soln.intervalIntersection([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]))
