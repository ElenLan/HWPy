def cash():
    return hours * payment + premium


hours = int(input('введите выработку в часах: '))
payment = int(input('введите оплату в час: '))
premium = int(input('введите размер премии: '))

cash()
