class base:
    def show(self):
        print("Base class show method called")
class derived(base):
    def show(self):
        print("Derived class show method called")


obj_derived = derived()
obj_derived.show()     # Output: Derived class show method called
                       # Base class show method is overridden