netto = 1230
brutto = 1000


def proces_invoice(net, gross):
    if net > gross:
        raise ValueError("Net is higher than gross")
    else:
        print('Invoice is being processed.')


try:
    proces_invoice(netto, brutto)
except ValueError as e:
    print('Error, error, error!', e)


print('Thank you for using our software')
