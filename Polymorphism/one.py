# Example of Polymorphism in Python

class Laptop1:
    def build(self):
        print("Laptop building")
    
class Desktop1:
    def build(self):
        print("Desktop building")

class Alien:
    def code(self, machine: Laptop1):
        print("Alien building")
        machine.build()
    
Asur_rog = Laptop1()
beas=Desktop1()

masu = Alien()
masu.code(Asur_rog)  
masu.code(beas) 