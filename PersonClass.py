

class Person(object):
    def __init__(self, age, height, yourName):
        self.age1 = age
        self.height1 = height
        self.yourName1 = yourName

    def showMe(self):
        print(
            f'Hi {self.yourName1} , Age is {self.age1} and Height is {self.height1}')


# tom = Person(18, 173, 'tom')

# tom.showMe()
