import time


class Combinations:
    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers

    def __getitem__(self, item):
        if item >= len(self.products) * len(self.promotions) * len(self.customers):
            raise StopIteration()
        else:
            pos_products = item // (len(self.promotions) * len(self.customers))
            item = item % (len(self.promotions) * len(self.customers))

            pos_promotions = item // len(self.customers)
            item = item % len(self.customers)

            pos_customers = item

        return f'Combination of product, promotion, customer: {self.products[pos_products]}, ' \
               f'{self.promotions[pos_promotions]}, {self.customers[pos_customers]}'


products = ["Product {}".format(i) for i in range(1, 4)]
print(products)

promotions = ["Promotion {}".format(i) for i in range(1, 3)]
print(promotions)

customers = ['Customer {}'.format(i) for i in range(1, 6)]
print(customers)

combinations = Combinations(products, promotions, customers)

for i in range(0, 30):
    # here an analysis will be done - currently, just nothing happens :)
    print(i, combinations[i])

print('---------------------------')
ids = iter(combinations)
for i, k in enumerate(ids):
    print(i, k)
