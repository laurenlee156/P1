from itertools import tee
class PeekableIterator:

    def __init__(self, iterable):
        # initializes the iterator with the iterable
        self.iterable = iter(iterable)
        self.original = iterable

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
        # if len(list(self.iterable)) > 0:
        #     return True
        # else:
        #     return False
        try:
            next_elem = next(self.iterable)
            self.iterable = iter(self.original)
            return True
        except StopIteration:
            self.iterable = iter(self.original)
            return False

# a = PeekableIterator([1, 2])
# # # # a.peek()
# # print(a.__next__())
# # print(a.__next__())
# # print(a.__next__())
# print(a.has_next())
# print(a.has_next())
# print(a.has_next())
# print(a.has_next())






















