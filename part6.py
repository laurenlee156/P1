from itertools import tee
class PeekableIterator:

    def __init__(self, iterable):
        # initializes the iterator with the iterable
        self.iterable = iter(iterable)
        self.original = iterable

        # create a duplicate to not change the original iterator
        #self.iterable, self.peek_iter = tee(self.iterable)

    def __iter__(self): # returns the iterator object
        return self

    def __next__(self):
        return next(self.iterable)

    def peek(self):
        # get the next element in the iterator
        next_elem = next(self.iterable)
        self.iterable = iter(self.original)
        return next_elem

    def has_next(self):
        try:
            # get the next element in the iterator
            self.peek()
            return True
        except StopIteration:
            return False


# a = PeekableIterator([1, 2])
# # # a.peek()
# # print(a.has_next())
# # print(a.has_next())
# # print(a.has_next())






















