# 1) Создать переменную типа String
item_str = 'homework1'
# 2) Создать переменную типа Integer
item_int = 5
# 3) Создать переменную типа Float
item_float = 0.5
# 4) Создать переменную типа Bytes
item_bytes = bytes('abcd', encoding='utf_8')
# 5) Создать переменную типа List
item_list = list([1, 2])
# 6) Создать переменную типа Tuple
item_tuple = tuple([1, 2, 3])
# 7) Создать переменную типа Set
item_set = set('ice')
# 8) Создать переменную типа Frozen set
item_frozenset = frozenset('ice')
# 9) Создать переменную типа Dict
item_dict = dict({'one': 32, 'two': 23})
# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных
# Первый вариант:
print('item_str =', item_str, type(item_str))
print('item_int =', item_int, type(item_int))
print('item_float =', item_float, type(item_float))
print('item_bytes =', item_bytes, type(item_bytes))
print('item_list =', item_list, type(item_list))
print('item_tuple =', item_tuple, type(item_tuple))
print('item_set =', item_set, type(item_set))
print('item_frozenset =', item_frozenset, type(item_frozenset))
print('item_dict =', item_dict, type(item_dict))

# Второй вариант:
a = ['item_str', 'item_int', 'item_float', 'item_bytes', 'item_list', 'item_tuple', 'item_set', 'item_frozenset', 'item_dict']
for i in a:
    print(i, type(i))

# q = dict({1: type, })
# print('a_1 =', type(a_1))
# a_1:, 2: b_2, 3: c_3, 4: d_4, 5: e_5, 6: f_6, 7: g_7, 8: h_8, 9: j_9
# k_10 = list([a_1, b_2, c_3, d_4, e_5, f_6, g_7, h_8, j_9])
# import string
# l_11 = str(string.ascii_letters)
# for q in range(len(k_10)):
#     print((l_11[q]), 'type', type(k_10[q]))


# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
item_1 = 'ice'
item_2 = 'cream'
skan_3 = item_1 + item_2
print('skan_3 = ', skan_3, type(skan_3))

# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
item_1 = 'east'
item_2 = 17
skan_3 = item_1, item_2
print(skan_3)

print(7, 'up', sep=',')

# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(str(7) +" "+ 'up')
