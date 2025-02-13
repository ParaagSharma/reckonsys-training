class Range:
    '''
        Custom implementation for range function
        using iterators
    '''
    
    
    def __init__(self, 
                 start: int, 
                 end: int, 
                 step: int,
            ) -> None:
        self.current = start
        self.end = (end - 1) if step > 0 else (end + 1)
        self.step = step
        
    def __iter__(self) -> None:
        return self 
        
    def __next__(self) -> int:
        if (self.current > self.end and self.step > 0) or \
            (self.current < self.end and self.step < 0):
            raise StopIteration
        else:
            x = self.current
            self.current += self.step
            return x
        
start = int(input('Enter start: '))
end = int(input('Enter end: '))
step = int(input('Enter step: '))

iterator = Range(start=start, end=end, step=step)

for i in iterator:
    print(i)


class FileRead:
    '''
        Reading file line by line using iterators
    '''
    
    
    def __init__(self, 
                 filename: str,
            ) -> None:
        self.file = open(filename.strip(), 'r')
        
    def __iter__(self) -> None:
        return self
    
    def __next__(self) -> str:
        line = self.file.readline()
        if not line:
            raise StopIteration
        return line

file = FileRead('hello.txt')

for line in file:
    print(line.strip())
    


class FlattenLists:
    '''
        Implement an iterator nested_iterator that takes a nested list 
        of numbers (i.e., a list of lists) and returns all the elements 
        in a flat structure. For example, given [[1, 2], [3, 4], [5]], 
        it should yield 1, 2, 3, 4, 5.
    '''
    
    def __init__(self, list: list) -> None:
        self.list = list
        self.list_num = 0
        self.i = 0
        self.output = []
        
    def __iter__(self) -> None:
        return self
    
    def __next__(self) -> int:
        if self.list_num >= len(self.list):
            raise StopIteration
        
        if self.i >= len(self.list[self.list_num]):
            self.list_num += 1
            self.i = 0
            return self.__next__()
        
        val = self.list[self.list_num][self.i]
        self.i += 1
        return val

        
list = [[1,2], [3,4], [5]]

iterator = FlattenLists(list)

output = []
for i in iterator:
    output.append(i)
    
print(output)    
