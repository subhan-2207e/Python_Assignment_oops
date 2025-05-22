class Person:

    def __init__(self , name):
        self.name = name

class Teacher(Person):

    def __init__(self, name , subject):
        super().__init__(name)
        self.subject = subject
    
t = Teacher("Subhan","python")

print(f"Name :- {t.name} & subject is {t.subject}")

        