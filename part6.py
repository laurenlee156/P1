class PeekableIterator:

    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self): # returns an iterator
        return self.iterable

    def __next__(self):
        return next(self.iterable)

    def peek(self):
        # return the next item
        if self.iterable < 1:
            return next(self.iterable)
        else:
            raise StopIteration



    def has_next(self):
        pass
