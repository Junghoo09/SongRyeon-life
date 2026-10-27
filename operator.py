def add(x, y, position):
    return position, (x + y) % 2


def subtract(x, y, position):
    return position, (x - y) % 2


def interaction(information):
    operator_slot, x_slot, y_slot, position_slot = information[:4]

    operator_number = information[operator_slot]
    if not operators:
        print("등록된 연산자가 없습니다.")
        return
    operator_number = operator_number % len(operators)

    x = information[information[x_slot]]
    y = information[information[y_slot]]
    position = information[position_slot]

    operator = operators[operator_number]
    position, value = operator(x, y, position)
    information[position] = value


operators = [add, subtract]
interaction_operators = [interaction]
