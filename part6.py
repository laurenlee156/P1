class PeekableIterator:

    def __init__(self, iterable):
        self.iterable = iter(iterable) # initializes the iterator with the iterable

    def __iter__(self): # returns the iterator object
        return self

    def __next__(self):
        return next(self.iterable)

    def peek(self):
        # assign the next item in the iterable to next_elem
        next_elem = next(self.iterable)
        # create a new iterator that has next_elem and the rest of the elements
        # convert self.iterable to a list to add to [next_elem]
        new_iterator = iter([next_elem] + list(self.iterable)) # [1] + [2, 3]
        return next_elem, new_iterator

    def has_next(self):
        try:
            next(self.iterable)
            return True
        except StopIteration:
            return False

# a = PeekableIterator([1, 2, 3])
# next_elem, next_iterator = a.peek()






