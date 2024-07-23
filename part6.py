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
            next_elem = next(self.iterable)
            print(next_elem)
            print(list(self.iterable))

            # modify self.peek_iter does not change self.iterable
            #new_iter = list(self.peek_iter)
            #print(new_iter)

            # check if there are elements left to iterate
            if len(list(self.iterable)) > 0:
                return True
            # else:
            #     return False
        except StopIteration:
            return False

        # elem = next(self.iterable)
        # print(elem)
        # return True
        # except StopIteration:
        #     return False

a = PeekableIterator([1, 2, 3, 4])
# # a.peek()
print(a.peek())
print(a.peek())
print(a.peek())






















