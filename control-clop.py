class Member:
    def __init__(self, name, post=None, x=0):
        self.name = name
        self.post = post
        self.salary = x

    def example(self, x):
        self.salary = x
        print('Оклад равен', round(self.salary) * 1.3)

    def __str__(self):
        return f'{self.name}: {self.post} \n{self.name}:{self.salary}'


class Manager(Member):
    def __init__(self, name,post, salary):
        super().__init__(name,post, salary)

    def example(self, x,y):
        self.salary *=x
        print('Зарплата c надбавками равна', round((self.salary * x) * y))


ivan = Manager('Ivan', 'Manager',1700)
ivan.example( 1.3,1.2)
print(ivan)
