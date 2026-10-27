def add(x, y, position):
    return position, (x + y) % 2


def subtract(x, y, position):
    return position, (x - y) % 2


def interaction(information):
    operator_number = information[0]
    x = information[information[1]]
    y = information[information[2]]
    position = information[3]

    operator = operators[operator_number]
    position, value = operator(x, y, position)
    information[position] = value


operators = [add, subtract]
interaction_operators = [interaction]
