def eager_range(up_to):
    sequence = []
    index = 0
    while index < up_to:
        sequence.append(index)
        index += 1
    return sequence


class IteratedRange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


def generator_range(up_to):
    index = 0
    while index < up_to:
        yield index
        index += 1

print(eager_range(10))
print(list(IteratedRange(10)))
print(list(generator_range(10)))
