from itertools import chain


class Cake:
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)

    def __str__(self):
        return f'Kind: {self.kind}, name: {self.name}, additives: {self.additives}.'

    def __add__(self, other):
        new_additives = self.additives
        if type(other) == list:
            new_additives.extend(list(chain(other)))
        elif type(other) is str:
            new_additives.append(other)
        else:
            raise Exception('This is wrong type')
        return Cake(self.name, self.kind, self.taste, new_additives, self.filling)


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream')
print(cake01)

cake01 += ['salt', 'sugar']
print(cake01.show_info())
