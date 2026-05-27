class product:
    l = []
    def __init__(self, name , price):
        self.name = name
        self.price = price
        product.l.append(self.name)
    
    @staticmethod
    def cal_discount(price, discount):
        
        final_price = price - (price * discount / 100)
        print(f"Price after {discount}% discount is : {final_price}")

    @classmethod
    def prodeut_details(self):
        print(product.l)
        print(f"Number of Prodects in Store : {len(product.l)}")

    
    
p1 = product("Laptop", 60000)
p2 = product("Smartphone", 30000)
p3 = product("Tablet", 25000)


product.prodeut_details()
p1.cal_discount(p1.price,10)

