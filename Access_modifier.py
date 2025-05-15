class Employess:

    def __init__(self , name , salary , ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

emp = Employess("Subhan" , 6000 , "03090050458")

print(emp.name)
print(emp._salary)
print(emp.__ssn)