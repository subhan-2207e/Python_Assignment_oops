class Dog:

    def __init__(self, name , breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is says Woof !")

d = Dog("Rex" , "German shperd")
# print(d.name)

d.bark()
        