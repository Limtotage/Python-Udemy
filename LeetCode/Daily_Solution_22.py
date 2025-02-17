class Daily_Solution_22:
    def solution_resolver(self, Count) ->int:
        total=0
        for i in range(26):
            if Count[i]:
                total+=1
                Count[i]-=1
                total+=self.solution_resolver(Count)
                Count[i]+=1
        return total

    def numTilePossibilities(self, tiles: str) -> int:
        Count = [0] * 26
        for ch in tiles:
            Count[ord(ch) - ord('A')] += 1
        return self.solution_resolver(Count)
