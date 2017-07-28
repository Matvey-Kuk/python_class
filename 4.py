def bottom():
    return (yield 42)


def middle():
    return (yield from bottom())


def top():
    return (yield from middle())

gen = top()
value = next(gen)
print(value)
try:
    value = gen.send(value * 2)
except StopIteration as exc:
    value = exc.value
print(value)