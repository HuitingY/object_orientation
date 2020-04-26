#object: complex data; orientation: structured, create data quickly.
#same as excel: creat column(format),then fill up it!
class Person:
    #define the atribute of 'object'
    def __init__(self, n, h, w):
        self.name = n
        self.height = h
        self.weight = w
    #define method
    def return_bmi(self):
        return self.weight / (self.height / 100) ** 2
    def is_over_weight(self):
        if self.weight >= 100:
            return True
        else:
            return False

p1 = Person("Tom", 175, 75)
print(p1.name, p1.return_bmi())
print("over weight:", p1.is_over_weight())

p2 = Person("Bob", 180, 80)
print(p2.name, p2.return_bmi())
