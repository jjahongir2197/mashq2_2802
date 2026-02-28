class Product:
    def __init__(self, name, qty):
        self.name = name
        self.qty = qty

class Warehouse:
    def __init__(self):
        self.products = []

    def add_product(self, name, qty):
        self.products.append(Product(name, qty))

    def update(self, name, qty):
        for p in self.products:
            if p.name == name:
                p.qty += qty
                return

    def show(self):
        print("\n--- Ombor ---")
        for p in self.products:
            print(p.name, "-", p.qty)

def run():
    w = Warehouse()

    while True:
        print("\n1. Qo‘shish\n2. Yangilash\n3. Ko‘rish\n4. Chiqish")
        c = input("Tanlang: ")

        if c == "1":
            w.add_product(input("Nomi: "), int(input("Soni: ")))
        elif c == "2":
            w.update(input("Nomi: "), int(input("Qo‘shiladigan: ")))
        elif c == "3":
            w.show()
        else:
            break

run()
