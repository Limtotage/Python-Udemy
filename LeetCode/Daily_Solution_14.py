class NumberContainers(object):
    def __init__(self):
        self.IndexToNumber={}
        self.NumberToIndex=defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:
        if index in self.IndexToNumber:
            if self.IndexToNumber[index]==number: 
                return 
            preVal=self.IndexToNumber[index]
            self.NumberToIndex.get(preVal).remove(index)
        
        self.NumberToIndex[number].add(index)
        self.IndexToNumber[index]=number
        

    def find(self, number: int) -> int:
        if number not in self.NumberToIndex or not self.NumberToIndex[number]:
            return -1
        return self.NumberToIndex[number][0]
