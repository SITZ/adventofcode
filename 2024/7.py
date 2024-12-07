import re


def evaluate_expression(total, inputs, current_total=-1):
    if not inputs:
        return total == current_total

    if current_total == -1:
        return evaluate_expression(total, inputs[1:], inputs[0])
    else:
        return any([
            evaluate_expression(total, inputs[1:], current_total * inputs[0]),
            evaluate_expression(total, inputs[1:], current_total + inputs[0]),
            evaluate_expression(total, inputs[1:], int(str(current_total) + str(inputs[0])))
        ])


total_calibration = 0
for line in open('input.txt', 'r'):
    equation = list(map(int, re.split('[: ]{1,2}', line.strip())))

    if evaluate_expression(equation[0], equation[1:]):
        total_calibration += equation[0]

print('total_calibration', total_calibration)
