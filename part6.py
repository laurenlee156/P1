class PeekableIterator:

    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.next = next(self.iterable)

    def __iter__(self): # returns the iterator object
        return self

    def __next__(self):
        curr = self.next
        self.next = None
        if not curr:
            raise StopIteration
        else:
            try:
                self.next = next(self.iterable)
            except StopIteration:
                self.next = None
            return curr

    def peek(self):
        if self.next:
            return self.next
        else:
            raise StopIteration("No more elements to peek at.")

    def has_next(self):
        return bool(self.next)


# a = PeekableIterator([1, 2, 3])
# print("has next: ", a.has_next())
# print("peek: ",a.peek())
# print("next: ",next(a))
# print("has next: ", a.has_next())
# print("peek: ",a.peek())
# print("next: ",next(a))
# print("has next: ", a.has_next())
#
# print("peek: ",a.peek())
# print("next: ",next(a))
# print("has next: ", a.has_next())























