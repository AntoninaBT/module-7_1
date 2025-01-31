# Teplova
class Product :
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        prod = str(f"{self.name}, {self.weight}, {self.category}")
        return prod

class Shop:
    def __init__(self):
        self.__file_name = open('products.txt', 'a')
        self.__file_name.close()

    def get_products(self):
        get_file = open('products.txt', 'r')
        name_prod = get_file.read()
        get_file.close()
        return name_prod
    def add(self, *products):
        for i in products:
            if str(i) not in self.get_products():
                file = open('products.txt', 'a+')
                file.write(f'{str(i)}\n')
                file.close()
            else:
                print(f'Продукт {i} уже есть в магазине')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())