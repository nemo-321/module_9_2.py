# Создается список first_strings, содержащий строки.
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
#  Создается список second_strings с различными словами.
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
# С помощью спискового выражения first_result формируется список длин строк из first_strings, длина которых не меньше 5.

first_result = [len(x) for x in first_strings if len(x) >= 5]
print(first_result)
# Создается список second_result,содержащий кортежи  из строк first_strings и second_strings, у которых длины равны.
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
print(second_result)
# Составляется словарь third_result, в котором ключами являются строки из объединенного списка first_strings и
# second_strings с четной длиной, а значениями — их длины.
third_result = {x: len(x) for x in first_strings + second_strings if len(x) % 2 == 0}
print(third_result)
