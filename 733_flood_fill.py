class Solution:
    def floodFill(self, image, sr, sc, newColor):
        if image[sr][sc] == newColor:
            return image
        height = len(image)
        length = len(image[0])
        color = image[sr][sc]
        from collections import deque
        queue = deque([[sr, sc]])
        while len(queue) > 0:
            r, c = queue.popleft()
            if image[r][c] != color:
                continue
            image[r][c] = newColor
            if r > 0:
                queue.append([r - 1, c])
            if r < height - 1:
                queue.append([r + 1, c])
            if c > 0:
                queue.append([r, c - 1])
            if c < length - 1:
                queue.append([r, c + 1])
        return image


soln = Solution();
print(soln.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
