rules = dict()

valid_middle_page_sum = 0
invalid_middle_page_sum = 0

for line in open('input.txt', 'r'):
    if line.strip() == '':
        continue

    elif '|' in line:
        X, Y = map(int, line.split('|'))
        if X not in rules:
            rules[X] = set()
        rules[X].add(Y)

    elif ',' in line:
        pages_seen = set()
        pages = list(map(int, line.split(',')))

        is_order_incorrect = False
        for page in pages:
            is_order_incorrect |= page in rules and pages_seen.intersection(rules[page]) != set()
            pages_seen.add(page)

        print('is_order_incorrect', is_order_incorrect)

        if not is_order_incorrect:
            valid_middle_page_sum += pages[len(pages) // 2]
        else:
            for i in range(len(pages) - 1, -1, -1):
                for j in range(i - 1, -1, -1):
                    if pages[i] in rules and pages[j] in rules[pages[i]]:
                        pages[i], pages[j] = pages[j], pages[i]
            invalid_middle_page_sum += pages[len(pages) // 2]

print('valid_middle_page_sum', valid_middle_page_sum)
print('invalid_middle_page_sum', invalid_middle_page_sum)
