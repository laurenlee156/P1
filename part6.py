from itertools import tee
class PeekableIterator:

    def __init__(self, iterable):
        # initializes the iterator with the iterable
        self.iterable = iter(iterable)

        # create a duplicate to not change the original iterator
        self.iterable, self.peek_iter = tee(self.iterable)

    def __iter__(self): # returns the iterator object
        return self

    def __next__(self):
        return next(self.iterable)

    def peek(self):
        # get the next element in the iterator
        next_elem = next(self.iterable) # 1, 2

        # modify self.peek_iter as it does not change self.iterable
        # new_iter = iter([next_elem] + list(self.peek_iter)) # iterable: [1] + [2, 3], [2] + [3]
        new_iterator = iter([next_elem] + list(self.iterable))
        return next_elem

    def has_next(self):
        # get the next element in the iterator
        next_elem = next(self.iterable)
        print(next_elem)

        # modify self.peek_iter does not change self.iterable
        new_iter = list(self.peek_iter) # iterable: [1] + [2, 3]
        print(new_iter)

        # check if there are elements left to iterate
        if len(new_iter) > 1:
            return True
        else:
            return False

        # try:
        #     elem = next(self.iterable)
        #     print(elem)
        #     return True
        # except StopIteration:
        #     return False

# a = PeekableIterator([1])
# # a.peek()
# print(a.has_next())
# print(a.has_next())
# print(a.has_next())
# print(a.has_next())





















