## Teste Pycharm

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        ''' Retona Nome e idade da classe str'''
        return f"Pessoa de nome {self.name} com {str(self.age)} anos de idade."

if __name__ == "__main__":
    p1 = Person("Ricardo",45)
    str(p1)
