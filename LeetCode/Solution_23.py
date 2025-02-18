class Solution_23:
    def smallestNumber(self, pattern: str) -> str:
        stack = deque()
        result=""
        for i in range(len(pattern)+1):
            stack.append(i+1)
            if i==len(pattern) or pattern[i]=='I':
                while stack:
                    result+=str(stack.pop())
        return result
