# Methods : ass , StatInstance , Clic Methods

class laptop:
    storage_Type = "SSD"

    def __init__(self,RAM,storage):
        self.RAM = RAM
        self.storage = storage

    # Instance Method : Can Access Both - Instance & Class Attributes
    def features(self):   # Instance Method
        print(f" RAM : {self.RAM} \n Storage : {self.storage} \n Storage Type : {laptop.storage_Type}")

    # Class Method : Can Access Only Class Attributes
    @classmethod
    def show_storage_type(cls):  # Class Method
        print(f" Storage Type : {cls.storage_Type}")
    
    # Static Method : Cannot Access Neither Instance Nor Class Attributes
    @staticmethod
    def cal_discount(price, discount):
       final_price = price - (price * discount / 100)
       print(f"Price after {discount}% discount is : {final_price}")

l1 = laptop("8GB","512GB")
l2 = laptop("16GB","1TB")
print("--------------------")
l1.features()
print("--------------------")
l1.show_storage_type()
laptop.show_storage_type()  # Can be called using Class Name also
print("--------------------")
l2.cal_discount(60000,10)
print("--------------------")