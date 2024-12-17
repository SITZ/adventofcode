# Problem: https://adventofcode.com/2024/day/17

file = open('input.txt', 'r')

A = int(file.readline().split(':')[-1].strip())
B = int(file.readline().split(':')[-1].strip())
C = int(file.readline().split(':')[-1].strip())
file.readline()
program = list(map(int, file.readline().split(':')[-1].strip().split(',')))

print(A, B, C, program)


def get_output(register_a, register_b, register_c):
    def combo_operand(operand):
        match operand:
            case 0 | 1 | 2 | 3:
                return operand
            case 4:
                return register_a
            case 5:
                return register_b
            case 6:
                return register_c
            case 7:
                raise 'Invalid operand'

    output = []
    instruction_pointer = 0

    while True:
        instruction = program[instruction_pointer]
        operand = program[instruction_pointer + 1]
        match instruction:
            case 0:
                register_a = register_a // 2 ** combo_operand(operand)
            case 1:
                register_b = register_b ^ operand
            case 2:
                register_b = combo_operand(operand) % 8
            case 3:
                if register_a == 0:
                    break
                else:
                    instruction_pointer = operand
            case 4:
                register_b = register_b ^ register_c
            case 5:
                output.append(combo_operand(operand) % 8)
            case 6:
                register_b = register_a // 2 ** combo_operand(operand)
            case 7:
                register_c = register_a // 2 ** combo_operand(operand)

        if instruction != 3:
            instruction_pointer += 2

        if instruction_pointer + 1 >= len(program):
            break

    return output


print("Output:", ",".join(map(str, get_output(A, B, C))))


def get_register_a():
    candidate_a = sum(7 * 8 ** i for i in range(len(program) - 1)) + 1

    while True:
        output = get_output(candidate_a, 0, 0)

        if output == program:
            return candidate_a

        for i in range(len(output) - 1, -1, -1):
            if output[i] != program[i]:
                candidate_a += 8 ** i
                break


print('Register A:', get_register_a())
