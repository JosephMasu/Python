import sys

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

y = map(lambda x: x**2, x)
# for i in y:
#     print(i)

# print(sys.getsizeof(y))  # size of the map object
# print(sys.getsizeof(list(y)))  # size of the list object


print(next(y))  # get the first element of the map object
print(next(y))  # get the first element of the map object
print(next(y))  # get the first element of the map object
print(next(y))  # get the first element of the map object  

print("For loop starts here")
for i in y:
    print(i)
