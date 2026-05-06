class Postman:
    def __init__(self):
        self.delivery_data = list()

    def add_delivery(self, street, house, flat):
        self.delivery_data.append((street, house, flat))

    def get_houses_for_street(self, street):
        result = [el[1] for el in self.delivery_data if el[0] == street]
        return result

    def get_flats_for_house(self, street, house):
        result = [el[2] for el in self.delivery_data if el[0] == street and el[1] == house]
        return result

postman = Postman()
postman.add_delivery('Советская', 15, 1)
postman.add_delivery('Советская', 15, 2)
postman.add_delivery('Советская', 20, 5)
postman.add_delivery('Ленина', 10, 8)

print(postman.get_houses_for_street('Советская'))   # [15, 15, 20]
print(postman.get_flats_for_house('Советская', 15)) # [1, 2]