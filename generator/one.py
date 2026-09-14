# Manually iterate over this list. Call __iter__() to get an iterator and call the __next__() method to obtain successive elements.

a = [1, 9, 4, 25, 16]

itarator = a.__iter__()

print(itarator.__next__())
print(itarator.__next__())
print(itarator.__next__())
print(itarator.__next__())
print(itarator.__next__())