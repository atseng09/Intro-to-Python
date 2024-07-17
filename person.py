#%%
class Person:
    def __init__(self,name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def change_address(self,new_address):
        self.address = new_address

    def birthday (self):
        self.age += 1
#%%
        
person = Person(
    name= "Alison",
    age = 17,
    address= "Greenwich, Connecticut"
)
person2 = Person(
    name="Renee",
    age = 16,
    address= "Cos Cob, Connecticut"
)

#%%
class Child(Person):
    def __init__(self, name, age, address, parent):
        super().__init__(name, age, address)
        self.parent = parent

#%%
child = Child(name = "Sharone", age = 16, address = "Portchester, NY", parent =person)
print(child.parent.name)

#%%
class Animal:
    def __init__ (self, name, num_legs, type):
        self.name = name
        self.num_legs = num_legs
        self.type = type

# class Dog(Animal):
#     def __init__(self, name, type):
