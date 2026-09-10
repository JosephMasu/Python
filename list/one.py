names = ['Elwood','Jake','Curtis']

print(names.index('Curtis'))

s = [10, 1, 7, 3]
s.sort()                    # [1, 3, 7, 10]

# Reverse order
s1 = [10, 1, 7, 3]
s1.sort(reverse=True)        # [10, 7, 3, 1]

# It works with any ordered data
s2 = ['foo', 'bar', 'spam']
s2.sort()                    # ['bar', 'foo', 'spam']

symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
symlist = symbols.split(',')
print(symlist[0])
print(symlist[1])
print(symlist[2])
print(symlist[3])
print(symlist[4])
print(symlist[5])
print(symlist[6])
print(symlist[-2]) # avant dernier element in the list 
print(symlist[-1]) # dernier element in the list 

# Try reassigning one value:

symlist[2] = 'AIG'
print(symlist[2])  
print(symlist)  # ['HPQ', 'AAPL', 'IBM', 'MSFT', 'YHOO', 'DOA', 'GOOG']

# Take a few slices:
print(symlist[0:3])

# Create an empty list and append an item to it.
mysyms = []
mysyms.append('MASU')
print(mysyms)  # ['MASU']

# You can reassign a portion of a list to another list. For example:
symlist[-2] = mysyms[0]
print(symlist)  # ['HPQ', 'AAPL', 'IBM', 'MSFT', 'MASU']

for sym in symlist:
    print(sym)

# Use the append() method to add the symbol 'RHT' to end of symlist.

symlist1 = []
symlist1.append('RHT')
print(symlist + symlist1)  # ['HPQ', 'AAPL', 'IBM', 'MSFT', 'MASU', 'RHT']

# Exercise 1.24: Putting it all back together
a = ','.join(symlist)
print(a)  

b = ':'.join(symlist)
print(b)

c = ''.join(symlist)
print(c)

print(s)
print(s1)
print(s2)
