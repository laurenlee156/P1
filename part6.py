class PeekableIterator:

    def __init__(self, iterable):
        # initializes the iterator with the iterable
        self.iterable = iter(iterable)
        # assigns self.original as the parameter iterable
        self.original = iterable

    def __iter__(self): # returns the iterator object
        return self

    def __next__(self):
        return next(self.iterable)

    def peek(self):
        # get the next element in the iterator
        next_elem = next(self.iterable)
        # reverts the change
        self.iterable = iter(self.original)
        return next_elem

    def has_next(self):
        try:
            if self.peek():
                return True
        except StopIteration:
            #self.iterable = iter(self.original)
            return False


# a = PeekableIterator([1])
# print(a.peek())
# print(a.has_next())
# print(a.has_next())
























