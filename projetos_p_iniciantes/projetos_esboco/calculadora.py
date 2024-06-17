def operacao(args):
    if args[1] == "+":
        return float(args[0]) + float(args[2])
    elif args[1] == "-":
        return float(args[0]) - float(args[2])
    elif args[1] == "*":
        return float(args[0]) * float(args[2])
    if args[1] == "/":
        return float(args[0]) / float(args[2])
    else:
        print("Invalid!")


def calculator(args):
    new_list = []
    result = 0
    for value in args:
        new_list.append(value)
        if len(new_list) == 3:
            result = operacao(new_list)
            new_list = []
            new_list.append(result)
    return result


values = []

while True:
    value = input("Insert a number or equal for calculate the result: ")

    if value != "=":
        values.append(value)
    else:
        print(f"Result = {calculator(values)}")
        break
