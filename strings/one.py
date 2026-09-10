import re
symbols = 'AAPL IBM AA CAT MSFT'

# Membership testing
lwerer_symbols = symbols.lower()

print('ibm'.upper() in symbols.upper())  # True
print('GOOG' in symbols)                 # False
print('AAPL' in symbols)                 # True
print('aapl' in lwerer_symbols)          # True

# String methods
print(symbols.find('MSFT'))              # 16
print(symbols[13:17])                    # MSFT

symbols = symbols.replace('SCO', 'DOA')
print(symbols)                           # AAPL IBM AA CAT MSFT
text = 'Today is 3/27/2018. Tomorrow is 3/28/2018.'

re.findall(r'\d+/\d+/\d+', text)
['3/27/2018', '3/28/2018']

re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
'Today is 2018-3-27. Tomorrow is 2018-3-28.'

print(re.findall(r'\d+/\d+/\d+', text))
# ['3/27/2018', '3/28/2018']

print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
# Today is 2018-3-27. Tomorrow is 2018-3-28.

name = '   IBM   \n'
shares = 100
price = 91.1
print(f'\n{name.strip()} \n{shares} \nshares at ${price:.2f}')  # IBM 100 shares at $91.10

