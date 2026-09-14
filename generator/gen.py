def numbers():
    yield 1
    yield 2
    yield 3
values = numbers()
# print(next(values))
# print(next(values))
# print(next(values))

# or

for value in numbers():
    print(value)