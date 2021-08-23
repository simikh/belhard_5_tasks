"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Напишите программу, которая принимает текст и выводит два слова:
наиболее часто встречающееся и самое длинное.

можно решить с помощью циклов и переменных, но предпочтительней с
помощью модуля collections, используя collections.Counter
"""


def common_and_longest(text: str) -> tuple:
    words = text.split(" ")
    counter = {}
    for word in words:
        current_value = counter.setdefault(word, 0)
        counter[word] = current_value + 1

    common = words[0]
    for key, value in counter.items():
        if value > counter[common]:
            common = key

    longest = words[0]
    for i in counter.keys():
        if len(i) > len(longest):
            longest = i
    return common, longest


if __name__ == '__main__':
    assert common_and_longest(
        "привет пока ялюблюpython привет"
    ) == ('привет', 'ялюблюpython')
    print('Решено!')
