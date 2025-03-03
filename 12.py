# # Срез списка
# #Основной синтаксис среза: list[начало:конец:шаг]
# lst = [10, 20, 30, 40, 50, 60, 70] # -> [20 30 40]
# # Получить все значения с индексом 1,2,3
# slice1 = lst [1:4] # 20 30 40
# slice2 = lst [:] # полный список
# slice3 = lst [::2] # [10, 30, 50, 70]
# slice4 = lst [-3: -1] # [50, 60]
# slice5 = lst[:: - 1] # [50, 60, 70
# slice6 = lst[3:] # [40, 50, 60, 70]
# slice7 = lst[:3] # [10, 20, 30]
#
# print(slice3)

# Генерация списков или list comprehension
# Синтаксический сахар  генератор списка - помогает создовать эффективно создавать новые с

#[выражение for элемент in список if условие]
#
# lst = [1, 2, 3, 4, 5]
# result = []
# for elem in lst:
#     result.append(elem*elem)
#
# result = [x*x for x in lst]

# lst = [1, 2, 3, 4, 5]
# result = []
# # for elem in lst:
# #     if elem % 2 == 0:
# #         result.append(elem)
#
# result = [elem for elem in lst if elem % 2 == 0]
#
# #Методы ist
# # append(x) -> добавляет х в конце списка
# # extend(x:list) -> расширяет первый список добавляя все элементы из списка х в конце оригинального списка
# lst = [1, 2, 3]
# lst2 = [4, 5, 6]
# new_list = lst + lst2
# lst.extend(lst2)
# # insert (i: int, х:Any) - вставляет
# # remove удаляет первый элемет значения х
# # pop - удаляет элемент со значением i, vtnj djpdhfoftn 'nj pyfxtybt
# #sort
# unsirted_list=[100, 8, 56, 44, 42]
# unsirted_list.sort()
# unsirted_list.sort(reverse=True)# 100 56 44 42 8
#
#
# lst = [1, 2, 3, 4, 5]
# my_val=lst.pop(1)
# print(lst)
# print(my_val)

#Строки (str)

# text = "\'"
# long_text = """
# cftuycvghjmvshk
# fasf
# saf
# fsf
# """
# #Сложение списков
# str1 = "Первая строка"
# str2 = "Вторая строка"
# str3 = str1 + str2
# #Умнжение списков
# str4 = a
# str5 = str*4
# print(str5)
# # f - сторока
# name = "test_name"
# age = 30
# str6=f"{name},возраст:{age}"
#join
words = ["word_1", "word_2", "word_3"]
sentence = " ".join(words)
print(sentence)

#Индексация сторк
my_str = "my string"
print(my_str[1]) # [y]
print(my_str[1:4]) #[y, s]

#Методы в строках
#Изменения в регистре
# .upper() - переводит строку в верхний регистр
my_str = "lower_case_str"
print(my_str.upper())
#lower() - переводит строгу внижний регистр
# capitalize - делает первую букву строки заглавной
# поиск и проверка
# .find (x: str)
main_str = "my_main_str"
str_to_be_found = main
index = main_str.find(str_to_be_found)

#.index(x: str) - вызывает ошибку
#replac (old:str,new:str)
text = "my_old_string"
print(text.replace("old","new"))

# даление пробелов
#.strip()
my_name = "test_username   "
new_username = my_name.strip()
#lstrip - left
#rstrip - right