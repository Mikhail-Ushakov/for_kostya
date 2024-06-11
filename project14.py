class man:
    def __init__(self,name,growth):
        self.name=name
        self.growth=growth
        self.eyes=2
    def walk(self):
        print(f"{self.name} идет")
    def eating(self,food):
        print(f"{self.name} ест {food}")
    def __add__(self,other):
        return f"{self.name} и {other.name} Образовали пару"
        
chel1=man(name="Oleg",growth=185)
print(chel1)

chel2=man(name="Alex",growth=190)
print(chel2)
print(chel2.eyes)
chel1.profession="Инженер"
print(dir(chel1))
print(chel1.__dict__)
chel2.walk()
chel2.eating("Салат")
print(chel1 + chel2)