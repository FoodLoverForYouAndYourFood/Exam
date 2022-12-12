# 18 задача
class Alchemy():
    def __init__(self, element):
        self.element = element

    def __add__(self, other):
        return Alchemy(self.element[0:3] + other.element[-3:])
    def hard_element(self,other):
        return Alchemy(self.element[0:3]*len(other.element))


element1 = Alchemy('Oxygen')
element2 = Alchemy('gold')
element3 = (element1 + element2)
element4 = hard_element
print(element3.element)
