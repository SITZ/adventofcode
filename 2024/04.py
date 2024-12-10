# Problem: https://adventofcode.com/2024/day/4

word_search = open("input.txt", "r").readlines()
word_search = [word.strip() for word in word_search]


def get_xmas_count():
    XMAS = 'XMAS'
    total_xmas_count = 0

    for i in range(len(word_search)):
        for j in range(len(word_search[0])):
            for i_delta in [-1, 0, +1]:
                for j_delta in [-1, 0, +1]:
                    if i_delta == 0 and j_delta == 0:
                        continue

                    word = ''
                    for index in range(len(XMAS)):
                        i_index = i + index * i_delta
                        j_index = j + index * j_delta
                        if any([i_index < 0, j_index < 0, i_index >= len(word_search), j_index >= len(word_search[i])]):
                            break
                        word += word_search[i_index][j_index]
                    total_xmas_count += (word == XMAS)

    return total_xmas_count


def get_x_mas_count():
    total_x_mas_count = 0

    for i in range(1, len(word_search) - 1):
        for j in range(1, len(word_search[i]) - 1):
            if word_search[i][j] != 'A':
                continue
            M_count, S_count = 0, 0
            for i_delta in [-1, +1]:
                for j_delta in [-1, +1]:
                    S_count += word_search[i + i_delta][j + j_delta] == 'S'
                    M_count += word_search[i + i_delta][j + j_delta] == 'M'

            total_x_mas_count += all([
                M_count == S_count == 2,
                word_search[i - 1][j - 1] != word_search[i + 1][j + 1],
                word_search[i + 1][j - 1] != word_search[i - 1][j + 1]
            ])

    return total_x_mas_count


print('XMAS count:', get_xmas_count())
print('X-MAS count:', get_x_mas_count())
