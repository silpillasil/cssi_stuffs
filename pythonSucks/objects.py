aishani_dict = {'name': 'Aishani',
                'age': 18,
                'adult': True,
                'hobbies': ['drawing', 'eating', 'sleeping']}

class Person(object):
    def __init__(self, name, age, adult, hobbies):
        self.name = name
        self.age = age
        self.adult = adult
        self.hobbies = hobbies
        self.hungry = True
    def eat(self, food):
        print('nom nom nom')
        self.hungry = False
    def give_birth(self, child_name):
        return Person(child_name, 0, False, ['screaming and crying'])
    def __str__(self):
        return ''



aishani = Person('Aishani', 18, True, ['drawing', 'eating', 'sleeping'])
random_person = Person('Jenny', 22, True, ['eating'])
random_beb = random_person.give_birth("Anna")
