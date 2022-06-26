import string

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_list = ["Are you sure? It is only one digit! (y / n)",
            "Don't be silly! It's just one number! Add to the memory? (y / n)",
            "Last chance! Do you really want to embarrass yourself? (y / n)"]
valid_chars = set(string.digits)
more_chars = {".", "M"}
valid_chars.update(more_chars)
M = 0


class EndLoop(Exception):
    pass


def string_to_sign(number1, sign, number2):
    if sign == "+":
        return number1 + number2
    elif sign == "-":
        return number1 - number2
    elif sign == "*":
        return number1 * number2
    else:
        return number1 / number2


def save_to_memory(number):
    print(msg_4)
    answer = input()
    if (answer == "n") or (answer == "y"):
        if answer == "y":
            if is_one_digit(number):
                count = 0
                while count < 3:
                    print(msg_list[count])
                    count += 1
                    answer2 = input()
                    if count == 3:
                        global M
                        M = number
                    elif answer2 == "n":
                        break
            else:
                M = number

    else:
        save_to_memory(number)


def continue_check():
    print(msg_5)
    cont_ask = input()
    if cont_ask == "n":
        raise EndLoop


def calculate(number1, number2):
    global M
    if (number1 == "M") and (number2 == "M"):
        result_calculate = string_to_sign(M, operator, M)
    elif number1 == "M":
        result_calculate = string_to_sign(M, operator, float(number2))
    elif number2 == "M":
        result_calculate = string_to_sign(float(number1), operator, M)
    else:
        result_calculate = string_to_sign(float(number1), operator, float(number2))
    return result_calculate


def is_one_digit(number1):
    return (float(number1).is_integer()) and (-10 < float(number1) < 10)


def check(number1, sign, number2):
    msg = ""
    msg_6 = " ... lazy"
    msg_7 = " ... very lazy"
    msg_8 = " ... very, very lazy"
    msg_9 = "You are"
    global M
    if number1 == "M":
        number1 = M
    if number2 == "M":
        number2 = M
    if (is_one_digit(number1)) and (is_one_digit(number2)):
        msg = msg + msg_6
    if ((float(number1) == 1.0) or (float(number2) == 1.0)) and (sign == "*"):
        msg = msg + msg_7
    if ((float(number1) == 0.0) or (float(number2) == 0.0)) and ((sign == "*") or (sign == "+") or (sign == "-")):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        return print(msg)


try:
    while True:
        print(msg_0)
        user_equation = input()
        x, operator, y = user_equation.split()
        check(x, operator, y)
        if any(char not in valid_chars for char in x):
            print(msg_1)
        elif any(char not in valid_chars for char in y):
            print(msg_1)
        elif operator not in ["+", "-", "*", "/"]:
            print(msg_2)
        else:
            try:
                result = calculate(x, y)
                print(result)
                save_to_memory(result)
                continue_check()
            except ZeroDivisionError:
                print(msg_3)
except EndLoop:
    pass
