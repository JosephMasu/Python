# dictionanry is a collection of pairs (key and values), ordered and changeable


capitals = {
    "USA": "Washington DC",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

# print(capitals.get("Germany"))
# print(capitals.keys())
# print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key, value)

# capitals.update({"Germany": "Berlin"})
# capitals.pop("China")
# capitals.clear()

# print(capitals)