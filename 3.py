def lazy_range(up_to):
    index = 0

    def gratuitous_refactor():
        nonlocal index
        while index < up_to:
            yield index
            index += 1

    yield from gratuitous_refactor()

print(list(lazy_range(10)))