class Dog:
    def __init__(self, name):
        self.name = name

    # getters and setters
    def get_dog_name(self):
        return self.name

    def set_dog_name(self, name):
        if type(name) != str:
            print('ERROR: Name must be a string')
            return
        self.name = name

    def bark(self):
        print("bark")


newDog = Dog("Fidi")

print(newDog.get_dog_name())
newDog.bark()
newDog.set_dog_name("Fido")
print(newDog.get_dog_name())