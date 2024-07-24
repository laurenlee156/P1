class PeekableIterator:

    def __init__(self, iterable):
        # initializes the iterator with the iterable
        # self.iterable = iter(iterable)
        # assigns self.original as the parameter iterable
        self.array = iterable

    def __iter__(self): # returns the iterator object
        return self

    def __next__(self):
        if not self.array:
            raise StopIteration
        return self.array.pop(0)
        # return next(self.iterable)

    def peek(self):
        if self.array:
            return self.array[0]
        else:
            raise StopIteration

    def has_next(self):
        return len(self.array) != 0


# a = PeekableIterator([1, 2])
# print("has next: ", a.has_next())
# print("peek: ",a.peek())
# print("next: ",next(a))
# print("has next: ", a.has_next())
# print("peek: ",a.peek())
# print("next: ",next(a))
# print("has next: ", a.has_next())
# print("peek: ",a.peek())
























