import csv

with open('./cake_text_all.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # for row in csvreader:
    #     print('|'.join(row))

    # check existing object iterator
    # print(next(csvreader))
    # next(csvreader)
    # print(next(csvreader))

    # while true loop
    while True:
        try:
            print('-'.join(next(csvreader)))
        except StopIteration as e:
            print('Iteration reached an eof.')
            break
    print('Program run its course.')