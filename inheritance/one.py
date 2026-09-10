class Animal:
    def __init__(self, breed):
        self.breed = breed

    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return f"I am a {self.breed}, and I bark!"

# Example usage
dog = Dog("Golden Retriever")
print(dog.speak())