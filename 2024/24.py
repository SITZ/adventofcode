# Problem: https://adventofcode.com/2024/day/23

values = {}
operations = {}
for line in open('input.txt'):
    if not line:
        continue
    elif ': ' in line:
        gate, value = line.strip().split(': ')
        values[gate] = int(value)
    elif ' -> ' in line:
        operation, gate = line.strip().split(' -> ')
        operations[gate] = operation


def evaluate(gate):
    if gate in values:
        return values[gate]

    operation = operations[gate]
    if ' AND ' in operation:
        a, b = operation.split(' AND ')
        value = evaluate(a) & evaluate(b)
    elif ' OR ' in operation:
        a, b = operation.split(' OR ')
        value = evaluate(a) | evaluate(b)
    elif ' XOR ' in operation:
        a, b = operation.split(' XOR ')
        value = evaluate(a) ^ evaluate(b)

    values[gate] = value
    return value


z_gates = sorted([gate for gate in operations.keys() if gate.startswith('z')])
z_value = 0
for z_index in range(len(z_gates)):
    z_value += evaluate(z_gates[z_index]) * (1 << z_index)

print(f'Part-1: {z_value}')
