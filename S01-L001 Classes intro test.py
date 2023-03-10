cake_01 = dict(
    taste='vanilla',
    glaze='chocolate',
    text='Happy Birthday',
    weight=0.7)

cake_02 = dict(taste='tea',
               glaze='lemon',
               text='Happy Python Coding',
               weight=1.3)


def show_cake_info(cake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        cake['taste'], cake['glaze'], cake['text'], cake['weight']))


show_cake_info(cake_01)
show_cake_info(cake_02)

cake_list = [cake_01, cake_02]

for cake in cake_list:
    show_cake_info(cake)
