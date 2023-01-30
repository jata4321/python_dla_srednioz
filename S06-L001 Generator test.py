import datetime


def combinations(product, promotion, customer):
    for p in product:
        for r in promotion:
            for c in customer:
                yield (p, r, c)


products = ["Product {}".format(i) for i in range(1, 4000)]
promotions = ["Promotion {}".format(i) for i in range(1, 2000)]
customers = ['Customer {}'.format(i) for i in range(1, 50)]

start = datetime.datetime.now()
for p in combinations(products, promotions, customers):
    pass
end = datetime.datetime.now()

print(end - start)
