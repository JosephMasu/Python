# with open("story.txt", "r") as file:
#     story = file.read()

# name = input("Enter a name: ")
# place = input("Enter a place: ")
# animal = input("Enter an animal: ")
# adjective = input("Enter an adjective: ")
# verb = input("Enter a verb: ")
# food = input("Enter a food: ")
# number = input("Enter a number: ")

# story = story.replace("{name}", name)
# story = story.replace("{place}", place)
# story = story.replace("{animal}", animal)
# story = story.replace("{adjective}", adjective)
# story = story.replace("{verb}", verb)
# story = story.replace("{food}", food)
# story = story.replace("{number}", number)

# print(story)

with open("story.txt", "r") as file:
    story = file.read()

words = ["name", "place", "adjective", "animal", "verb", "food", "number"]

for i, word in enumerate(words):
    answer = input(f"Enter a {word}: ")
    story = story.replace("{" + word + "}", answer)

print("\n" + story)