class Solution(object):
    def floodFill(self, image, sr, sc, color):
        oldColor = image[sr][sc]
        rows= len(image)
        cols = len(image[0])
        if oldColor != color:
            self.dfs(sr,sc, rows, cols, image, color, oldColor)
        return image
    def dfs(self,sr, sc, rows , cols, image, newColor, oldColor):
        if sr<0 or sc<0 or sr>=rows or sc >=cols or image[sr][sc]!=oldColor:
            return
        image[sr][sc] = newColor
        self.dfs(sr-1, sc , rows, cols, image, newColor, oldColor)
        self.dfs(sr+1, sc , rows, cols, image, newColor, oldColor)
        self.dfs(sr, sc+1 , rows, cols, image, newColor, oldColor)
        self.dfs(sr, sc-1 , rows, cols, image, newColor, oldColor)
    