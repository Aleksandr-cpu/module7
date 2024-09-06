class Product():

    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop():

    __file_name = 'product.txt'

    def get_products(self):
        product = []
        file = open(self.__file_name, 'r')
        lines = file.readlines()
        for line in lines:
            product.append(line)
        file.close()
        return product

    def add(self, *products):
        existing_products = self.get_products()
        existing_names = set(product.split(', ')[0] for product in existing_products)
        for product in products:
            if product.name not in existing_names:
                file = open(self.__file_name, 'a')
                file.write(str(product) + '\n')
                file.close()
            else:
                print(f'Продукт {product.name} уже есть в магазине')




s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())