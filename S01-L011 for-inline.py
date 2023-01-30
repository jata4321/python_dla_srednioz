product = [{a: b} for a in range(1000) for b in range(5000) if a % 5 == 1 if b % 2 == 0]
print(product)

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

routs = list()
routs = [(port_a, port_b) for port_a in ports for port_b in ports if port_a != port_b]
print(routs)

routs = list()
routs = [(port_a, port_b) for port_a in ports for port_b in ports if port_a < port_b]
print(routs)
print(len(routs))
