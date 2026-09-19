
class Cat:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
        self.hunger = 50
        self.energy = 50

    def eat(self):
        self.hunger -= 20
        print(self.name, "поїв")

    def sleep(self):
        self.energy += 20
        print(self.name, "поспав")


cat1 = Cat("Мурчик", "сірий", age=2)

print(cat1.name)
print(cat1.color)
print(cat1.age)

cat1.eat()
cat1.sleep()


