

groceries = ({'apple', 'banana', 'orange'},
             {'celery', 'carrots', 'potatoes'},
             {'checken', 'beef', 'fish'})

for collection in groceries:
    for food in collection:
        print(food, end=' ')
    print()