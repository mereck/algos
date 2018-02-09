    def md(self, i, j):
        
        if not self.x and not self.y:
            return 0
        
        if i == len(self.x):
            return len(self.y) - j
        
        if j == len(self.y):
            return len(self.x) - i
        

        if (i+1, j+1) not in self.memo:
            self.memo[(i+1, j+1)] = self.md(i+1, j+1)
        
        if self.x[i] == self.y[j]:
            return self.memo[(i+1,j+1)]
        
        if (i, j+1) not in self.memo:
            self.memo[(i, j+1)] = self.md(i, j+1)
            
        if (i+1, j) not in self.memo:
            self.memo[(i+1, j)] = self.md(i+1, j)
            
        if (i+1, j+1) not in self.memo:
            self.memo[(i+1, j+1)] = self.md(i+1, j+1)
        
        return min(1 + self.memo[(i, j+1)], 1 + self.memo[i+1, j], 1 + self.memo[i+1, j+1])
    
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        
        subproblem: x[i:] and y[j:] for all i, j
        guess: ins y[j] into x, del x[i] or replace x[i] with y[j]
        recurrence: md(i,j) = min(1 + md(i,j+1),1 + md(i+1,j),1 + md(i+1,j+1))
        
        """
        self.memo = {}
        self.x = word1
        self.y = word2
        return self.md(0,0) 
