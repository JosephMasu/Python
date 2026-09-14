def test():
    print("A")
    yield 1
    print("B")
    yield 2
    print("C")

x = test()

print(next(x))
print(next(x))
print(next(x))


# for x in test():
#     print(x)

