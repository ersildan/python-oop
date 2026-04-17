class Cat:
    def say(self):
        print('Мяу амзмафака!')

    def eat(self, meal):
        print(f'{meal}, - вкусно!')

cat = Cat()

cat.say() # знакомый вид
Cat.say(cat) # как работает на самом деле

