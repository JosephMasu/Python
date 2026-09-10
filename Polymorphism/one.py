# Example of Polymorphism in Python

class Laptop1:
    def build(self):
        print("Laptop building")
    
class Desktop1:
    def build(self):
        print("Desktop building")
# Ducktyping
class Tablet1:
    def open_pdf(self):
        print("Opening PDF on Tablet")

class Alien:
    def code(self, machine: Laptop1):
        print("Alien building")
        machine.build()
    
Asur_rog = Laptop1()
beas = Desktop1()
lenovo = Tablet1()

masu = Alien()
masu.code(Asur_rog)  
masu.code(beas) 
masu.code(lenovo)  # This will raise an error since Tablet1 does not have a build method