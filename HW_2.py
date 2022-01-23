import math

item_1 = 4
print('item_1 =', item_1, type(item_1))

#2 Создать переменную item_2 типа integer
item_2 = 5
print('item_2 =', item_2, type(item_2))

#3 Создать переменную result_sum в которой вы суммируете item_1 и item_2
result_sum = item_1 + item_2
#4 Вывести result_sum в консоль
print('result_sum =', result_sum, type(result_sum))

#5 Создать переменную result_subtr в которой вы вычитаете большую по значению переменную из меньшей по значению.
result_subtr = item_2 - item_1
#6 Вывести result_subtr в консоль
print('result_subtr =', result_subtr, type(result_subtr))

#7 Создать переменную result_multi в которой вы умножаете item_1 на item_2.
result_multi = item_1 * item_2
#8 Вывести result_multi в консоль
print('result_multi =', result_multi, type(result_multi))

#9 Создать переменную result_exp в которой вы item_1 возводите в степень item_2.
result_exp = item_1 ** item_2
#10 Вывести result_exp в консоль
print('result_exp =', result_exp, type(result_exp))

#11 Создать переменную result_m_exp в которой вы item_1 возводите в степень item_2 используя библиотеку math.
result_m_exp = math.pow(2, 3)
#12 Вывести result_m_exp в консоль
print('result_exp =', result_exp, type(result_exp))

#13 Создать переменную result_s_root в которой вы найдёте квадратный корень любой из переменной item
result_s_root = item_1 ** 0.5
#14 Вывести result_s_root в консоль
print('result_s_root =', result_s_root, type(result_s_root))

#15 Создать переменную result_m_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math.
result_m_s_root = math.sqrt(item_1)
#16 Вывести result_m_s_root в консоль
print('result_m_s_root =', result_m_s_root, type(result_m_s_root))

#17 Создать переменную result_mp_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math используя метод pow.
result_mp_s_root = pow(item_1, 0.5)
#18 Вывести result_mp_s_root в консоль
print('result_mp_s_root =', result_mp_s_root, type(result_mp_s_root))

#19 Присвоить переменной item_1 odd значение
item_1 = 4
print('item_1 =', item_1, type(item_1))

#20 Присвоить переменной item_2 even значение
item_2 = 3
print('item_2 =', item_2, type(item_2))

#21 Создать переменную result_division в которой вы разделите item_1 на item_2
result_division = item_1 / item_2
#22 Вывести result_division в консоль
print('result_division =', result_division, type(result_division))

#22 Создать переменную result_m_floor и result_division округлить до ближайшего целого меньшего чем result_division.
result_m_floor = math.floor(result_division)
#23 Вывести result_m_floor в консоль
print('result_m_floor =', result_m_floor, type(result_m_floor))

#24 Создать переменную result_m_ceil и result_division округлить до ближайшего целого большего чем result_division.
result_m_ceil = math.ceil(result_division)
#25 Вывести result_m_ceil в консоль
print('result_m_ceil =', result_m_ceil, type(result_m_ceil))

#26 Создать переменную result_int и result_division округлить до ближайшего целого через явное приведение.
result_int = int(round(result_division))
#27 Вывести result_int в консоль
print('result_int =', result_int, type(result_int))

#28 Создать переменную result_no_division_loss в которой вы разделите item_1 на item_2 без остатка.
result_no_division_loss = item_1//item_2
#29 Вывести result_no_division_loss в консоль
print('result_no_division_loss =', result_no_division_loss, type(result_no_division_loss))

#30 Создать переменную result_division_loss в которой вы найдёте остаток от деления item_1 на item_2.
result_division_loss = item_1%item_2
#31 Вывести result_division_loss в консоль
print('result_division_loss =', result_division_loss, type(result_division_loss))

#32 Создать переменную item_3 и присвоить ей целое число
item_3 = 5

#33 Прибавить 10 к item_3 с присвоением
item_3 += 10
#34 Вывести item_3 в консоль
print('item_3 =', item_3, type(item_3))

#35 Отнять 5 от item_3 с присвоением
item_3 -= 5
#36 Вывести item_3 в консоль
print('item_3 =', item_3, type(item_3))

#37 Умножить item_3 на 3 с присвоением.
item_3 *= 3
#38 Вывести item_3 в консоль
print('item_3 =', item_3, type(item_3))

#39 Разделить item_3 на 2 с присвоением.
item_3 /= 2
#40 Вывести item_3 в консоль
print('item_3 =', item_3, type(item_3))

#41 Возвести в степень 2 item_3 с присвоением
item_3 **= 2
#42 Вывести item_3 в консоль
print('item_3 =', item_3, type(item_3))

#43 Найти квадратный корень item_3 с присвоением
item_3 **= 0.5
#44 Вывести item_3 в консоль
print('item_3 =', item_3, type(item_3))

#45 Присвоить остаток от деления item_3
item_3 %= item_3
#46 Вывести item_3 в консоль
print('item_3 =', item_3, type(item_3))

# 48. Создать переменную b_item_t и присвоить True
b_item_t = True
# 49. Создать переменную b_item_f и присвоить False
b_item_f = False
# 50. Создать переменную b_item_result_sum и присвоить сумму b_item_t и b_item_f
b_item_result_sum = b_item_t + b_item_f
# 51. Вывести b_item_relult_sum в консоль.
print('b_item_result_sum =', b_item_result_sum, type(b_item_result_sum))

# 52. Создать переменную b_item_result_subtr и присвоить разницу b_item_t и b_item_f
b_item_result_subtr = b_item_t - b_item_f
# 53. Вывести b_item_relult_subtr в консоль.
print('b_item_result_subtr =', b_item_result_subtr, type(b_item_result_subtr))

# 54. Создать переменную b_item_result_multi и присвоить умножение b_item_t и b_item_f
b_item_result_multi = b_item_t * b_item_f
# 55. Вывести b_item_result_multi в консоль.
print('b_item_result_multi =', b_item_result_multi, type(b_item_result_multi))

# 56. Создать переменную b_item_result_division и присвоить деление b_item_t и b_item_f
# b_item_result_division = b_item_t / b_item_f
# # 57. Вывести b_item_result_division в консоль. (Получить ошибку)
# print('b_item_result_division =', b_item_result_division, type(b_item_result_division))

# 58. Создать переменную b_item_1_int и присвоить явное приведение b_item_t к int
b_item_1_int = int(b_item_t)
# 59. Вывести b_item_1_int в консоль.
print('b_item_1_int =', b_item_1_int, type(b_item_1_int))

# 60. Создать переменную b_item_2_int и присвоить явное приведение b_item_2 к int
b_item_2_int = int(b_item_f)
# 61. Вывести b_item_2_int в консоль.
print('b_item_2_int =', b_item_2_int, type(b_item_2_int))
