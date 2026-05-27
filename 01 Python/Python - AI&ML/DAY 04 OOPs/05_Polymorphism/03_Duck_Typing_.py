class Duck:
    def quack(self):
        print("Quack! Quack!")

class Person:
    def quack(self):
        print("I'm pretending to be a duck - Quack! Quack!")

def make_it_quack(thing):
    # We don't check the type — we just call quack()
    thing.quack()

d = Duck()
p = Person()

make_it_quack(d)
make_it_quack(p)
# Both Duck and Person can "quack" even though they are different types