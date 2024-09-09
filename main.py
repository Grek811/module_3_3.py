def print_params(a=1, b='строка', c=True):
    """Функция для вывода параметров."""
    print(a, b, c)
print("Вызовы функции с разным количеством аргументов:")
print_params()
print_params(10)
print_params(10, 'текст')
print_params(10, 'текст', False)
print_params(b=25)
print_params(c=[1, 2, 3])
print("\nРаспаковка параметров из списка и словаря:")
values_list = [3.14, 'hello', False]
values_dict = {'a': 100, 'b': 'dict_value', 'c': None}
print_params(*values_list)
print_params(**values_dict)
print("\nРаспаковка + отдельные параметры:")
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)