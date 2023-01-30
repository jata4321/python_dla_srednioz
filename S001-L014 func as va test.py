from datetime import datetime


def tcounter(kind='d'):

    s = 1
    m = s * 60
    h = m * 60
    d = h * 24

    source = ''' 
def duration(start, koniec):
    trwanie = datetime.strptime(koniec, '%Y-%m-%d') - datetime.strptime(start, '%Y-%m-%d')
    return(trwanie.total_seconds()/{})
'''.format(eval(kind))
    exec(source, globals())
    return duration


f_days = tcounter('d')
print(f_days('2022-01-01', '2022-12-01'))
